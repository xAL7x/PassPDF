from PyPDF2 import PdfFileWriter,PdfFileReader
pdfw=PdfFileWriter()
print('\033[3;34m')
pdf=PdfFileReader(input("enter the name file \n "))
for page_num in range(pdf.numPages):
    pdfw.addPage(pdf.getPage(page_num))

password=input("\033[3;31m enter the password >> ")
pdfw.encrypt(password)
a=input("\033[3;36m enter the name new file \n")
with open(a+".pdf","wb")as f:
    pdfw.write(f)
    f.close()
