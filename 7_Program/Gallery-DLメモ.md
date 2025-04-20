# gallery dlのインストール

`gallery-dl` は、Python パッケージとしてもインストールできるツールです。Python の環境があれば、簡単にインストールして使用することができます。

以下の手順でインストールできます：

### 1. `gallery-dl` のインストール

Python と `pip` がインストールされている前提で、次のコマンドを実行します：

```bash
pip install gallery-dl
```

これで、`gallery-dl` がインストールされます。

### 2. インストール確認

インストールが完了したら、以下のコマンドで動作確認ができます：

```bash
gallery-dl --version
```

バージョン情報が表示されれば、正常にインストールされています。

### 3. 使用方法

インストール後は、コマンドラインで `gallery-dl` を使って、画像や動画をダウンロードできます。例えば、以下のように DeviantArt のページを指定してダウンロードできます：

```bash
gallery-dl https://www.deviantart.com/username/art/some-art-id
```

Python として使う場合、Python スクリプトからも `gallery-dl` を呼び出すことができます。

```python
import gallery_dl

# ダウンロードするURL
url = 'https://www.deviantart.com/username/art/some-art-id'

# gallery-dlでURLをダウンロード
gallery_dl.download(url)
```

これで Python でも動作するようになります！

<br>

---
---

<br>

# Gallery-DLの使い方

## powershellでリストから読み込み実行

```powerhsell
$G=get-content list.txt

foreach($k in $G){
    gallery-dl $k
    Write-Host "ok!"
}
```

<br>

---
---

<br>

# Megaのアドレス一覧を自動ダウンロード

`gallery-dl` は **MEGA** にも対応していて、**複数のMEGAリンクを自動でダウンロード**することができます。

以下にやり方をまとめるね。

---

## 【やりたいこと】  
MEGAのURL一覧（たとえば `.txt` に保存）から、gallery-dl を使って自動でダウンロードしたい。

---

## 【手順まとめ】

### 1. URL一覧ファイルを用意（例：`mega_links.txt`）

中身はこんな感じでOK：

```
https://mega.nz/file/xxxx#key
https://mega.nz/file/yyyy#key
https://mega.nz/file/zzzz#key
```

---

### 2. gallery-dl を使って一括ダウンロード

以下のように実行すれば、すべてのリンクが自動で処理されます：

```bash
gallery-dl -i mega_links.txt
```

※ `-i` は「input file（URLのリスト）」を意味します。

---

### 3. （任意）`config.json` を使って設定をカスタマイズ

たとえば保存先やファイル名を変えたい場合は、`config.json` に書いておくと便利。

```json
{
    "extractor": {
        "mega": {
            "overwrite": false  // 既存ファイルを上書きしない
        }
    },
    "output": {
        "directory": ["downloads", "mega"]  // 保存フォルダ
    }
}
```

---

## 【注意点】

- MEGAは**大容量ファイルのダウンロードに制限**がある場合あり（特に非ログイン時）。
- gallery-dl は基本的に **個別ファイルURL** に対応。MEGAフォルダ全体のURLにはうまくいかないこともある。

---

## 【まとめ】

- MEGAのリンク一覧を `.txt` にして `gallery-dl -i` で一括処理できる。
- `config.json` を使えば柔軟なカスタマイズが可能。
- MEGAの制限（無料ユーザーの帯域）に注意！

<br>

---
---

<br>

# Deviant artからのダウンロードにも対応
**`gallery-dl` は DeviantArt にもバッチリ対応**してるよ！

イラストや画像を**フル解像度で自動ダウンロード**できるし、  
ログインしていれば **年齢制限付きの作品（NSFW）** も取得可能！

---

## 【基本的な使い方】

特定の DeviantArt 投稿をダウンロードしたい場合：

```bash
gallery-dl https://www.deviantart.com/username/art/title-id
```

ユーザーページの **すべての投稿**をダウンロードするには：

```bash
gallery-dl https://www.deviantart.com/username/gallery
```

---

## 【ログインが必要な場合】

Pixivと同じく、DeviantArtもログインしないと見れない作品があるから、  
cookie を使って gallery-dl にログイン状態を渡すのがオススメ。

### 方法1：cookieをブラウザからコピーして使う

1. ブラウザで DeviantArt にログイン
2. 開発者ツールで `cookie` をコピー（`deviantart.com` のもの）
3. `config.json` に以下のように設定：

```json
{
    "extractor": {
        "deviantart": {
            "cookies": {
                "auth": "ここにコピーしたcookieの値"
            }
        }
    }
}
```

---

## 【カスタマイズ例：config.json】

```json
{
    "extractor": {
        "deviantart": {
            "filename": "{title} - {author}.{extension}",
            "folders": true
        }
    },
    "output": {
        "directory": ["DeviantArt", "{author}"]
    }
}
```

→ `DeviantArt/作者名/タイトル - 作者.jpg` みたいな構成で保存される。

---

## 【注意点】

- DeviantArt 側が仕様変更すると動かなくなることもあるけど、`gallery-dl` は割と更新されてる。
- 動作しない時は `gallery-dl` を最新版にするか、GitHubの issue をチェック！

---

## zipファイルがアップロードされてるdeviant artのダウンロード

DeviantArt にアップされている **ZIPファイルなどの添付ファイル（Download ボタン付き）** も、`gallery-dl` は基本的に **対応しています**！

---

## 【前提】  
- DeviantArt では、イラストの「フルサイズ画像」ではなく、ZIP などの**ダウンロード用ファイル**を作者が添付できる。
- これはページに「Download」ボタンがあるタイプ。

---

## 【gallery-dl はそれを取得できる？】

→ **Yes！** `gallery-dl` は **Download ボタンがある投稿では、ZIPなどの添付ファイルを自動でダウンロード**してくれます。

---

## 【実際の使い方】

たとえばこのような投稿：

```
https://www.deviantart.com/username/art/some-pack-123456789
```

に対して以下を実行するだけでOK：

```bash
gallery-dl https://www.deviantart.com/username/art/some-pack-123456789
```

→ ZIPファイルがあれば、それをそのままダウンロードしてくれる。

---

## 【注意点】

1. **Download ボタンがない作品**は ZIP も存在しない（gallery-dl は何も落とさない）。
2. **ログイン必須の作品（年齢制限等）**は、先ほどのように Cookie 設定が必要。
3. ZIPではなく画像がメインの場合は、画像のみ取得される。

---

## 【おすすめ設定：ZIPも画像も整理したいとき】

```json
{
    "extractor": {
        "deviantart": {
            "filename": "{title} - {author}.{extension}",
            "folders": true
        }
    },
    "output": {
        "directory": ["DeviantArt", "{author}", "{title}"]
    }
}
```

これで「作品ごとにフォルダが分かれて、ZIP や画像がそこに入る」形式になる。

---
---
