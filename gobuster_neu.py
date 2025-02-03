from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
import argparse 

# PARSE ARGS

parser = argparse.ArgumentParser(description="Parser for headless gobuster")

parser.add_argument("--url", type=str, required=True ,help="Target base url")
parser.add_argument("--w", type=str, required=True , help="Path to wordlist")

args = parser.parse_args()

url = args.url
wordlist = args.w

# CONFIGURE SELENIUM

driver_path = "/usr/local/bin/geckodriver"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path=driver_path, options=options)

# FUNCTIONS

def check_directory(url):
    
    driver.get(url)

    try:
        initial_length = len(driver.page_source)

        WebDriverWait(driver, 5).until(
            lambda driver: len(driver.page_source) > initial_length
        )
        
        print(f"[+] Gefunden: {url}")
    except:
        print(f"[-] Nicht gefunden: {url}")

# LOOP OVER WORDLIST AND CHECK EVERY WORD

def main():
    try:
        with open(wordlist, "r") as file:
            for line in file:
                directory = line.strip()
                full_url = f"{url}/{directory}"
                check_directory(full_url)
    except Exception as e:
        print(f"[X] Error: {e}")
    finally:
        print("----------- SCANNING COMPLETE ----------")



if __name__ == "__main__":
    main()