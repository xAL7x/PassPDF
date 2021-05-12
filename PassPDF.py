from PyPDF2 import PdfFileWriter, PdfFileReader
import time


def PassPDF():
    pdf_fw = PdfFileWriter()
    pdf_file = PdfFileReader(input("What is the file name? "))

    for page_num in range(pdf_file.numPages):
        pdf_fw.addPage(pdf_file.getPage(page_num))

    file_password = input("Please enter the password you want: ")
    pdf_fw.encrypt(file_password)

    new_file_name = input("Please enter the new file name: ")
    with open(f'{new_file_name}.pdf', "wb") as file:
        pdf_fw.write(file)
        file.close()
        print('Done, Successfully added a encrypted the file!')


try:
    PassPDF()
except KeyboardInterrupt:
    print('\nExiting!')
    time.sleep(0.5)
    quit()
