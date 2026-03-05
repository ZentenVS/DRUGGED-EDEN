import requests
import time
import os
import sys
import threading
import re
from bs4 import BeautifulSoup

# =========================
# CONFIG (INSERT YOUR KEYS)
# =========================
GOOGLE_API_KEY = "put_api_key"
GITHUB_TOKEN = "put_github_token"
GOOGLE_CSE_ID = "put_cse_id"
SHODAN_API_KEY = "put_shodan_key"

ALLOWED_DOMAINS = []

# =========================
# BANNERS (UNCHANGED)
# =========================
MAIN_BANNER = """
░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░


███▄ ▄███▓▄▄▄     ▓█████▄▓█████     ▄▄▄▄▓██   ██▓   ▒███████▓█████ ███▄    █▄▄▄█████▓█████ ███▄    █ 
▓██▒▀█▀ ██▒████▄   ▒██▀ ██▓█   ▀    ▓█████▒██  ██▒   ▒ ▒ ▒ ▄▀▓█   ▀ ██ ▀█   █▓  ██▒ ▓▓█   ▀ ██ ▀█   █ 
▓██    ▓██▒██  ▀█▄ ░██   █▒███      ▒██▒ ▄█▒██ ██░   ░ ▒ ▄▀▒░▒███  ▓██  ▀█ ██▒ ▓██░ ▒▒███  ▓██  ▀█ ██▒
▒██    ▒██░██▄▄▄▄██░▓█▄   ▒▓█  ▄    ▒██░█▀ ░ ▐██▓░     ▄▀▒   ▒▓█  ▄▓██▒  ▐▌██░ ▓██▓ ░▒▓█  ▄▓██▒  ▐▌██▒
▒██▒   ░██▒▓█   ▓██░▒████▓░▒████▒   ░▓█  ▀█░ ██▒▓░   ▒███████░▒████▒██░   ▓██░ ▒██▒ ░░▒████▒██░   ▓██░
░ ▒░   ░  ░▒▒   ▓▒█░▒▒▓  ▒░░ ▒░ ░   ░▒▓███▀▒██▒▒▒    ░▒▒ ▓░▒░░░ ▒░ ░ ▒░   ▒ ▒  ▒ ░░  ░░ ▒░ ░ ▒░   ▒ ▒ 
░  ░      ░ ▒   ▒▒ ░░ ▒  ▒ ░ ░  ░   ▒░▒   ▓██ ░▒░    ░░▒ ▒ ░ ▒░ ░  ░ ░░   ░ ▒░   ░    ░ ░  ░ ░░   ░ ▒░
░      ░    ░   ▒   ░ ░  ░   ░       ░    ▒ ▒ ░░     ░ ░ ░ ░ ░  ░     ░   ░ ░  ░        ░

"""

OSINT_BANNER = """
 ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄
█      █ █ █   ▐ █   █  █  █  █ █ █ █    █  ▐
█      █    ▀▄   ▐   █  ▐  ▐  █  ▀█ ▐   █
▀▄    ▄▀ ▀▄   █      █       █   █     █
  ▀▀▀▀    █▀▀▀    ▄▀▀▀▀▀▄  ▄▀   █    ▄▀
          ▐      █       █ █    ▐   █
                 ▐       ▐ ▐        ▐
"""

# =========================
# SCOPE ENFORCEMENT
# =========================
def set_scope():
    global ALLOWED_DOMAINS
    domains = input("Enter allowed domains (comma-separated): ")
    ALLOWED_DOMAINS = [d.strip() for d in domains.split(",") if d.strip()]
    print("[✓] Scope set:", ALLOWED_DOMAINS)

def in_scope(target):
    if not ALLOWED_DOMAINS:
        return True
    return any(d in target for d in ALLOWED_DOMAINS)

# =========================
# OSINT MODULES
# =========================
def google_dork():
    dork = input("Google dork: ").strip()
    if not dork:
        print("[-] Empty dork")
        return

    if not in_scope(dork):
        print("[-] Outside allowed scope")
        return

    print("[*] Running Google dork search...\n")

    results_found = 0
    start = 1

    while start <= 91:  # Google API limit
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": dork,
            "num": 10,
            "start": start
        }

        r = requests.get(
            "https://www.googleapis.com/customsearch/v1",
            params=params,
            timeout=10
        )

        data = r.json()

        # 🔴 API error handling
        if "error" in data:
            print("[-] Google API error:")
            print(data["error"]["message"])
            break

        items = data.get("items")
        if not items:
            break

        for item in items:
            link = item.get("link")
            if link:
                print("[+] ", link)
                results_found += 1

        start += 10
        time.sleep(1)

    if results_found == 0:
        print("\n[!] No results returned.")
        print("Possible reasons:")
        print("- CSE not set to search entire web")
        print("- Dork filtered by Google API")
        print("- API quota exceeded")
    else:
        print(f"\n[✓] Total URLs found: {results_found}")

def github_code_search():
    query = input("GitHub search query: ").strip()
    if not query:
        print("[-] Empty query")
        return

    if not in_scope(query):
        print("[-] Outside allowed scope")
        return

    print("[*] Running GitHub code search...\n")

    url = "https://api.github.com/search/code"
    params = {
        "q": query,
        "per_page": 10
    }

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "osint-tool"
    }

    # 🔐 Auth token support
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)

        if r.status_code == 403:
            print("[-] GitHub rate limit hit")
            print(r.headers.get("X-RateLimit-Remaining"))
            return

        if r.status_code != 200:
            print(f"[-] GitHub API error: {r.status_code}")
            print(r.text[:300])
            return

        data = r.json()

    except Exception as e:
        print("[-] Request failed:", e)
        return

    items = data.get("items", [])
    if not items:
        print("[!] No results found")
        return

    for item in items:
        print("[+] ", item.get("html_url"))

    print(f"\n[✓] Total results: {len(items)}")


def shodan_recon():
    query = input("Shodan query: ").strip()
    if not query:
        print("[-] Empty query")
        return

    if not in_scope(query):
        print("[-] Outside allowed scope")
        return

    url = "https://api.shodan.io/shodan/host/search"
    params = {
        "key": SHODAN_API_KEY,
        "query": query
    }

    try:
        r = requests.get(url, params=params, timeout=10)

        # 🔴 HTTP-level error (401, 403, 429, etc.)
        if r.status_code != 200:
            print(f"[-] Shodan HTTP error: {r.status_code}")
            print(r.text[:300])
            return

        # 🔴 Shodan sometimes returns NON-JSON
        if not r.text.strip().startswith("{"):
            print("[-] Shodan returned non-JSON response")
            print(r.text[:300])
            return

        data = r.json()

    except requests.exceptions.RequestException as e:
        print("[-] Network error:", e)
        return

    except ValueError:
        print("[-] JSON parse failed")
        print(r.text[:300])
        return

    matches = data.get("matches", [])
    if not matches:
        print("[!] No results found")
        return

    for m in matches:
        ip = m.get("ip_str", "N/A")
        port = m.get("port", "N/A")
        org = m.get("org", "N/A")
        print(f"[+] {ip}:{port} | {org}")


import requests

import requests
import time

def wayback_urls():
    domain = input("Enter domain (example.com): ").strip()
    if not domain:
        print("[-] Empty domain")
        return

    if not in_scope(domain):
        print("[-] Outside allowed scope")
        return

    print("[*] Fetching URLs from Wayback Machine...\n")

    base_url = "http://web.archive.org/cdx/search/cdx"  # HTTP is more stable
    params = {
        "url": f"{domain}/*",
        "output": "json",
        "fl": "original",
        "collapse": "urlkey",
        "limit": 500          # 🔴 LIMIT results to avoid timeout
    }

    attempts = 3
    for attempt in range(1, attempts + 1):
        try:
            r = requests.get(base_url, params=params, timeout=10)

            if r.status_code != 200:
                print(f"[-] Wayback HTTP error: {r.status_code}")
                return

            if not r.text.strip().startswith("["):
                print("[-] Wayback returned non-JSON response")
                return

            data = r.json()
            break  # ✅ success

        except requests.exceptions.ReadTimeout:
            print(f"[!] Timeout (attempt {attempt}/{attempts})")
            time.sleep(2)

        except requests.exceptions.RequestException as e:
            print("[-] Network error:", e)
            return
    else:
        print("[-] Wayback unreachable after retries")
        return

    if len(data) <= 1:
        print("[!] No archived URLs found")
        return

    urls = set()
    for entry in data[1:]:
        if isinstance(entry, list) and entry:
            urls.add(entry[0])

    if not urls:
        print("[!] No usable URLs extracted")
        return

    for u in sorted(urls):
        print("[+] ", u)

    print(f"\n[✓] Total unique URLs found: {len(urls)}")


def subdomain_enum():
    domain = input("Domain: ")
    if not in_scope(domain):
        print("[-] Outside scope")
        return

    r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
    subs = set()
    for e in r.json():
        for s in e.get("name_value", "").split("\n"):
            subs.add(s.strip())
    for s in sorted(subs):
        print("[+] ", s)

# =========================
# OSINT MENU
# =========================
def osint_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(OSINT_BANNER)
        print("[1] Google Dork")
        print("[2] Github search")
        print("[3] Shodan Recon")
        print("[4] Wayback URLs")
        print("[5] Subdomain Enumeration")
        print("[6] Set Scope")
        print("[0] Back")

        c = input("> ")

        if c == "1": google_dork()
        elif c == "2": github_code_search()
        elif c == "3": shodan_recon()
        elif c == "4": wayback_urls()
        elif c == "5": subdomain_enum()
        elif c == "6": set_scope()
        elif c == "0": break
        else: print("Invalid")

        input("\nPress ENTER...")

# =========================
# MAIN MENU
# =========================
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(MAIN_BANNER)
        print("[1] OSINT")
        print("[0] EXIT")

        choice = input("> ")

        if choice == "1":
            osint_menu()
        elif choice == "0":
            sys.exit()
        else:
            print("Invalid")
            time.sleep(1)

# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    main()
