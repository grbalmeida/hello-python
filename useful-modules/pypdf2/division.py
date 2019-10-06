import PyPDF2
import os

with open('pdf/new_file.pdf', 'rb') as pdf_file:
  reader = PyPDF2.PdfFileReader(pdf_file)
  num_pages = reader.getNumPages()
  print(f'Num pages: {num_pages}')

  for num_page in range(num_pages):
    writer = PyPDF2.PdfFileWriter()
    current_page = reader.getPage(num_page)
    writer.addPage(current_page)

    with open(f'new-pdf/{num_page}.pdf', 'wb') as new_pdf:
      writer.write(new_pdf)
