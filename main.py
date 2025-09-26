import requests
import random
import time
from lxml import html

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/91.0.864.67",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Safari/537.36 OPR/77.0.4054.172",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/90.0.4430.93 Safari/537.36"
]

colors = [
    "\033[91m",
    "\033[92m",
    "\033[93m",
    "\033[94m",
    "\033[95m",
    "\033[96m",
    "\033[97m",
]
reset = "\033[0m"

def colorize(text):
    return random.choice(colors) + text + reset

def get_site_data(domain, attempt=1):
    url = f"https://byspass-cors.rudiwind10026.workers.dev/?url=https://xeo.my.id/checker/free/moz/?domain={domain}"
    headers = {
        "User-Agent": random.choice(user_agents)
    }

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.encoding = 'utf-8'
    except requests.RequestException as e:
        print(colorize(f"[!] Error fetching {domain}: {e}"))
        if attempt < 3:
            print(colorize(f"[~] Retrying... Attempt {attempt+1}/3"))
            time.sleep(5)
            return get_site_data(domain, attempt + 1)
        else:
            print(colorize(f"[x] Max retries reached for {domain}. Skipping."))
            return [domain, "Error", "Error", "Error", "Error"]

    tree = html.fromstring(response.text)

    if tree.xpath('//h3[contains(text(), "TUNGGU")]'):
        print(colorize(f"[!] Tunggu 30 detik lagi untuk {domain}..."))
        time.sleep(30)
        return get_site_data(domain)

    try:
        first_row = tree.xpath('(//table[@class="table"])[1]//tr[2]/td')
        da = first_row[0].text_content().strip() if len(first_row) > 0 else "Error"
        pa = first_row[1].text_content().strip() if len(first_row) > 1 else "Error"
        ss = first_row[2].xpath('.//b/text()')[0].strip() if len(first_row) > 2 and first_row[2].xpath('.//b') else "Error"
        bl = first_row[3].text_content().strip() if len(first_row) > 3 else "Error"
        mt = first_row[4].text_content().strip() if len(first_row) > 3 else "Error"
        mr = first_row[5].text_content().strip() if len(first_row) > 3 else "Error"
        return [domain, da, pa, ss, bl, mt, mr]
    except Exception as e:
        print(colorize(f"[!] Parsing error {domain}: {e}"))
        return [domain, "Error", "Error", "Error", "Error"]

with open("domain.txt", "r") as f:
    domains = [line.strip() for line in f if line.strip()]

for domain in domains:
    data = get_site_data(domain)

    result_line = (
        f"{colorize(data[0])}\n"
        f"DA: {colorize(data[1])} | "
        f"PA: {colorize(data[2])} | "
        f"SS: {colorize(data[3])} | "
        f"BL: {colorize(data[4])} | "
        f"MT: {colorize(data[5])} | "
        f"MR: {colorize(data[6])}\n\n"
    )

    print(result_line, end="")

    with open("hasil.txt", "a", encoding="utf-8") as result_file:
        result_file.write(f"{data[0]}\nDA: {data[1]} | PA: {data[2]} | SS: {data[3]} | BL: {data[4]} | MT: {data[5]} | MR: {data[6]}\n\n")

    time.sleep(30)

print(colorize("Selesai! Semua data telah disimpan di hasil.txt."))
