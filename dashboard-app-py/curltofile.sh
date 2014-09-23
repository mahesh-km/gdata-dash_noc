#!/bin/bash 
DATE=`date +%d-%m-%Y`
TIME=`date +%H:%M:%S`
LOG="/opt/dashboard-app/curltofile.log"
echo "start reading JSON" ${DATE}${TIME} | tee ${LOG}
curl -c ~/.mmonit/cookie http://mmonit.vyoma-media.com:10002/index.csp > /dev/null 2>&1
curl -b ~/.mmonit/cookie -d z_username=admin -d z_password=****** http://mmonit.vyoma-media.com:10002/z_security_check > /dev/null 2>&1
curl -b ~/.mmonit/cookie http://mmonit.vyoma-media.com:10002/status/hosts/list > /opt/dashboard-app/json.txt 
curl -b ~/.mmonit/cookie http://mmonit.vyoma-media.com:10002/login/logout.csp > /dev/null 2>&1
echo "Reading Ends" ${TIME} | tee -a ${LOG}
