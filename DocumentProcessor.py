# This python file to work with the doucments (.docx type)
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

def DisableLinks(filepath):
    doc=Document(filepath)
    rels=doc.part.rels
    urls=[]
    for rel in rels:
        if rels[rel].reltype == RT.HYPERLINK:
            urls.append(rels[rel]._target)
            doc.part.rels[rel]._target='#'
    doc.save(filepath)
    print("it's done.")
    return urls



def ReadProperties(filepath):
    document = Document(filepath)
    # read properties
    document_property = document.core_properties
    # print all accessible document properties
    print([p for p in dir(document_property) if not p.startswith('_')])
    # print author of the document
    print(document_property.author)
    # set new value for title
    document_property.title = 'Everything is Awesome'
    # save changes to current file
    # document.save(path)


ReadProperties('C:\\temp\\NAC\\FinalProject\\CDRFP\\CDRFinal\\Test.docm')
    

