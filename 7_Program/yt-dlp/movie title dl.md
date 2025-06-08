# youtubeのあるアカウントの動画のタイトル一覧を作る

OK！`yt-dlp`で取得したYouTubeチャンネルの動画タイトル一覧を、**テキストファイル（.txt）に書き出すPythonコード**を紹介します✨

---

## ✅ 完全版コード：タイトル一覧をテキストファイルに保存

```python
import yt_dlp

# チャンネルのURL（@ユーザー名 or channel/ID どちらでもOK）
channel_url = 'https://www.youtube.com/@YourChannelName'

# 出力ファイル名
output_file = 'video_titles.txt'

# yt-dlp オプション設定
ydl_opts = {
    'extract_flat': True,  # 動画をダウンロードせず情報だけ取得
    'quiet': True,         # ログを抑制
    'force_generic_extractor': True
}

# タイトル取得とファイル書き出し
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(channel_url, download=False)

    entries = info.get('entries', [])
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"動画一覧（{info.get('title', 'チャンネル名不明')}）\n")
        f.write("="*30 + "\n")
        for i, entry in enumerate(entries, 1):
            f.write(f"{i}. {entry['title']}\n")

print(f"✅ タイトル一覧を '{output_file}' に保存しました！")
```

---

## 📄 出力されるファイルの例（video\_titles.txt）

```
動画一覧（MyCoolChannel）
==============================
1. はじめての投稿！
2. Pythonで自動化してみた
3. AIにイラストを描かせてみた
...
```

---

## 🛠 カスタマイズ例（必要なら）

* `f.write(f"{i}. {entry['title']} - {entry['url']}\n")` → タイトル＋URLも出力
* `.txt` を `.csv` に変えたい場合 → `csv` モジュールで保存可能

---

## 🚀 補足：ファイルの保存場所

* ファイルは**スクリプトを実行した場所と同じディレクトリ**に `video_titles.txt` という名前で保存されます。
* パスを指定すれば好きな場所にも保存できます：

```python
output_file = 'C:/Users/あなたの名前/Documents/video_titles.txt'
```

---

もっとカスタムしたい？（再生数も一緒に出したい、特定の単語だけ抽出したいなど）そういうのも対応できます！

---
---

# 再生リストから動画タイトルを取得する

`yt-dlp`（YouTubeのダウンロードツール）を使っても、YouTubeの再生リストから動画タイトルを簡単に取得することができます。`yt-dlp`は、YouTubeやその他のサイトからメタデータ（タイトル、説明、再生リストなど）を取得するための強力なツールです。

### yt-dlpを使って再生リストから動画タイトル一覧を取得する方法

以下の手順で、`yt-dlp`を使用して動画タイトルの一覧を取得できます。

1. **yt-dlpのインストール**

   まず、`yt-dlp`がインストールされていない場合は、以下のコマンドでインストールします。

   ```bash
   pip install yt-dlp
   ```

2. **再生リストから動画タイトルを取得するコマンド**

   `yt-dlp`を使って再生リストの動画タイトルを一覧で取得するには、`--get-title`オプションを使います。例えば、以下のコマンドをターミナルやコマンドプロンプトで実行します。

   ```bash
   yt-dlp --get-title "https://www.youtube.com/playlist?list=PLFeEvEPtX_0S6vxxiiNPrJbLu9aK1UVC_"
   ```

   このコマンドを実行すると、再生リスト内の全ての動画タイトルがリスト形式で表示されます。

### 例

```bash
$ yt-dlp --get-title "https://www.youtube.com/playlist?list=PLFeEvEPtX_0S6vxxiiNPrJbLu9aK1UVC_"
タイトル1
タイトル2
タイトル3
...
```

### 詳細な情報も取得したい場合

もし、さらに詳細な情報（動画ID、再生回数など）も含めて取得したい場合は、`-j`オプションを使用してJSON形式でメタデータを取得することができます。これにより、動画の他の情報も含まれたJSONデータを出力することができます。

```bash
yt-dlp -j "https://www.youtube.com/playlist?list=PLFeEvEPtX_0S6vxxiiNPrJbLu9aK1UVC_"
```

### 出力例（JSON）

```json
{
  "id": "動画ID1",
  "title": "動画タイトル1",
  "url": "https://www.youtube.com/watch?v=動画ID1",
  ...
}
```

JSON形式で出力されたデータから、必要な情報（例えばタイトル）を抽出することもできます。

---

これで、`yt-dlp`を使ってYouTubeの再生リストから動画タイトルを簡単に取得できます！他に質問があれば、気軽に聞いてくださいね。

---

## テキスト形式での出力

`yt-dlp`で動画のメタデータやタイトルなどを**テキスト形式で出力**するには、以下のオプションを使用できます。

### 1. **`--get-title`でタイトルのみを出力**

もし動画のタイトルだけをテキスト形式で出力したい場合、以下のコマンドを使います。

```bash
yt-dlp --get-title "動画URL" > output.txt
```

このコマンドは、指定した動画または再生リストの**動画タイトル**を`output.txt`というファイルに保存します。

### 2. **`--get-id`で動画IDのみを出力**

動画のIDのみをテキストファイルに保存したい場合は、次のようにします。

```bash
yt-dlp --get-id "動画URL" > output.txt
```

これで、動画IDだけが`output.txt`に保存されます。

### 3. **`-j`オプションでJSONデータを出力し、それをテキスト形式に変換**

`yt-dlp`のメタデータを**JSON形式**で出力する場合、次のコマンドを使います。

```bash
yt-dlp -j "動画URL" > output.json
```

このコマンドでは、動画の詳細な情報（タイトル、ID、URLなど）がJSON形式で`output.json`に保存されます。

もしJSONをテキスト形式に変換したい場合は、JSONデータを解析して特定の情報（例えばタイトルのみ）を取り出して別のテキスト形式で保存することも可能です。

### 4. **`--write-info-json`で動画の情報をJSONとしてファイルに保存**

複数の動画や再生リストをダウンロードしている場合、動画ごとにJSON情報を保存したい時には`--write-info-json`オプションを使います。

```bash
yt-dlp --write-info-json "動画URL"
```

このコマンドを使うと、ダウンロードした動画の情報が`動画ID.info.json`という名前で保存されます。

### 5. **全ての動画メタデータをテキストで保存**

もし、再生リスト内のすべての動画の情報（タイトル、URL、IDなど）をテキスト形式で保存したい場合、以下のようにします。

```bash
yt-dlp --get-title "再生リストURL" > output.txt
```

また、特定の動画メタデータをカスタマイズして出力したい場合は、`--output`オプションを使って出力内容を指定することもできます。例えば：

```bash
yt-dlp -o "%(title)s.%(ext)s" "動画URL"
```

これは、ダウンロードしたファイル名をタイトルと拡張子で保存する設定です。

---

これらの方法を使えば、`yt-dlp`で必要な情報をテキスト形式で出力できます。もし他に質問があれば、遠慮なくどうぞ！

---
---

