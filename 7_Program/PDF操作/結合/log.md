# カレントディレクトリにある全pdfを結合するプログラム
良い質問です！
Python を使って、**カレントディレクトリ内にあるすべての PDF ファイルを結合**する方法は以下のとおりです。

---

## ✅ 必要なライブラリ

```bash
pip install pypdf
```

---

## ✅ コード例（全PDFファイルを結合）

```python
import os
from pypdf import PdfReader, PdfWriter

# カレントディレクトリのPDFファイルを取得（.pdfで終わるファイルのみ）
pdf_files = [f for f in os.listdir() if f.lower().endswith('.pdf')]
pdf_files.sort()  # アルファベット順に並べ替え（必要に応じて変更）

writer = PdfWriter()

# 各PDFを読み込み、すべてのページを追加
for pdf_file in pdf_files:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

# 結合後のファイルを書き出し
with open("merged_output.pdf", "wb") as f:
    writer.write(f)

print("PDF結合が完了しました: merged_output.pdf")
```

---

## 🧠 ポイント

* `os.listdir()` でカレントディレクトリ内のファイル一覧を取得
* 拡張子が `.pdf`（大小区別なし）だけを対象にしています
* `pdf_files.sort()` でファイル名順に並べています（並び順を変更したければ自分で調整可）

---

## 📝 補足

* 特定の順番で結合したい場合（例：数字順や日付順など）、`sort()` にカスタムキーを使えます
* パスワード付きPDFや破損ファイルがあるとエラーになるので、そういうケースがあれば追加の処理が必要です

---

必要に応じてファイル名の順序を変えたり、特定のファイルを除外したい場合もアドバイスできます！

---
---


# pdf結合プログラムの修正版

ありがとうございます！エラーメッセージ、完璧です。
内容を見ると：

---

## ❌ エラーの原因：

あなたの環境の `pypdf` は **バージョン5.0.0以降** であり、
そのバージョンでは **`PdfMerger` は廃止（削除）** されています。

```
DeprecationError: PdfMerger is deprecated and was removed in pypdf 5.0.0. Use PdfWriter instead.
```

---

## ✅ 対処方法

### ▶ 方法1：**推奨** — `PdfWriter` を使って結合する

最新版の `pypdf` では、`PdfWriter` を使って PDF を結合する必要があります。

### ✅ 修正版コード：

```python
from pypdf import PdfReader, PdfWriter

writer = PdfWriter()

for pdf in ['file1.pdf', 'file2.pdf']:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

with open("merged_output.pdf", "wb") as f:
    writer.write(f)
```

---

### ▶ 方法2：古い `pypdf` バージョンに戻す（**非推奨**）

どうしても `PdfMerger` を使いたい場合は、`pypdf` の旧バージョン（例：4.0.1）にダウングレード可能です：

```bash
pip install pypdf==4.0.1
```

ただし、**新しい機能やバグ修正が使えなくなるので非推奨**です。

---

## ✅ 結論：今後は `PdfWriter` を使いましょう！

この方式の方が最新版に対応しており、今後も安心して使えます。

もし結合元PDFにパスワードがかかっていたり、表紙を挿入したいなどの要望があれば、それも対応できますよ！

---
---

