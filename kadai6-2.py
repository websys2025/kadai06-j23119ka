import requests
import xml.etree.ElementTree as ET

# --- 気象庁のオープンデータ「降灰予報（定時）」を取得して表示するプログラム ---

# ■データの種類
# 気象庁が提供する火山の降灰予報（定時）の速報情報

# ■データ提供元
# 気象庁オープンデータ：https://www.data.jma.go.jp/developer/

# ■エンドポイント
# https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml

# ■使い方
# XMLフィードから「降灰予報」が含まれる情報を抽出し、最新5件を表示する

url = "https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml"
res = requests.get(url)
root = ET.fromstring(res.content)

ns = {'atom': 'http://www.w3.org/2005/Atom'}

print("【降灰予報（先頭5件）】")
count = 0
for entry in root.findall("atom:entry", ns):
    title = entry.find("atom:title", ns).text
    if "降灰予報" in title:
        link = entry.find("atom:link", ns).attrib['href']
        updated = entry.find("atom:updated", ns).text

        print(f"タイトル: {title}")
        print(f"URL: {link}")
        print(f"日時: {updated}")
        print("-" * 40)

        count += 1
        if count >= 5:
            break
