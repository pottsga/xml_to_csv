import argparse
import pandas as pd
from rich.console import Console
import os
from urllib.parse import urlparse

console = Console()

def is_url(path):
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert an XML file or URL to CSV.')
    parser.add_argument('xml_source', help='The XML file or URL to convert')
    parser.add_argument('--output', default='output.csv', help='The output CSV file (default: output.csv)')
    args = parser.parse_args()

    console.print("[bold green]Reading XML source...[/bold green]")
    if is_url(args.xml_source):
        df = pd.read_xml(args.xml_source)
    else:
        if not os.path.isfile(args.xml_source):
            console.print(f"[bold red]Error: File {args.xml_source} does not exist.[/bold red]")
            return
        df = pd.read_xml(args.xml_source)

    df.to_csv(args.output, index=False)
    console.print(f"[bold green]Conversion complete! CSV saved as [bold yellow]{args.output}[/bold yellow].[/bold green]")

if __name__ == '__main__':
    main()