import imaplib
import email
import os



def get_mail_client(email_address):
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993
    
    password = ""
    with open("Secret.txt", "r") as f:
        password = f.read().strip()

    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(email_address, password)
    return mail



def get_msg_object(data):
    for response_part in data:
        if isinstance(response_part, tuple):
            return email.message_from_bytes(response_part[1])

def get_top_10_emails(category):
   
    status, response = mail.uid('search', 'X-GM-RAW "category:' + category + '"')

    response = response[0].decode('utf-8').split()
    response.reverse()
    response = response[:min(1, len(response))]
    return response



mail=get_mail_client("donyacdrproject@gmail.com")
mail.select('INBOX')



for uid in get_top_10_emails(''):
    status, data = mail.uid('fetch', uid, '(RFC822)')
    msg = get_msg_object(data)
    #print(type(msg))
    # print(filename)

for part in msg.walk():
    #print(part.get_content_type())
    if part.get_content_maintype() == 'multipart':
        continue
    if part.get('Content-Disposition') is None:
        continue

    fileName = part.get_filename()
    
    if bool(fileName):
        # this path will only work on kareem's computer and when we add UI we should modify it according to what the user wants
        filePath = os.path.join('C:/Users/user/Desktop/CDRFinal/CDRRoom', fileName)
    
    if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        
        
print(fileName)

