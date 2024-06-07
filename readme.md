# URL and Endpoint Extractor Tool

This tool helps in extracting all URLs and endpoints from a given domain using the Internet Archive. It validates the URL format and checks its existence before fetching the URLs. This tool is useful for security researchers, developers, and anyone interested in retrieving historical URLs for analysis or testing.

## Features

- **URL Format Validation**: Ensures the input URL is in a correct format.
- **URL Existence Check**: Verifies that the URL is reachable before proceeding.
- **Fetch Historical URLs**: Uses the Internet Archive to retrieve historical URLs associated with the given domain.
- **Save URLs to File**: Saves the fetched URLs to a specified output file.
- **User-friendly Interface**: Provides clear instructions and colored prompts for a better user experience.

## Installation

To use this tool, you need to have Python installed. You can install the required libraries using `pip`:

```bash
pip install requests validators termcolor
```

## Usage
- Clone the repository:
```bash
git clone https://github.com/shivangmauryaa/pythawayback.git
cd pythawayback
```
- Run the script:
```bash
python script.py
```
- Follow the prompt to enter the domain:
- Example: example.com (Do not add http:// or https://)

## Script Description
- The script prompts the user to enter a domain and performs the following steps:

- The script prompts the user to enter a domain and performs the following steps:
- URL Validation: Checks if the entered URL is in a valid format.
- Existence Check: Makes a HEAD request to ensure the URL is reachable.
- Fetch URLs: Constructs a query to the Internet Archive to retrieve historical URLs.
- Save to File: Saves the fetched URLs to a file named urls.txt.

# Example
```bash

URL Format eg pythagorex.com, Do Not Add HTTPS or HTTP.
Enter URL: example.com
URL exists
All URLs have been successfully saved to urls.txt
```
