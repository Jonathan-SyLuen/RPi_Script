# To Sync RTC Clock
  1. Copy folder RTC_DS1302 to /home/pi/scripts
  2. Update the file 
  2. sudo vi /etc/rc.local
  3. Add this lines before "Close"
     python3 /home/pi/scripts/setTimeFromRTC
  4. Done... Reboot and try
  
 # To Sync Time from Internet
  1. in terminal, enter timedatectl
 
 # To Update RTC clock
  1. cd /home/pi/scripts/RTC_DS1302/
  2. python3 setTimeToRTC
  3. System time will be copied to RTC clock.
