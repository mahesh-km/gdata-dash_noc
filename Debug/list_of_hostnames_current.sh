for HOSTNAME in `cat list_of_hostnames` ; 
do 
	IP=`host $HOSTNAME | awk '{print $4}'`; 
	echo $HOSTNAME $IP; 
done  > list_of_hostnames_current 
