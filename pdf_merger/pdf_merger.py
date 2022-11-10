# this version of the merger is deprecated
import sys
import PyPDF2

inputs = sys.argv[1:]  # check how to use this correctly!

pdf_list = ('dummy.pdf', 'twopage.pdf', 'wtr.pdf')


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(pdf_list)


#add watermark from wtr to all pages exercise
# import PyPDF2

# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#   page = template.getPage(i)
#   page.mergePage(watermark.getPage(0))
#   output.addPage(page)

#   with open('watermarked_output.pdf', 'wb') as file:
#     output.write(file)