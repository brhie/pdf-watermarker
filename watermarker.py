import PyPDF2

object_file = input("What file do you want to watermark?")
watermark = input("What is the watermark file?")
output = input("What do you want it to be saved as?")

def insert_watermark(object_pdf, wtr_pdf, output_pdf):
    object_reader = PyPDF2.PdfFileReader(object_pdf)
    wtr_reader = PyPDF2.PdfFileReader(wtr_pdf)
    watermark = wtr_reader.getPage(0)
    writer = PyPDF2.PdfFileWriter()

    for page in range(object_reader.getNumPages()):
        page_object = object_reader.getPage(page)
        page_object.mergePage(watermark)
        writer.addPage(page_object)
        print(f"adding watermarker to page {page + 1}")
    
    with open(output_pdf, "wb") as out:
        writer.write(out)
        print("all done!")


if __name__ == "__main__":
    insert_watermark(object_file, watermark, output)