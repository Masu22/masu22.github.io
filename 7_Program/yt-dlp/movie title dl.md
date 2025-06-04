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
