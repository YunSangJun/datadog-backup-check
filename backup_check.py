# stdlib
from fnmatch import fnmatch
from os import stat
from os.path import abspath, exists, join
from datetime import datetime, timedelta
 
# 3p
from scandir import walk
 
# project
from checks import AgentCheck
from config import _is_affirmative
 
class BackupCheck(AgentCheck):
    """This check is for monitoring and reporting metrics on cf backup
    WARNING: the user/group that dd-agent runs as must have access to stat the files in the desired directory
    Config options:
        "directory" - string, backup directory. required
        "name" - string, backup service name. Required
    """
    SOURCE_TYPE_NAME = 'system'
 
    def check(self, instance):
        if "directory" not in instance:
            raise Exception('DirectoryCheck: missing "directory" in config')
 
        directory = instance["directory"]
        abs_directory = abspath(directory)
        name = instance.get("name")
        service_check_tags = ['name:%s' % name]
 
        if not exists(abs_directory):
            raise Exception("DirectoryCheck: the directory (%s) does not exist" % abs_directory)
        current_datetime = datetime.now()
        # pattern for checking backup
        pattern = current_datetime.strftime('*%Y%m%d*')
        print ("pattern : %s"  % pattern)
 
        hasBackup = False
 
        #compare backup file date to current date
        for root, dirs, files in walk(abs_directory):
            for filename in files:
                filename = join(root, filename)
                print ("filename : %s"  % filename)
 
                if fnmatch(filename, pattern):
                   hasBackup = True
                   break
 
        print ("hasBackup : %s"  %hasBackup)
  
        #check backup file size is above 0
        try:
            file_stat = stat(filename)
        except OSError as ose:
            self.warning("DirectoryCheck: could not stat file %s - %s" % (filename, ose))
            status = AgentCheck.WARNING
            self.service_check("backup.state", status, tags=service_check_tags, message="Could not get file information. Please check the file.")
        else:
            if file_stat.st_size <= 0:
                status = AgentCheck.WARNING
                self.service_check("backup.state", status, tags=service_check_tags, message="Backup file size is under 0 byte. Please check the file.")
 
        if not hasBackup:
            status = AgentCheck.CRITICAL
            self.service_check("backup.state", status, tags=service_check_tags)
        else:
            status = AgentCheck.OK
            self.service_check("backup.state", status, tags=service_check_tags)
