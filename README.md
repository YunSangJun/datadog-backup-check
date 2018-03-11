# datadog-backup-check

Use Datadog custom check feature to automatically check if backups are handled properly and generate an alarm if back up can not be done

Reference : http://docs.datadoghq.com/guides/agent_checks/

## Configure directory checking backup

1. Create "backup_check.yaml" file to the "/etc/dd-agent/conf.d" directory

2. Configure "backup_check.yaml"
```
init_config:
 
instances:
  # This check is for monitoring and reporting metrics on cf backup
  #
  # WARNING: Ensure the user account running the Agent (typically dd-agent) has read
  # access to the monitored directory and files.
  #
  # Instances take the following parameters:
  # "directory" - string, the directory to monitor. Required
  # "name" - string, backup service name. Required
 
  - directory: "/root/backup/mariadb"
    name: "mariadb"
```

* dd-agent should have permission to access the folder

* Backup folder should have an 755 authority

## Copy backup check script file

Copy the "backup_check.py" file to the "/etc/dd-agent/checks.d" folder

## Datadog agent restart
```
sudo /etc/init.d/datadog-agent restart
```

## Datadog agent info check
```
sudo /etc/init.d/datadog-agent info
```

## Create Monitor in Datadog

1. Monitos > New Monitor > Custom check

2. Configure Datadog
```
Pick a Custom Check : backup.state
Pick monitor scope : host:HOST_NAME
Set alert conditions
  Status: Critical => 1
  Status: OK => 1
```
  
## Check list

1. Whether file is backed up or not


2. File size


3. File status
