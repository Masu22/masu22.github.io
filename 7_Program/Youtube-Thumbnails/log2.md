# サムネイル画像のダウンロード
## サムネイル画像アドレス一覧をurls.txtに保存しておく
## downloaded_imagesフォルダを作成して、そこにダウンロード！

完璧です！では、`.txt`ファイルから画像URLを読み込むようにコードを調整します。

---

### 📝 `urls.txt` の例
```txt
https://example.com/image1.jpg
https://example.com/image2.jpg
https://example.com/image1.jpg
```

---

### 🐍 修正後のPythonコード（`.txt`からURLを読み込む）

```python
import os
import requests
from urllib.parse import urlparse

# URLを記載したテキストファイルのパス
url_file = 'urls.txt'

# 保存先ディレクトリ
save_dir = 'downloaded_images'
os.makedirs(save_dir, exist_ok=True)

# 同じ名前のファイルがある場合、番号を追加して保存
def get_unique_filename(directory, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

# URLリストを読み込み
with open(url_file, 'r', encoding='utf-8') as f:
    image_urls = [line.strip() for line in f if line.strip()]

# ダウンロード処理
for url in image_urls:
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        parsed_url = urlparse(url)
        original_filename = os.path.basename(parsed_url.path)

        # 重複しないファイル名
        unique_filename = get_unique_filename(save_dir, original_filename)

        # 保存
        filepath = os.path.join(save_dir, unique_filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Saved: {filepath}")
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
```

---

このコードで、`urls.txt` のURLすべてにアクセスして、画像を安全に保存できます！

`.txt`のファイル名や場所を変える場合は、`url_file` のパスを調整してくださいね。

試してみます？
