#Will display system data using percentage bars.

import time
import sys

from rich.table import Table
from rich.bar import Bar
from rich.align import Align
from rich.live import Live
from rich.console import Console
from rich.panel import Panel
from monitor import get_stats

console=Console();

#Format table
table = Table(show_header=False, box=None)


try:
	with Live (Align.center(Panel("Loading...")), console=console, refresh_per_second=4,screen=True) as live:

		while True:
			uptime, temp, cpusage, ramCent, diskCent = get_stats();

			CPUSG = float(cpusage.replace("%", ""))
			DSKUSG = float(diskCent.replace("%", ""))

			barRAM = Bar(size=100, begin=0, end=ramCent, color = "cyan")
			barCPUSAGE = Bar(size=100, begin=0, end=CPUSG, color = "magenta")
			barDSKUSG = Bar(size=100, begin=0, end=DSKUSG, color ="red")

			#Format table
			table = Table(show_header=False, box=None)

			table.add_column("Metric", width=20)
			table.add_column("Bar" , width=30)
			table.add_column("Percentage", width=20)

			table.add_row("",Align.center(f"{uptime}"))
			table.add_row(f"{temp}")
			table.add_row("CPU usage", barCPUSAGE, f"{cpusage}")
			table.add_row("RAM usage", barRAM, f"{ramCent:.2f}%")
			table.add_row("DISK usage", barDSKUSG, f"{diskCent}")

			panel = (Align.center(Panel(table, title = "System Monitor")))

			live.update(panel)
			time.sleep(0.25)
except KeyboardInterrupt:
	with Live (Align.center(Panel("Exiting Program...")),screen=True) as live:
		time.sleep(0.8)
	print("Dashboard Closed\n")
	sys.exit(0)


