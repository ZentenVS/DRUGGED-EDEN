# DRUGGED-EDEN
# DRUGGED EDEN

A modular **OSINT reconnaissance and intelligence gathering tool** designed for penetration testers, security researchers, and ethical hackers.

DRUGGED EDEN automates the process of collecting publicly available intelligence from multiple sources such as **Google, GitHub, Shodan, Certificate Transparency logs, and the Wayback Machine**.

The tool is actively under development and new modules and improvements will be added over time.

---

# Features

### OSINT Modules

* Google Dork automation using Google Custom Search API
* GitHub code search for exposed secrets and repositories
* Shodan reconnaissance for exposed services and infrastructure
* Wayback Machine URL extraction for historical endpoints
* Subdomain enumeration using Certificate Transparency logs

### Security Features

* Scope enforcement system
* API error handling
* Rate limit protection
* Network timeout handling
* Modular design for easy expansion

---

# Modules

## Google Dork Search

Automates Google dorking through the **Google Custom Search API**.

Example use cases:

* Finding exposed files
* Discovering open directories
* Locating sensitive documents
* OSINT footprinting

---

## GitHub Code Search

Search GitHub repositories for:

* leaked API keys
* exposed credentials
* configuration files
* sensitive commits

Uses the **GitHub Search API** with optional authentication to bypass strict rate limits.

---

## Shodan Recon

Search internet-facing devices using the **Shodan API**.

Information gathered includes:

* IP addresses
* open ports
* organization names
* exposed infrastructure

Useful for infrastructure reconnaissance.

---

## Wayback URL Discovery

Extract archived URLs from the **Internet Archive Wayback Machine**.

Helps discover:

* old endpoints
* deleted pages
* hidden paths
* forgotten APIs

Useful during web application reconnaissance.

---

## Subdomain Enumeration

Enumerates subdomains using **Certificate Transparency logs (crt.sh)**.

Helps discover:

* forgotten subdomains
* staging environments
* internal infrastructure

---

# Scope System

The tool includes a **built-in scope restriction system** to prevent scanning outside authorized targets.

Example:

```
Enter allowed domains (comma-separated):
example.com,example.org
```

All modules will automatically enforce this scope.

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/drugged-eden.git
```

Navigate to the directory

```
cd drugged-eden
```

Install dependencies

```
pip install -r requirements.txt
```

---

# API Configuration

DRUGGED EDEN uses several external APIs for OSINT data collection.
Before running the tool, you must configure the required API keys inside the script.

Open the main script and locate the configuration section.

```python
GOOGLE_API_KEY = "put_api_key"
GITHUB_TOKEN = "put_github_token"
GOOGLE_CSE_ID = "put_cse_id"
SHODAN_API_KEY = "put_shodan_key"
```

Replace the placeholder values with your own API credentials.

---

# Google Custom Search API (Required for Google Dorks)

This is required for the **Google Dork module**.

Step 1 — Create a Google Cloud Project
https://console.cloud.google.com/

Step 2 — Enable the **Custom Search API**

Step 3 — Create an API Key

Step 4 — Create a Custom Search Engine
https://programmablesearchengine.google.com/

Configure the search engine to **search the entire web**.

After creating it, copy:

* API Key
* Custom Search Engine ID (CSE ID)

Insert them into the script.

```python
GOOGLE_API_KEY = "your_google_api_key"
GOOGLE_CSE_ID = "your_search_engine_id"
```

---

# GitHub Token (Recommended)

Used for the **GitHub Code Search module**.

Without a token you will quickly hit GitHub rate limits.

Step 1 — Go to

https://github.com/settings/tokens

Step 2 — Generate a **Personal Access Token**

Recommended permissions:

* public_repo
* read:org

Insert the token into the script.

```python
GITHUB_TOKEN = "your_github_token"
```

---

# Shodan API Key

Required for the **Shodan Recon module**.

Step 1 — Create an account

https://account.shodan.io

Step 2 — Copy your API key from the dashboard

Step 3 — Add it to the script

```python
SHODAN_API_KEY = "your_shodan_api_key"
```

Note: Some Shodan features require a paid account.

---

# Verifying Configuration

After inserting the API keys, run the tool:

```bash
python main.py
```

If the keys are configured correctly, the OSINT modules will begin returning results.

---

# Security Tip

Do **not commit your API keys to public repositories**.

If publishing the project on GitHub, it is recommended to:

* use environment variables
* create a `.env` file
* or remove keys before pushing

```

---

# Configuration

Before running the tool you must configure your API keys.

Edit the script and insert your keys:

```
GOOGLE_API_KEY = "your_google_api_key"
GOOGLE_CSE_ID = "your_custom_search_engine_id"
GITHUB_TOKEN = "your_github_token"
SHODAN_API_KEY = "your_shodan_api_key"

---

# Usage

Run the tool

```
python main.py
```

Main menu

```
[1] OSINT
[0] EXIT
```

OSINT menu

```
[1] Google Dork
[2] Github search
[3] Shodan Recon
[4] Wayback URLs
[5] Subdomain Enumeration
[6] Set Scope
[0] Back
```


# Example Workflow

1. Set scope
2. Run subdomain enumeration
3. Extract historical URLs
4. Search GitHub for leaked credentials
5. Run Google dorks for sensitive files

This creates a strong **recon pipeline during the early stages of penetration testing**.

---

# Roadmap

Planned future features

* Username OSINT modules
* Email intelligence gathering
* Metadata extraction
* DNS reconnaissance
* Automated recon pipelines
* Report generation
* Multi-threaded scanning
* Additional OSINT APIs

---

# Disclaimer

This tool is intended **for educational purposes and authorized security testing only**.

The developer is not responsible for misuse of this software. Always ensure you have **proper authorization before performing reconnaissance or penetration testing**.

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

Bug reports and feature suggestions are appreciated.

---

# License

MIT License

---

# Author

Developed by the Zenten project.
More modules and improvements will be added over time.
discord- zentenv



