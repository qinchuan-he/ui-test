import logging
import os
from enum import Enum
import fitz


class PdfType(Enum):
    NORMAL = "normal"
    IMAGE = "image"
    ENCRYPT = "encrypted"
    OTHER = "other"


def check_pdf_type(file):
    try:
        pdf_doc_fitz = fitz.open(filetype="pdf", stream=file.read())
    except Exception as e:
        # logging.warning("fitz加载失败！ %s" % e.__str__())
        return PdfType.OTHER, pdf_doc_fitz, -1
    if pdf_doc_fitz.isEncrypted:
        return PdfType.ENCRYPT, pdf_doc_fitz, -1
    for i, page in enumerate(pdf_doc_fitz):  # iterate the document pages
        text = page.getText()
        text = text.replace("\t", "").replace("\r", "").replace("\n", "")
        if text.strip():
            return PdfType.NORMAL, pdf_doc_fitz, i
    return PdfType.IMAGE, pdf_doc_fitz, -1

if __name__ == '__main__':
    file = open('other.txt','r+')
    dir_path = "/data/judge/"
    # ls = os.listdir(dir_path)
    ls = file.readlines()
    for f in ls:
        f = f.replace('\n','')
        with open(dir_path + f, "rb") as pdf_file:
            rs = check_pdf_type(pdf_file)
            if rs[0] != PdfType.IMAGE:
                print("文件名%s" % f, "\t第%d页开始有文字" % rs[-1])

