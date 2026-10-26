import json
import pandas as pd
import requests

EXCEL_URL = "https://zsmutenickacz-my.sharepoint.com/:x:/g/personal/danhelm_zsmutenicka_cz/IQABvTy5zcGXQ58S7iuLxd7OAawg5I-KJEhuoLC4raj2Hac?download=1"

response = requests.get(EXCEL_URL)
response.raise_for_status()

with open("temp.xlsx", "wb") as f:
    f.write(response.content)

df = pd.read_excel("temp.xlsx")

items = []

for _, row in df.iterrows():

    items.append({
        "name": str(row.get("Jméno", "")),
        "model": str(row.get("Vlož odkaz na model", "")),
        "color": str(row.get("Jakou barvou chceš model vytisknout?", "")),
        "notes": str(row.get("Něco dalšího co bych měl vědět?", "")),
        "delivery": str(row.get("komu mám model doručit?", "")),
    })

with open(
    "data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        items,
        f,
        ensure_ascii=False,
        indent=2
    )
