# リンクを収集する


## リンク一覧から読み込む。相対アドレスを生成
相対アドレスのままでリンクを収集するプログラムに変更することはできます。相対リンクは、ベースとなるURLを基にして完全なURLに変換する必要がありますが、今回は相対アドレスのままで保持するようにプログラムを調整します。

以下のコードでは、相対URLをそのまま保持し、ファイルに保存します。

### 修正したPythonコード：

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# URLリストが保存されているファイル（例: urls.txt）
url_file = 'urls.txt'

# 出力先ファイル（リンク一覧を保存する）
output_file = 'links_relative.txt'

# URLリストを読み込み
with open(url_file, 'r') as f:
    urls = f.readlines()

# リンクを格納するリスト
all_links = []

# 各URLに対してリンクを抽出
for url in urls:
    url = url.strip()  # URLの前後の空白を削除
    try:
        # サイトのHTMLを取得
        response = requests.get(url)
        response.raise_for_status()  # 応答が成功したか確認
        soup = BeautifulSoup(response.text, 'html.parser')

        # ページ内のすべてのリンクを抽出
        links = soup.find_all('a', href=True)

        # リンクを収集（相対URLのままで）
        for link in links:
            href = link['href']
            # 相対URLをそのまま保持
            if not href.startswith(('http', 'https', 'ftp')):  # 絶対URLでない場合は相対URL
                all_links.append(href)
            else:
                # 絶対URLはそのまま
                all_links.append(href)

    except requests.exceptions.RequestException as e:
        print(f"Error with URL {url}: {e}")

# 重複を排除して整理
unique_links = list(set(all_links))

# リンクをファイルに書き出す
with open(output_file, 'w') as f:
    for link in unique_links:
        f.write(link + '\n')

print(f"相対アドレスのリストが {output_file} に保存されました。")
```

### 説明:
- **相対URLの処理**  
   相対URL（例: `/page2`）をそのまま保持するために、`href`が`http`や`https`、`ftp`で始まらない場合は、そのままリストに追加します。
   
- **絶対URLは変換しない**  
   もし絶対URLが必要な場合は、`urljoin()`を使って絶対URLに変換することもできますが、このコードでは相対URLのまま保存します。

- **出力ファイル**  
   結果として、`links_relative.txt`ファイルに相対URLが保存されます。

### URLリスト（`urls.txt`）の例:
```
https://mathpedia.example.com/page1
https://mathpedia.example.com/page2
https://mathpedia.example.com/page3
```

### 出力ファイル（`links_relative.txt`）:
- 相対URL（例: `/page2`）や絶対URLが一行ずつ記録されます。

この方法で、相対リンクをそのままファイルに保存することができます。もし他に調整が必要であれば、お知らせください！

---
---

## １つのアドレスを直接指定
そのような作業を行うには、プログラム的にウェブサイトをスクレイピングして、ページ内のリンクを抽出し、それらを一つのファイルにまとめるという方法が考えられます。

具体的には、Pythonの`requests`や`BeautifulSoup`ライブラリを使ってウェブサイトのリンクを抽出し、その結果をファイル（例えばテキストファイルやCSVファイル）に書き出すことができます。

### 簡単な流れ:
1. **サイトのHTMLを取得**  
   Pythonを使って、サイトのHTMLを取得します。
   
2. **リンクの抽出**  
   `BeautifulSoup`を使って、HTML内のリンク（`<a>`タグ）を抽出します。

3. **リンクのリスト化**  
   抽出したリンクをリストにまとめ、重複を避けるために整理します。

4. **ファイルに書き出す**  
   リストにまとめたリンクをテキストファイルやCSVファイルとして保存します。

以下は、Pythonコードの一例です。

```python
import requests
from bs4 import BeautifulSoup

# スクレイピングするサイトのURL
url = 'https://mathpedia.example.com'  # ここに実際のURLを入れる

# サイトのHTMLを取得
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# ページ内のすべてのリンクを抽出
links = soup.find_all('a', href=True)

# リンクのリストを作成
link_list = []
for link in links:
    href = link['href']
    # 絶対URLに変換
    if not href.startswith('http'):
        href = url + href
    link_list.append(href)

# 重複を排除して整理
unique_links = list(set(link_list))

# ファイルに書き出す
with open('links.txt', 'w') as f:
    for link in unique_links:
        f.write(link + '\n')

print("リンクのリストが links.txt に保存されました。")
```

### 説明:
- `requests.get(url)`で指定したURLのHTMLを取得します。
- `BeautifulSoup`でそのHTMLを解析し、全ての`<a>`タグから`href`属性（リンク）を抽出します。
- 重複するリンクを削除し、ファイルに書き込みます。

これにより、指定したサイトからリンク一覧を収集し、1つのテキストファイルに保存することができます。

### 注意点:
- サイトによっては、スクレイピングが禁止されている場合があるので、利用規約を確認することが大切です。
- サイト構造やリンクの取り扱いが異なる場合は、コードを適宜調整する必要があります。

もし具体的なURLを教えていただければ、より詳細なサポートができます！

---
---

## リンク一覧から読み込む。絶対アドレスを生成
はい、URLのリストから読み込んで、各URLに対してリンクを収集するようにコードを変更できます。

以下のコードは、URLのリストを指定して、各ページのリンクを取得し、最終的にすべてのリンクを一つのファイルにまとめる方法です。

### 実装方法:

1. **URLリストを読み込む**  
   URLリストをテキストファイルに保存しておき、それを読み込んで処理します。
   
2. **各URLからリンクを抽出**  
   各URLに対してリンクを抽出し、それらをまとめます。

3. **結果を一つのファイルに保存**  
   収集したリンクを重複を排除して、1つのファイルに書き出します。

以下に、コードの例を示します。

### Pythonコード:

```python
import requests
from bs4 import BeautifulSoup

# URLリストが保存されているファイル（例: urls.txt）
url_file = 'urls.txt'

# 出力先ファイル（リンク一覧を保存する）
output_file = 'links.txt'

# URLリストを読み込み
with open(url_file, 'r') as f:
    urls = f.readlines()

# リンクを格納するリスト
all_links = []

# 各URLに対してリンクを抽出
for url in urls:
    url = url.strip()  # URLの前後の空白を削除
    try:
        # サイトのHTMLを取得
        response = requests.get(url)
        response.raise_for_status()  # 応答が成功したか確認
        soup = BeautifulSoup(response.text, 'html.parser')

        # ページ内のすべてのリンクを抽出
        links = soup.find_all('a', href=True)

        # リンクを収集
        for link in links:
            href = link['href']
            # 絶対URLに変換
            if not href.startswith('http'):
                href = url + href
            all_links.append(href)

    except requests.exceptions.RequestException as e:
        print(f"Error with URL {url}: {e}")

# 重複を排除して整理
unique_links = list(set(all_links))

# リンクをファイルに書き出す
with open(output_file, 'w') as f:
    for link in unique_links:
        f.write(link + '\n')

print(f"リンクのリストが {output_file} に保存されました。")
```

### 説明:
1. **URLリストの読み込み**  
   `urls.txt`というファイルにURLを一行ずつ書いておき、それを`with open(url_file, 'r')`で読み込みます。
   
2. **各URLからリンクを取得**  
   各URLに対して、`requests.get(url)`でHTMLを取得し、`BeautifulSoup`を使ってリンク（`<a>`タグ）を抽出します。

3. **リンクを整理**  
   重複を排除するために、`set()`を使ってリンクを整理し、その後ファイル（`links.txt`）に書き出します。

### URLリスト（`urls.txt`）の例:
```
https://mathpedia.example.com/page1
https://mathpedia.example.com/page2
https://mathpedia.example.com/page3
```

### 出力ファイル（`links.txt`）:
- 各URLから収集したリンクが一行ずつ書き込まれます。

これで、指定したURLリストからリンクを一括で収集してファイルに保存することができます。

もしさらにカスタマイズが必要であれば、コードを調整して対応できます！

---
---