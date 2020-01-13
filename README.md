This is IoT based Weather Station with Pi 3b+ with real time monitoring   : 


SSH 
1.	Create a blank text file named ‘ssh’ in the boot drive of pi.
2.	Create another file with ‘unix EOL conversion’ and name that as “ wpa_supplicant.conf “ 
3.	Then add the following codes with your own SSID and password:

country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
scan_ssid=1
ssid="Your-SSID"
psk="Your-PSK"
key_mgmt=WPA-PSK
}



4.	You can login to your pi with any terminal by knowing the IP of the Pi. You can use the app ‘Fing’ to find the IP of Pi.
Codes
Codes are attached in the separate files. 
1.	Coding for BME 280 and SGP30 are in a single file – ‘Final1.py’ which is written in python3. 
2.	Coding for SI1145 is in file – ‘Final2.py’ . It is written in python, as there was no library in python3. I have managed to get one library with works on python only and its unofficial.
3.	The codes for ph sensor is in fill ‘Final3.py’ and it is written python3. 

