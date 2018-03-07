# datadog-backup-check

Datadog custom check 기능을 사용하여 백업이 정상처리되는지 자동으로 체크하고 백업이 되지 않는 경우 알람을 발생

Reference : http://docs.datadoghq.com/guides/agent_checks/

1./etc/dd-agent/conf.d 폴더에 backup_check.yaml 파일 복사
*dd-agent가 해당 폴더에 접근할 수 있도록 권한이 있어야 함.
*/root, /root/backup/, /root/backup/cf-ccdb 에 755 권한이 있어야 함.

2./etc/dd-agent/checks.d 폴더에 backup_check.py 파일 복사

3.datadog agent 재시작
sudo /etc/init.d/datadog-agent restart

4.check
sudo /etc/init.d/datadog-agent info

5.Create Monitor in Datadog
1)Monitos > New Monitor > Custom check
2)Configure Datadog
Pick a Custom Check : backup.state
Pick monitor scope : host:HOST_NAME
Set alert conditions
  Status: Critical => 1
  Status: OK => 1
  
  
6.체크 항목
-파일 유무
현재 날짜로 백업된 파일이 있는지 체크
-파일 크기
파일 크기가 0 이상인지 체크
-파일 상태
파일 상태에 이상이 없는지 체크
