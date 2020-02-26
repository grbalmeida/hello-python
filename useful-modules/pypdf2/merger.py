import PyPDF2
import os

path = 'pdf'

new_pdf = PyPDF2.PdfFileMerger()

for root, directories, files in os.walk(path):
  for file in files:
    full_file_path = os.path.join(root, file)
    
    pdf_file = open(full_file_path, 'rb')
    new_pdf.append(pdf_file)

with open(f'{path}/new_file.pdf', 'wb') as my_new_pdf:
  new_pdf.write(my_new_pdf)
