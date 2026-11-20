#System Monitor Display
#This Code will read CPU temp, CPU usage, RAM usage, disk usage, and uptime.

import sys
import os
import subprocess
import time

#HEADER
#print('-' * 15 , "Raspberry Pi System Monitor Display", '-' * 15, '\n');

#define stat function
def get_stats():

	## Uptime Read
	result = subprocess.run(
		["uptime","-p"],
		capture_output=True,
		text=True
	)

	uptime = result.stdout.strip(); #strip removes whitespace/newlines

	## Temp Reading
	tempRead = subprocess.run(
		["vcgencmd","measure_temp"],
		capture_output=True,
		text=True
	)

	temp = tempRead.stdout.strip();

	## Read CPU Usage
	CPUcent = subprocess.run(
		"top -bn 2 -d 0.01 | grep '^%Cpu' | tail -n 1 | gawk '{print $2+$4+$6 \"%\"}' ",
		## Grabs line with CPU percentage usages and adds them
		shell=True,
		capture_output=True,
		text=True
	)

	cpusage = CPUcent.stdout.strip();

	## READ MEMORY USAGE
	ramUSG = subprocess.run(
		"top -bn 2 -d 0.01 | grep '^MiB Mem' | tail -n 1 | gawk '{print ($8/$4)*100}' ",
		shell=True,
		capture_output=True,
		text=True
	)

	ramCent = float(ramUSG.stdout.strip());

	## READ DISK USAGE
	diskUSG = subprocess.run(
		"df -h | grep '/dev/mmcblk0p2' | gawk '{print $5}' ",
		shell=True,
		capture_output=True,
		text=True
	)

	diskCent = diskUSG.stdout.strip();
	return uptime, temp, cpusage, ramCent, diskCent

			##PRINT EVTHING
if __name__ == "__main__":
	try:
		while True:
			uptime, temp, cpusage, ramCent, diskCent = get_stats()
			print(uptime);
			print("CPU USAGE:", cpusage);
			print(temp);
			print(f"RAM USAGE: {ramCent:.2f}%");
			print("DISK USAGE:", diskCent);


			time.sleep(1)
			os.system("clear")
		pass
	except KeyboardInterrupt:
		print("Program Exited by User")
		sys.exit(0); #Tell computer it exited successfully
