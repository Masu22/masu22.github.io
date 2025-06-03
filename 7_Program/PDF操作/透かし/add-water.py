# input.pdfの全ページにウォーターマークを入れる！
# 必要なファイルはinput.pdfのみ
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
    
