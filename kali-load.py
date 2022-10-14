import os
import sys
import time
import requests

try:
	requests.get("https://www.google.com", timeout=5)
except:
	print("\n\033[1;91mOFFLINE.\033[0;0m")
	sys.exit()
	
os.system("clear")

print("""\033[1;91m

   ██╗  ██╗ █████╗ ██╗     ██╗    ██╗      ██████╗  █████╗ ██████╗
   ██║ ██╔╝██╔══██╗██║     ██║    ██║     ██╔═══██╗██╔══██╗██╔══██╗
   █████╔╝ ███████║██║     ██║    ██║     ██║   ██║███████║██║  ██║
   ██╔═██╗ ██╔══██║██║     ██║    ██║     ██║   ██║██╔══██║██║  ██║
   ██║  ██╗██║  ██║███████╗██║    ███████╗╚██████╔╝██║  ██║██████╔╝
   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝
                                                  \033[1;0m Cyber Anonymous
\033[0;0m""")
print("")
print("")
print("")
print("")
print("")
print("\033[1;92m[1]\033[1;0m Install Kali Linux")
print("\033[1;92m[2]\033[1;0m Uninstall Kali Linux")
print("")
print("")
try:
	option = input("\nSELECT OPTION: ")
except:
	pass
try:
	option=int(option)
except:
	print("\n\033[1;91m[!] Invalid option!\033[0;0m\n")
	sys.exit()
	
print("")
if(option==1):
	os.system("""

apt-get update -y
apt-get upgrade -y

pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh
	
	""")

	try:
		requests.get("https://www.google.com", timeout=5)
	except:
		print("\n\033[1;91mOFFLINE.\033[0;0m")
		sys.exit()

	while(True):
		desktop_environment=input("\n\033[1;93mDo you want to install desktop environment (Y/n):\033[0;0m ").lower()
		
		if(desktop_environment=="y" or desktop_environment=="n"):
			break
		else:
			print("\n\033[1;91m[!] Invalid option!\033[0;0m")
			pass
	print("\n")

	if (desktop_environment == "y"):
	 	
		os.system("chmod +x start-kali.sh")
		print("\n\033[1;92mRun the below command in Kali Linux.\033[0;0m")
		print("")
		print("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/de-apt-xfce4.sh && bash de-apt-xfce4.sh")
		print("\n")
		time.sleep(2)
		os.system("./start-kali.sh")
	
	elif (desktop_environment == "n"):
		pass
	
	else:
		print("\n\033[91m[!] Invalid option! \033[0;0m")
		


elif(option==2):

	try:
		requests.get("https://www.google.com", timeout=5)
	except:
		print("\n\033[1;91mOFFLINE.\033[0;0m")
		sys.exit()
		
	os.system("""
	wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Uninstaller/Kali/UNI-kali.sh && bash UNI-kali.sh
	""")
	
else:
	print("\n\033[1;91m[!] Invalid option!\033[0;0m\n")
	
