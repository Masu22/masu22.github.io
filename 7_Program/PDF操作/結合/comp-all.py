# カレントディレクトリの全PDFを結合
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
