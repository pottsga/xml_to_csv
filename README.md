# XML to CSV Converter

A simple command-line tool to convert XML sources (files and URLS) to CSV format.

## Installation

```bash
python3 -m venv env
env/bin/pip install .
```

## Usage

```bash
env/bin/xml_to_csv <xml_file>
env/bin/xml_to_csv source_file.xml
env/bin/xml_to_csv source_file.xml --output /home/user/output.csv

env/bin/xml_to_csv <xml_url>
env/bin/xml_to_csv https://example.com/source
env/bin/xml_to_csv https://example.com/source --output /home/user/output.csv
```

## Features

- Convert XML files to CSV format
- Convert XML URLs to CSV format
- Save the output to a file

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.