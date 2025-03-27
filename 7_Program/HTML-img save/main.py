import os
import csv
from bs4 import BeautifulSoup

# 対象のHTMLファイルがあるフォルダを指定
html_folder = "html_files"  # フォルダ名を適宜変更

# 結果を書き出すCSVファイル
output_file = "image_urls.csv"

# 画像URLを保存するリスト
image_data = []

# フォルダ内のすべてのHTMLファイルを処理
for filename in os.listdir(html_folder):
    if filename.endswith(".html") or filename.endswith(".htm"):
        filepath = os.path.join(html_folder, filename)
        
        # HTMLを解析
        with open(filepath, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        
        # すべての <img> タグの src 属性を取得
        for img in soup.find_all("img"):
            img_url = img.get("src")
            if img_url:  # Noneでないことを確認
                image_data.append([filename, img_url])

# 結果をCSVに書き出し
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["HTMLファイル", "画像URL"])  # ヘッダー
    writer.writerows(image_data)

print(f"処理完了！ {output_file} に書き出しました。")
