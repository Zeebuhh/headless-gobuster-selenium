# Headless Gobuster with Selenium

This script is a **headless directory brute-forcer** that attempts to discover hidden directories and endpoints on a target web application. It is particularly useful for **Single Page Applications (SPA)** that dynamically load content via JavaScript.

## Features

- Uses **Selenium** to interact with web pages dynamically.
- Detects hidden directories by monitoring changes in the **page source length**.
- Runs in **headless mode** for faster execution.
- Supports a **custom wordlist** for brute-forcing endpoints.

---

## **Installation**

### **1️ Install Selenium**

```bash
#bash
pip install selenium
```

### **2️ Install WebDriver**

This script requires a WebDriver to control the browser. For Firefox, install **GeckoDriver**:

```bash
#bash
sudo apt install -y firefox-geckodriver
```

Or manually:

```bash
#bash
wget https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-linux64.tar.gz
sudo tar -xvzf geckodriver-linux64.tar.gz -C /usr/local/bin/
chmod +x /usr/local/bin/geckodriver
```

For **Chrome**, install **Chromedriver**:

```bash
#bash
sudo apt install -y chromium-chromedriver
```

Ensure the WebDriver is in your system's PATH.

Verify the installation:

```bash
#bash
geckodriver --version  # For Firefox
chromedriver --version  # For Chrome
```

---

## **Usage**

Run the script with the following parameters:

```bash
#bash
python gobuster_selenium.py --url <TARGET_URL> --w <WORDLIST>
```

### **Example:**

```bash
#bash
python gobuster_selenium.py --url http://127.0.0.1:3000/ --w ~/Desktop/wordlist.txt
```

### **Arguments:**

`--url` - The target base URL (e.g., `http://example.com`)

`--w` - Path to the wordlist file containing directories to test

---

## **How It Works**

1. The script reads **each line from the wordlist** and appends it to the base URL.
2. It then **opens the URL in a headless browser instance** using Selenium.
3. The script checks if the **HTML content dynamically changes**, indicating that the directory exists.
4. If a directory is found, it prints `[+] Gefunden: <URL>` (found), otherwise `[-] Nicht gefunden: <URL>` (not found).

---

## **Code Overview**

### **1️ Argument Parsing**

The script uses `argparse` to accept user-defined parameters (`--url`, `--w`).

### **2️ Selenium WebDriver Setup**

- Runs **the selected browser in headless mode** for performance.
- Uses **the appropriate WebDriver** (GeckoDriver for Firefox, ChromeDriver for Chrome).

### **3️ Checking Directories**

- The script **loads each URL** and captures its initial **HTML length**.
- It then **waits for the page content to change** within 5 seconds.
- If the page **loads new content**, the directory is considered **found**.

---

## **Disclaimer**

This script is intended for **educational and ethical use only**. Do **not** use it on unauthorized systems without permission. The author assumes **no responsibility** for misuse.
