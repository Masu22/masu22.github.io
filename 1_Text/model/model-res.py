# model resourceの各ゲームページから、モデルをダウンロードリンクを抽出
# 例としてsmiteのページを入力してる
# ダウンロードはirvineなどで実行した方がいいかな？

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 対象URL
base_url = "https://www.models-resource.com"
target_url = "https://www.models-resource.com/pc_computer/smite/"

# HTML取得
response = requests.get(target_url)
if response.status_code != 200:
    print(f"ページ取得失敗: {response.status_code}")
    exit()

# パース
soup = BeautifulSoup(response.text, 'html.parser')

# /model/ を含むリンクを抽出
model_links = []
for a_tag in soup.find_all("a", href=True):
    href = a_tag['href']
    if "/model/" in href:
        # モデル番号を抽出して、新しいURL形式に変更
        model_number = href.split('/')[4]  # /model/{番号}/の番号部分
        new_link = f"https://www.models-resource.com/download/{model_number}/"
        model_links.append(new_link)

# テキストファイルに書き込む
with open("model_links.txt", "w", encoding="utf-8") as file:
    for link in model_links:
        file.write(link + "\n")

print("結果が 'model_links.txt' に保存されました。")
