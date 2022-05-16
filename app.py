import EmailReciver
import PDFprocessor
from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def hello_world():
    
    filename=EmailReciver.get_attachments()
    PDFprocessor.Clean_Pdf_From_ClickAbles(filename=filename)

    return "emails in CDR Room"






if __name__ == '__main__':
    app.run(debug=True)