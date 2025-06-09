import requests
import json

# 将来婚姻件数のデータをe-Stat APIから取得するプログラム
# 統計表ID: 0003411954（厚生労働省 人口動態調査）
# データは年別、単位は「件」

APP_ID = "2907a934e9805e009cebb3828953ed505fd943d3"

params = {
    "appId": APP_ID,
    "statsDataId": "0003411954",
    "lang": "J",
    "metaGetFlg": "N",
    "cntGetFlg": "N",
    "explanationGetFlg": "N",
    "sectionHeaderFlg": "1"
}

# APIからデータ取得
response = requests.get("https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData", params=params)

# JSONに変換
data = response.json()

# 一部データの表示（最初の10件）
print("\n【取得結果の一部を表示】")
try:
    values = data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
    for v in values[:10]:
        print(f'年月: {v["@time"]}, 単位: {v["@unit"]}, 値: {v["$"]}')
except KeyError:
    print("データ取得に失敗しました。")
