import argparse
from rich import print
from rich.panel import Panel
from rich.table import Table

# Initialize ArgumentParser to accept the --name argument
parser = argparse.ArgumentParser(description="A friendly CLI greeting tool built with rich.")
parser.add_argument("--name", default="World", help="The name of the person to greet.")
args = parser.parse_args()

# 1. Display a formatted welcome Panel
print(Panel.fit(
    f"[bold cyan]Welcome to open source, [bold yellow]{args.name}[/bold yellow]! Enjoy building cool projects![/]", 
    title="[bold magenta]OSS Hello Tool[/]", 
    border_style="magenta"
))

# 2. Display a structured rich Table
table = Table(title="[bold green]Practice Progress Checklist[/]", border_style="blue")

table.add_column("Check Item", style="bold cyan", justify="left")
table.add_column("Details", style="bold white", justify="left")
table.add_column("Status", style="bold green", justify="center")

table.add_row("Student Name", args.name, "Verified")
table.add_row("Library Used", "rich==15.0.0", "Installed")
table.add_row("Assignment Status", "Mini Assignment #8", "Completed")

print(table)