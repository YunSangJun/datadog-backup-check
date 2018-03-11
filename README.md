# datadog-backup-check

Use Datadog custom check feature to automatically check if backups are handled properly and generate an alarm if backup can not be done

Reference : http://docs.datadoghq.com/guides/agent_checks/

1. Copy 'backup_check.yaml' file to '/etc/dd-agent/conf.d' folder

  * dd-agent가 해당 폴더에 접근할 수 있도록 권한이 있어야 함.

  * /root, /root/backup/, /root/backup/cf-ccdb 에 755 권한이 있어야 함.

2. /etc/dd-agent/checks.d 폴더에 backup_check.py 파일 복사

3. datadog agent 재시작
sudo /etc/init.d/datadog-agent restart

4. check
sudo /etc/init.d/datadog-agent info

5. Create Monitor in Datadog

  5.1. Monitos > New Monitor > Custom check

  5.2. Configure Datadog
  ```
  Pick a Custom Check : backup.state
  Pick monitor scope : host:HOST_NAME
  Set alert conditions
    Status: Critical => 1
    Status: OK => 1
  ```
  
6. 체크 항목
6.1. 파일 유무
현재 날짜로 백업된 파일이 있는지 체크
6.2. 파일 크기
파일 크기가 0 이상인지 체크
6.3. 파일 상태
파일 상태에 이상이 없는지 체크
