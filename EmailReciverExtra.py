from email import message
import imaplib
import base64
import os
import email

def Find_Emails(mail,password):
    imap_server='imap.gmail.com'
    imap=imaplib.IMAP4_SSL(imap_server)
    imap.login(mail,password)
    imap.select('Inbox')
    lis=[]
    _,msg_nums=imap.search(None,'ALL')
    count_msg=msg_nums[0].split()[len(msg_nums[0].split())-1].decode('utf-8')
    for msgnum in msg_nums[0].split():
        _,data=imap.fetch(msgnum,"(RFC822)")
        message=email.message_from_bytes(data[0][1])
        lis.append(message)

    return (count_msg,lis)


def get(mail,password):
    email_user = mail
    email_pass = password
    gmail_host='imap.gmail.com'
    gmail_port=993
    mail = imaplib.IMAP4_SSL(gmail_host,gmail_port)
    mail.login(email_user, email_pass)
    mail.select('Inbox')
    type_, data = mail.search(None, 'ALL')
    n_m=data[0].split()[len(data[0].split())-1]
    number_Msg=n_m.split("'")
    print(number_Msg
    )
    mail_ids = data[0]
    id_list = mail_ids.split()
    for num in data[0].split():
        _ , data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
    # converts byte literal to string removing b''
        raw_mail_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_mail_string)
        print(email_message.get('From'))
    # downloading attachments
        print('content:')
        for part in email_message.walk():
            if part.get_content_type() =='text/plain':
                print(part.as_string())
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            if bool(fileName):
                filePath = os.path.join('CDRRoom', fileName)
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                print('Downloaded "{file}" from email titled "{subject}"'.format(file=fileName, subject=subject))
        
            # print (fileName ,subject)

# Count_Emails('cdrpro2022@gmail.com','uqsnaaeoxnigvftu')