import PyPDF2
import pdfx
import re





def ExtractURLS(path):
    pdf = pdfx.PDFx(path)
    return pdf.get_references_as_dict()




remove_pdf_links("F2.pdf",ExtractURLS("F1"), "C:\Users\user\Desktop\CDRFP")