from pathlib import Path
import json

def update_money(money):                    # Updates the money
    path = Path("money.json")
    content = json.dumps(money)
    path.write_text(content)

def extract_money():                        # Extracts the money
    path = Path("money.json")
    text = path.read_text()
    content = json.loads(text)
    return content

def update_deals(deals):                    # Updates the deals
    path = Path("deals.json")
    content = json.dumps(deals)
    path.write_text(content)

def extract_deals():                        # Extracts the deals
    path = Path("deals.json")
    return json.loads(path.read_text)