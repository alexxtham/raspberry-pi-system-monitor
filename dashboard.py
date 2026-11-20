# Python's Rich library test
import subprocess
import time
import sys

from rich.align import Align
from rich.live import Live
from rich.console import Console
from rich.panel import Panel
from monitor import get_stats

console=Console();
try:
	with Live (Align.center(Panel("Loading...")), console=console, refresh_per_second=4,screen=True) as live:

		while True:
			uptime, temp, cpusage, ramCent, diskCent = get_stats();


			panel = (Align.center(Panel(f"""{uptime}
{temp}
CPU USAGE: {cpusage}
RAM USAGE: {ramCent:.2f}%
DISK USAGE: {diskCent}""",
			title = "System Monitor"))
				)
			live.update(panel)
			time.sleep(0.25)

except KeyboardInterrupt:
	with Live (Align.center(Panel("Exiting Program...")),screen=True) as live:
		time.sleep(1.5)
	print("Dashboard Closed\n")
	sys.exit(0)
