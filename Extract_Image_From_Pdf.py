#pip install pikepdf

from pikepdf import Pdf, Name , PdfImage

old_pdf = Pdf.open("C:\Python_AK\PF-Withdraw.pdf")
page_1 = old_pdf.pages[0]

#print(list(page_1.images.keys()))

raw_image = page_1.images['Image_Path']
pdf_image = PdfImage(raw_image)
pdf_image.extract_to(fileprefix="New_Filename")