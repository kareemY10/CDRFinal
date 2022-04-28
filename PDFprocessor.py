from bs4 import BeautifulSoup
import aspose.words as aw

# def ExtractURLS(path):
#     pdf = pdfx.PDFx(path)
#     return pdf.get_references_as_dict()

# def CheckUrl(str):
#  regex = re.compile(
#         r'^(?:http|ftp)s?://'
#         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
#         r'localhost|' 
#         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
#         r'(?::\d+)?' 
#         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
#  if(re.match(regex,str)is not None):
#     return True
#  else:
#      return False


# def Clean_txtFile(myPath):
#     with open(myPath, encoding='utf-8') as f:
#         content = f.readlines()
#     content = [x.strip() for x in content]
#     new_content = []
#     url_format='https://'
#     c=''
#     for item in content:
#         print(item)
#         for i in item.split():
#             if i.startswith(url_format):
#                 c='' 
#             else:
#                 c=i
#             new_content.append(c)        
#         new_content.append('\n')
#     print(new_content)
#     with open('result.txt', mode='wt', encoding='utf-8') as myfile:
#         myfile.write(''.join(new_content))


def Clean_HyperLinks(myfile):
    # with open(myfile, 'r') as file:
    #  data = file.read().rstrip()
    spam = """<p>Hello world, it's <a href="https://google.com">foo bar time</a></p>
        <p>Hello world, it's <a href="https://stackoverflow.com">spam eggs</a></p>"""

    soup = BeautifulSoup(spam, 'html.parser')
    # for a_tag in soup.find_all('a'):
        # a_tag.replace_with(a_tag.text)

    # print(soup.text)
    print(soup)
    print('ok!')

def Pdf_to_Html(myFile):
    # Load the PDF file
    doc = aw.Document(myFile)

    # Save the document as HTML
    doc.save("Test\Document.html")
# This is our application entry point
if __name__ == "__main__":
    my_input ="C:\\temp\\NAC\\FinalProject\\JWP_2021_MoedA.pdf"
    # Pdf_to_Html(myFile=my_input)
    Clean_HyperLinks('Test\Document.html')
    
