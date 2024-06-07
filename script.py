import requests
import validators
from termcolor import colored

def check_url_exists(url):
    if not validators.url(url):
        return False, "Invalid URL format"

    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True, "URL Exists,Process Has Been Started"
        else:
            return False, f"URL returned a status code of {response.status_code}"
    except requests.RequestException as e:
        return False, f"URL is not reachable"

def fetch_and_save_urls(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        raw_urls = response.text

        with open(output_file, "w") as file:
            file.write(raw_urls)

        print(f"All URLs have been successfully saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

prompt_text = colored("URL Format eg pythagorex.com, Do Not Add HTTPS or HTTP.", 'green')
enter_text = colored("Enter URL:", 'blue')

print(prompt_text)
link = input(enter_text)

full_url = f"http://{link}"
is_valid, message = check_url_exists(full_url)

if is_valid:
    print(colored(message, 'green'))
    url = f"https://web.archive.org/cdx/search/cdx?url=*.{link}/*&output=text&fl=original&collapse=urlkey"
    output_file = "urls.txt"
    fetch_and_save_urls(url, output_file)
else:
    print(colored(message, 'red'))
