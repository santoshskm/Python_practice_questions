# # PDF TO IMAGE CONVERSION
# # IMPORT LIBRARIES
# import pdf2image
# from PIL import Image
# import time
#
# # DECLARE CONSTANTS
# PDF_PATH = "/home/santosh/Documents/psp_docs/narrative3.pdf"
# DPI = 200
# OUTPUT_FOLDER = "/home/santosh/Documents/psp_docs"
# FIRST_PAGE = None
# LAST_PAGE = None
# FORMAT = 'png'
# THREAD_COUNT = 1
# USERPWD = None
# USE_CROPBOX = False
# STRICT = False
#
#
# def pdftopil():
#     # This method reads a pdf and converts it into a sequence of images
#     # PDF_PATH sets the path to the PDF file
#     # dpi parameter assists in adjusting the resolution of the image
#     # output_folder parameter sets the path to the folder to which the PIL images can be stored (optional)
#     # first_page parameter allows you to set a first page to be processed by pdftoppm
#     # last_page parameter allows you to set a last page to be processed by pdftoppm
#     # fmt parameter allows to set the format of pdftoppm conversion (PpmImageFile, TIFF)
#     # thread_count parameter allows you to set how many thread will be used for conversion.
#     # userpw parameter allows you to set a password to unlock the converted PDF
#     # use_cropbox parameter allows you to use the crop box instead of the media box when converting
#     # strict parameter allows you to catch pdftoppm syntax error with a custom type PDFSyntaxError
#
#     start_time = time.time()
#     pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, fmt=FORMAT,userpw=USERPWD,
#                                              use_cropbox=USE_CROPBOX, strict=STRICT)
#     print("Time taken : " + str(time.time() - start_time))
#     return pil_images
#
#
# def save_images(pil_images):
#     # This method helps in converting the images in PIL Image file format to the required image format
#     index = 1
#     for image in pil_images:
#         image.save("page_" + str(index) + ".png")
#         index += 1
#
#
# if __name__ == "__main__":
#     pil_images = pdftopil()
#     save_images(pil_images)


# from pdf2image import convert_from_path
# input_path='/home/santosh/Documents/psp_docs/filable/issue/2017SA022695_12046.pdf'
# output_path='/home/santosh/Documents/psp_docs/filable/issue'
# images_from_path = convert_from_path(pdf_path= input_path,dpi=300, output_folder=output_path,fmt='png',size=3000)
from PyPDF2 import PdfFileReader,PdfFileWriter
import pathlib
import os
from natsort import natsorted
file_path = "/home/santosh/Documents/local docs/pypdf_issue.pdf"
dest_folder_path = "/home/santosh/Documents/local docs"
def split_pdf_into_singepdf(file_path, dest_folder_path):
    converted_pdfs = []
    inputpdf = PdfFileReader(open(file_path, "rb"), strict=False)
    # file_name = FileAssistant.get_file_name(file_path)
    file_name = file_path.split('/')[-1]
    if not dest_folder_path.endswith("/"):
        dest_folder = dest_folder_path + "/"
    else:
        dest_folder = dest_folder_path
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(dest_folder + file_name + "-%s.pdf" % str(i+1), "wb") as outputStream:
            output.write(outputStream)
    dt = pathlib.Path(dest_folder)
    for f in dt.iterdir():
        if f.name.startswith(file_name) and f.name.endswith('.pdf') and str(f) != file_path:
            converted_pdfs.append(str(f))

    converted_pdfs = natsorted(converted_pdfs)
    print(converted_pdfs)
    return converted_pdfs

split_pdf_into_singepdf(file_path, dest_folder_path)