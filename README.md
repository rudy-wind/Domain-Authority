# Domain Authority Bulk Checker (DA/PA) — README

A simple Python tool to check Domain Authority (DA) and Page Authority (PA) in bulk.
Reads domains from a text file, queries the free XEO.MY.ID service, and prints a compact report for each domain.

---

## Features

* Bulk check domains listed in `domain.txt`
* Outputs DA, PA, Spam Score (SS), Backlinks (BL), MozTrust (MT), MozRank (MR) (as returned by the data source)
* Uses the free data feed from `XEO.MY.ID`
* Simple — easy to run and integrate into workflows

---

## Requirements

* Python 3.8+
* Internet connection (the script queries `XEO.MY.ID`)
* `requirements.txt` (install with pip)

Example `requirements.txt` (put this in your repo if not already present):

```
requests
tqdm
```

Install:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Add the domains you want to check to `domain.txt`, one domain per line. Examples:

```
google.com
example.org
mysite.id
```

2. Run the checker:

```bash
python main.py
```

3. Wait until all domains are checked. Output format will look like this:

```
GOOGLE.COM
DA: 94 | PA: 90 | SS: 1% | BL: 1.489.770.510 | MT: 9 | MR: 9.0
```

---

## Notes & Limitations

* **Data source:** This tool fetches authority data from `XEO.MY.ID` (free).
* **Rate limiting / timing:** The data source limits requests — each domain check is limited to **~30 seconds**. Expect the script to take roughly 30 seconds per domain (actual time can vary).
* **Accuracy:** Values are as returned by `XEO.MY.ID`. The tool does not modify or recalculate metrics.
* **Respect the source:** Use responsibly and avoid hammering the free service. If you need high-volume automated checks, consider using an official paid API or contacting the data provider.

---

## Example output (full)

```
GOOGLE.COM
DA: 94 | PA: 90 | SS: 1% | BL: 1.489.770.510 | MT: 9 | MR: 9.0

EXAMPLE.ORG
DA: 40 | PA: 35 | SS: 3% | BL: 12.345 | MT: 3 | MR: 2.1
```

---

## Troubleshooting

* If the script fails to fetch data, check your internet connection and confirm `XEO.MY.ID` is reachable.
* If you get HTTP 429 or similar rate-limit responses, slow down the requests or check the provider’s limits.
* For parsing issues, make sure domains in `domain.txt` are plain domain names (no `http://`/`https://` prefixes).
