TIME=`date +%Y-%m-%d-%H-%M-%S`
LOG="/opt/Debug/mmonit__restart.log"
echo "mmonit server rebooting..." $TIME | tee -a ${LOG}
pkill python
stop mmonit
start mmonit
