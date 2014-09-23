s script used to manage ip address.         #
#Basicly that take each ip and done a ping test #
#and if need, add to ip block                   #
#-----------------------------------------------#
#
#declare -i p
limit=400
for hos in `cat /opt/Debug/Dl_Dyndns_hostnames`
do
        address1=`host $hos | awk '{print $1}'`
        address=`host $hos | awk '{print $4}'`
        echo $address1  $address
        echo "**************************************************************************************"
        if [ $address == "216.146.39.125" ]
        then
                echo "Host in offine state!"
        else


#               p=`ping -w 5 $hos | awk -F '[time= ]' '{print $10}'`
#               if [[ -z "$p" ]]
#               then 
#                       echo "start"
#               else
#                       echo "Time $p" 
#                       if [ "$p" > "$limit" ]
#                       then 
                                ping  -w 5 $hos
                                # echo "You Need to Drop this $address IP address, Enter 'y' for Drop or 'n' , then [ENTER]"
                                #read input
                                # if [ "$input" == "y" ]
                                # then
                               #         iptables -I INPUT -s $address -j DROP
                                #        echo "****** IP $address added to iptable"
                                #elif [ "$input" == "n" ]
                                #then
                                 #       echo "pass"
                                #fi
#                       else
#                               echo "pass!"
#                       fi
#               fi
        fi
        echo "---------------------------------------------------------------------------------------"
done

