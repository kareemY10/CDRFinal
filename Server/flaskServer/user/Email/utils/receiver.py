import imaplib
import email
# import user.Database.database as DBAccess
# import user.Database.Entities as model
from models.user import user
import os


class EmailReceiver:
    
    def __init__(self,User : user ,keyword : str):
        """_summary_

        Args:
            email_address (str): email address
            AppKey (str): password from kareem(server-side)
            keyword (str): the type of emails(inbox,spam,etc.)
        """
        self._email = User._credentials[0]
        self._password = User._credentials[1]
        self._imapserver = User._credentials[2]
        self._option = keyword
        self._dir = User._dir
    
    def receiver(self):
        AttahcmentsPath = None
        dict = {}
        imap = imaplib.IMAP4_SSL(self._imapserver)
        imap.login(self._email,self._password)
        imap.select(self._option)
        _,arr = imap.search(None,'ALL')
        for message in arr[0].split():
            _,data = imap.fetch(message,"(RFC822)")        
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            del raw_email,raw_email_string
            From = email_message.get('From')
            to = email_message.get('To')
            bcc = email_message.get('BCC')
            date = email_message.get('Date')
            subject = email_message.get('Subject')
            dict[From+date]= [From,to,bcc,date,subject]
            
            # firstTime = True
            # content = ''    
            # # iterate through the tree of mail
            # for part in email_message.walk():
                
            #     if part.get_content_type() == 'text/plain':
            #         content += part.as_string()
            #         continue
            #     if part.get_content_type() == 'multipart':
            #         continue
            #     if part.get('Content-Disposition') is None:
            #         continue
            #     filename = part.get_filename()
            #     if firstTime :
            #         firstTime = False
            #         AttahcmentsPath = os.mkdir(os.path.join(self._dir,))            
            #     if bool(filename):
            #         filepath = 
        return dict
    
         
        