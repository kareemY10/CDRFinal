import re
import itertools
import pprint
import pdfrw
from pdfid import pdfid

pp = pprint.PrettyPrinter(indent=4)

TEST_FILENAME = "pdf.pdf"

def Name_analyze(filenames):
    options = pdfid.get_fake_options()
    options.scan = True
    options.json = True
    
    list_of_dict = pdfid.PDFiDMain(filenames, options)

    return list_of_dict

def Buffer_analyze(filenames, file_buffers):
    options = pdfid.get_fake_options()
    options.scan = True
    options.json = True

    list_of_dict = pdfid.PDFiDMain(filenames, options, file_buffers)
    return list_of_dict

def disarm_pdfs_by_buffer(filenames, file_buffers):
    options = pdfid.get_fake_options()

    options.disarm = True
    
    options.return_disarmed_buffer = True

    # disarm
    disarmed_pdf_buffers = pdfid.PDFiDMain(filenames, options, file_buffers)
    return disarmed_pdf_buffers




def Clean_Pdf_From_ClickAbles(filename):
    pdf = pdfrw.PdfReader("CDRRoom/"+str(filename))
    new_pdf = pdfrw.PdfWriter()  

    for page in pdf.pages:  

        for annot in page.Annots or []:
            old_url = annot.A.URI
            new_url = pdfrw.objects.pdfstring.PdfString("#")
            # print(new_url)
            annot.A.URI = new_url

            # print(annot.A.URI)
        new_pdf.addpage(page)   

    new_pdf.write('CDR_Processor/'+str('CDR_'+filename))
    return ('CDR_'+filename)



def remove_pdf_links(file_input, file_output):
    """ A Simplistic Python function to remove all links from a pdf file
    """
 
    # Open the pdf file in binary mode and extract contents
    f = open(file_input, mode='rb')
    data = f.read()
    f.close()
 
    # PDF encode URL info as /URI(<<URL PATH>>) so we need a
    # regex to extract this information
    regexstring = b"\\/URI \\((.*)\\)"
    dadsd = b"(www\.)?([^\.]+\.)?(com)?"
 
    # Compile string as regex
    regexcompiled = re.compile(regexstring, re.MULTILINE)

    regexcompiledd = re.compile(dadsd, re.MULTILINE)
 
    # Make a copy of the pdf content for the output pdf file
    output = data
 
    # Process the pdf contents
    items = regexcompiled.finditer(data)

    together = itertools.chain([regexcompiledd.finditer(data)], items)

 
    # For each regex match
    for match in items:
        # We have two options here, either replaces the PDF URL with a URL of the same size 
        # Like So:
        ## output = output.replace(match.group(1), ' ' * len(match.group(1)), 1)
        # Or replace the whole command with spaces to remove the URL
        # Like So:
        ## output = output.replace(match.group(0), ' ' * len(match.group(0)), 1)
        #
        # Experimentation shows that we should leave the ( ) in the encoded format
        # when we remove the /URI command, so the first option is the best approach
        output = output.replace(match.group(1), ' ' * len(match.group(1)), 1)
 
    # Because replacing the URL with spaces still leaves the link clickable and
    # opens a blank webpage in the local browser. We need to replace the 
    # preceding /URL command to remove the clickable aspect.
    # Note Experimentation shows that the pdf will crash if the () is not within
    # pdf /Link tag, so ensure that it is above
    # Replace might work for this task, but regex was handy so i used it
    # regex to extract this information
    regexstring = b"\\/URI"
 
    # Compile string as regex
    regexcompiled = re.compile(regexstring, re.MULTILINE)
 
    # Process the pdf contents
    items = regexcompiled.finditer(data)
 
    # For each regex match
    for match in items:
        # Replace the /URI tag with spaces
        output = output.replace(match.group(0), b' ' * len(match.group(0)), 1)
 
    # Save the modified pdf file as a binary file   
    f = open(file_output, mode='xb')
    f.write(output)
    f.close()
    print('done')
 
 

def ANALYZE_AND_DISARM(fileDST):
    filenames = [fileDST]
    file_buffers = []
    for filename in filenames:
        with open(filename, "rb") as f:
            file_buffers.append(f.read())

    print("analyzing file by name ,")
    results_1 = Name_analyze(filenames)
    pp.pprint(results_1)

    print("initiating buffer analyzing")
    results_2 = Buffer_analyze(filenames, file_buffers)
    pp.pprint(results_2)

    print("STARTING DISARM")
    disarmed_pdf_buffers = disarm_pdfs_by_buffer(filenames, file_buffers)

    print("STARTING DISARMED ANALYSIS")
    results_3 = Buffer_analyze(filenames, disarmed_pdf_buffers['buffers'])
    pp.pprint(results_3)
 





if __name__ == "__main__":
    # Clean_Pdf_From_ClickAbles()
    my_input="./pdf.pdf"
    my_output="new.pdf"
    ANALYZE_AND_DISARM('pdf.pdf')
    print("ok")
    
