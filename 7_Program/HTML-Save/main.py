# 外部urlリストから、各urlのhtmlテキストデータを保存していく！
# エラーが出たら、そのアドレスを別ファイルに書きだす！

import requests
from bs4 import BeautifulSoup
import re

# 📌 URLリストを外部ファイルから読み込み
with open("urls.txt", "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file.readlines() if line.strip()]

# 🔧 保存できない文字を除外する関数
def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

# 📌 失敗したURLを記録するリスト
failed_urls = []

# 🎯 各URLにアクセスしてHTMLデータを取得＆保存
for i, url in enumerate(urls):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # 🛠️ HTMLを解析
        soup = BeautifulSoup(response.content, "html.parser")
        html_content = soup.prettify()

        # 🌟 ページタイトルを取得してファイル名にする
        title = soup.title.string.strip() if soup.title else f"page_{i+1}"
        safe_title = clean_filename(title)

        # 💾 ファイル保存
        with open(f"{safe_title}.html", "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"✅ {url} の保存成功！ → {safe_title}.html")

    except Exception as e:
        # 失敗したURLをリストに追加
        print(f"⚠️ {url} の保存失敗: {e}")
        failed_urls.append(url)

# 📌 失敗したURLをファイルに書き出し
if failed_urls:
    with open("failed_urls.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(failed_urls))
    print("⚠️ 失敗したURLを failed_urls.txt に保存しました！")

print("🎉 完了！")
