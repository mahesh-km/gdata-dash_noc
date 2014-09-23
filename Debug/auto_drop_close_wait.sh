netstat -tonp | grep CLOSE_WAIT | awk '{print $5}' | sort  | awk -F: '{print $1}' | sort | uniq  > /tmp/list_of_ip



for IP in `cat /tmp/list_of_ip`; 
do 
 	COUNT=`netstat -tonp | grep $IP | grep CLOSE_WAIT | wc -l` ;  
	if [ $COUNT -gt 30 ] ; 
	then  
		echo IP $IP COUNT $COUNT ; 
		iptables -I INPUT -s $IP -j DROP; 
	fi; 
done

