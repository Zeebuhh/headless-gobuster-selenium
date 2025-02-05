from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService

import argparse

# PARSE ARGS

parser = argparse.ArgumentParser(description="Parser for headless gobuster")
parser.add_argument("--url", type=str, required=True ,help="Target base url")
parser.add_argument("--w", type=str, required=True , help="Path to wordlist")

args = parser.parse_args()

Url = args.url
Wordlist = args.w

# CONFIGURE SELENIUM

driver_path = "/usr/local/bin/geckodriver"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

service = FirefoxService(driver_path)
driver = webdriver.Firefox(service=service, options=options)

# FUNCTIONS

def check_directory(url):
    
    driver.get(url)

    try:
        initial_length = len(driver.page_source)

        WebDriverWait(driver, 5).until(
            lambda d: len(driver.page_source) != initial_length
        )
        
        print(f"[+] FOUND: {url}")
    except:
        pass

# LOOP OVER WORDLIST AND CHECK FOR EVERY WORD

def main():
    try:
        with open(Wordlist, "r") as file:
            for line in file:
                directory = line.strip()
                full_url = f"{Url}/{directory}"
                check_directory(full_url)
    except Exception as e:
        print(f"[X] Error: {e}")
    finally:
        print("----------- SCANNING COMPLETE ----------")
        driver.quit() 

if __name__ == "__main__":
    main()
