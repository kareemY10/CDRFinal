import user.Database.database as DB
from user.Database.Entities import User 
from utils.config import CDR_PATH

import os
from message import Message
class user:
    
    def __init__(self,email_address,appkey,imapserver):
        doc = DB.DataBase()._users.find_one({User.EMAIL_ADDRESS: email_address})
        DirPath =CDR_PATH+'\\'+str(doc[0][User.CODE])
        del doc
        os.mkdir(DirPath)
        self._dir = DirPath
        self._credentials = [email_address,appkey,imapserver]

    def getMessages(self) ->list[Message]:
        pass
        
          