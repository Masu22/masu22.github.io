# pdfに透かしを入れるには？

PDFに透かし（ウォーターマーク）を入れるには、使用する環境やツールによって異なります。以下に代表的な方法を紹介します。

---

### ① **Adobe Acrobatを使う場合（有料）**

1. PDFをAdobe Acrobatで開く。
2. メニューから **「ツール」→「編集」→「透かし」→「追加」** を選択。
3. テキストまたは画像の透かしを設定。
4. 表示位置、透明度、ページ範囲などを調整。
5. OKをクリックして保存。

---

### ② **無料ソフトやオンラインツールを使う**

#### 例：PDF24、iLovePDF、Sejdaなど

1. ウェブサイトにアクセス。
2. PDFファイルをアップロード。
3. 「透かしの追加」などの項目を選び、文字や画像を指定。
4. オプションを設定して、ダウンロード。

🔗 例：

* [https://www.ilovepdf.com/ja/add\_watermark](https://www.ilovepdf.com/ja/add_watermark)
* [https://tools.pdf24.org/ja/pdf-watermark](https://tools.pdf24.org/ja/pdf-watermark)

---

### ③ **無料のソフトウェアを使う（例：LibreOffice、PDFTK、Python）**

#### Python（`PyPDF2`や`reportlab`を使用）：

```python
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# 透かし用のPDFを作成
packet = BytesIO()
c = canvas.Canvas(packet, pagesize=letter)
c.setFont("Helvetica", 40)
c.setFillColorRGB(0.6, 0.6, 0.6, alpha=0.3)
c.drawString(150, 500, "CONFIDENTIAL")
c.save()

# 元PDFと合成
packet.seek(0)
watermark = PdfReader(packet)
original = PdfReader("input.pdf")
writer = PdfWriter()

for page in original.pages:
    page.merge_page(watermark.pages[0])
    writer.add_page(page)

with open("output.pdf", "wb") as f:
    writer.write(f)
```

---

### ④ **Mac の「プレビュー」アプリを使う（簡易的な方法）**

* プレビューで画像やテキストを透かし風に重ねて保存。ただし多ページPDFには向きません。

---

### 目的別おすすめ：

| 目的        | おすすめの方法                     |
| --------- | --------------------------- |
| 簡単・すぐやりたい | オンラインツール                    |
| 高度な制御がしたい | Adobe Acrobat / Python      |
| 無料かつオフライン | LibreOffice / PDF24 Creator |

---

必要であれば、あなたの環境（OS・用途・ファイルの例など）に合った具体的な手順もお手伝いできます。

---
---

# 普通のpdfを用意して、pythonで全ページに透かしを入れたい！
了解しました！Pythonで「普通のPDF」に**全ページに透かし（ウォーターマーク）を入れる**方法をご紹介します。以下の手順でできます。

---

## ✅ 必要なライブラリ

```bash
pip install PyPDF2 reportlab
```

* `PyPDF2`: PDFの読み書き用
* `reportlab`: 透かしを描画したPDFページを作成するために使用

---

## ✅ コード全体（すべてのページにテキスト透かし）

```python
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# === 1. 透かしPDFを作成 ===
def create_watermark(text):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica-Bold", 40)
    can.setFillColorRGB(0.5, 0.5, 0.5, alpha=0.3)
    can.saveState()
    can.translate(300, 400)
    can.rotate(45)
    can.drawCentredString(0, 0, text)
    can.restoreState()
    can.save()
    packet.seek(0)
    return PdfReader(packet)

# === 2. 元のPDFに透かしを適用 ===
def add_watermark_to_pdf(input_pdf_path, output_pdf_path, watermark_text):
    original_pdf = PdfReader(input_pdf_path)
    watermark_pdf = create_watermark(watermark_text)
    watermark_page = watermark_pdf.pages[0]

    writer = PdfWriter()

    for page in original_pdf.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

# === 3. 実行 ===
add_watermark_to_pdf("input.pdf", "output_with_watermark.pdf", "CONFIDENTIAL")
```

---

## ✅ 補足

* `"input.pdf"` に任意のPDFファイル名を指定してください。
* `"CONFIDENTIAL"` の部分を好きな透かしテキストに変えられます。
* `letter` を変更するとサイズも指定できます（例：`A4`）。

---

## ✅ 出力例

`output_with_watermark.pdf` という新しいPDFができて、すべてのページの中央に斜めに薄く「CONFIDENTIAL」と表示されます。

---

必要であれば「画像透かし」や「ページの隅に配置」などカスタマイズも可能です。どうしますか？

---

## 透かしを入れるのに、必要なライブラリ！
このプログラムを実行するために必要な主なライブラリは以下のとおりです：

---

### ✅ 必要なライブラリ

1. **PyPDF2**
   PDFファイルの読み書きやページ操作のために使用しています。

   ```
   pip install PyPDF2
   ```

2. **reportlab**
   PDFに透かし文字を描くためのライブラリです。

   ```
   pip install reportlab
   ```

---

### 💡補足

* `input.pdf` は同じフォルダにある前提で処理されています。ファイルがないとエラーになります。
* `reportlab.lib.pagesizes.letter` は用紙サイズ（USレター）を指定していますが、他のサイズも利用可能です。
* `setFillColorRGB(..., alpha=0.3)` の `alpha` は `reportlab` のバージョンによってサポートされない場合があります。その場合は透過処理なしで使うか、他の方法を検討する必要があります。

---

インストールが必要なコマンドをまとめると：

```bash
pip install PyPDF2 reportlab
```

もしエラーが出たら、その内容を教えてくれれば解決を手伝います！

---
---
