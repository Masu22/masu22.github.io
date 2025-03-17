# アドレス一覧から、htmlのテキストデータのみを保存!
それなら、Pythonを使えば割と簡単にできますよ！やりたいことをまとめると、例えばこんな感じでしょうか？  

1. **アドレス一覧（URLのリスト）を読み込む**  
2. **各URLにアクセスしてHTMLデータを取得する**  
3. **HTMLデータをファイルとして保存する（URLごとに分けるか、1つのファイルにまとめるかも選べる）**  

以下のコード例を考えてみました👇  

### 🎯 **Python + BeautifulSoup でHTML保存プログラム**
```python
import requests
from bs4 import BeautifulSoup

# URLリストを用意
urls = [
    "https://example.com",
    "https://example.org",
]

# 各URLにアクセスしてHTMLデータを取得＆保存
for i, url in enumerate(urls):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # HTMLを解析してきれいに整形
        soup = BeautifulSoup(response.content, "html.parser")
        html_content = soup.prettify()

        # ファイルに保存（番号つけて区別）
        with open(f"page_{i+1}.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        
        print(f"✅ {url} の保存成功！")

    except Exception as e:
        print(f"⚠️ {url} の保存失敗: {e}")

```

---

### 🔥 **ポイント解説**

1. `requests` でURLにアクセスしてHTMLを取得します。
2. `BeautifulSoup` でHTMLを整形して見やすくします。
3. `with open()` で各ページを別ファイルとして保存します。（`page_1.html` みたいな感じ）

---

### 🛠️ **さらに改良するなら…**

- **リストを外部ファイル（CSVやTXT）から読み込む**  
- **特定のタグ（タイトルや本文だけなど）を抜き出す**  
- **エラー処理や再試行機能を追加する**  
- **進行状況を表示するプログレスバー（`tqdm`ライブラリなど）**  

---

✨ **他にもScrapyみたいな専用のスクレイピングフレームワークもあります**が、この規模ならPythonの標準ライブラリ＋αで十分やれそうです！

どうでしょう、やりたいイメージに近そうですか？  
もっと簡単にしたい・逆に凝りたいなどあれば、そっちも調整しますよ💪✨

---
---

# 外部ファイルから読み取りたい！
なるほど！じゃあURLのリストを外部ファイルから読み込むバージョンを作りましょう✨

例えば、`urls.txt` というファイルを作って、こんな感じでURLを1行ずつ書いておくとします👇
```
https://example.com
https://example.org
https://example.net
```

---

### 🎯 **改良版：外部ファイルからURLリストを読み込む**
```python
import requests
from bs4 import BeautifulSoup

# 📂 外部ファイル (urls.txt) からURLを読み込む
with open("urls.txt", "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file.readlines() if line.strip()]

# 🎯 各URLにアクセスしてHTMLデータを取得＆保存
for i, url in enumerate(urls):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # 🔧 HTMLを解析＆整形
        soup = BeautifulSoup(response.content, "html.parser")
        html_content = soup.prettify()

        # 💾 URLごとに保存 (ファイル名をURLのドメインにする)
        domain = url.split("//")[-1].replace("/", "_").replace(":", "_")
        with open(f"{domain}.html", "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"✅ {url} の保存成功！")

    except Exception as e:
        print(f"⚠️ {url} の保存失敗: {e}")
```

---

### 🔥 **ポイント解説**

1. **`with open()`** で `urls.txt` からURLリストを読み込みます。
   - `strip()` で余分な空白や改行を取り除きます。
   - 空白行があってもスキップできるように `if line.strip()` を追加しました。

2. **ファイル名をURLベースで作成**  
   URLそのままだとファイル名にできないので、`/` や `:` を `_` に置き換えています。  
   例: `https://example.com/page` → `example.com_page.html`

3. **エラー処理も強化**  
   - URLが無効なときや、ページが取得できなかった場合も止まらずに次のURLに進みます。

---

### 🛠️ **さらに強化できるアイデア**

- **ページタイトルをファイル名にする**  
   `soup.title.string` でページタイトルを取り出してファイル名にするのも面白いかも！
   
- **保存形式をTXTやMarkdownにも変更可能**  
   HTMLだけじゃなく、本文だけ抜き出してテキスト保存もできます。

- **途中で止まっても再開できるように改良**  
   成功したURLを別ファイルに記録して、次回はそこから続きができる仕組みもアリですね✨

---

これなら外部ファイルを編集するだけでURLを自由に増やせるので、かなり楽になると思います💪  
他にも「特定のタグだけ抜き出したい」や「保存形式を変えたい」とかあれば、そこも組み込みますよ〜！

---
---

# さらに改良
了解です！じゃあ次の改良ポイントを全部盛り込みましょう💪✨

✅ **外部ファイルからURLリストを読み込む**  
✅ **成功したページはタイトルを使って保存（使えない文字を削除して安全なファイル名に変換）**  
✅ **失敗したURLは `failed_urls.txt` に書き出して記録**  

---

### 🎯 **完全版：改良プログラム**
```python
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
```

---

### 🔥 **ポイント解説**

1. **`clean_filename()`**  
   WindowsでもMacでも安全なファイル名にするために、`\ / * ? : " < > |` みたいな使えない文字を正規表現で削除します。  

2. **ページタイトルをファイル名に使う**  
   `soup.title.string` でタイトルを取得し、なかった場合は `page_1.html` のように番号で保存します。

3. **失敗したURLを記録する**  
   失敗したURLをリストに貯めて、最後に `failed_urls.txt` へ保存します。  
   次回 `urls.txt` を直す必要がないので、再チャレンジも楽チン🎉  

---

### 🎁 **さらに改良するなら…**

- **再試行機能を追加** → 何度かリトライできるようにしてもいいですね！
- **レスポンスのサイズ制限を追加** → 極端に大きいページをスキップする処理を加えるのもアリ。
- **特定のタグだけ抜き出し保存** → たとえば本文だけ `soup.find("article")` みたいにすれば記事抽出も可能です。

---

これなら、  
✅ **URL管理も簡単**  
✅ **ファイル名もきれい**  
✅ **失敗してもログを残してリカバリーしやすい**  
という"実用レベル"なプログラムになったはずです！ 🚀✨  

どうでしょう、イメージ通りになりそうですか？

---
---
