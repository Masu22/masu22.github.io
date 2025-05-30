# file1.pdfとfile2.pdfを結合して、merged_output.pdfを出力
from pypdf import PdfReader, PdfWriter

writer = PdfWriter()

for pdf in ['file1.pdf', 'file2.pdf']:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

with open("merged_output.pdf", "wb") as f:
    writer.write(f)
