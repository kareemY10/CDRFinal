import smtplib
import base64



UEmail="example@gmail.com"
Password="example123"


def SendFile(filename,reciver):
    #try:
    fo = open(filename, "rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)
    #except:
    #   print('fileNotFound')
    #    return
    
    
    marker = "AUNIQUEMARKER"
    body =  """
                The body of the emails will be here

            """

    part1 = """From: From Person <me@fromdomain.net>
                To: To Person <amrood.admin@gmail.com>
                Subject: Sending Attachement
                MIME-Version: 1.0
                Content-Type: multipart/mixed; boundary=%s
                --%s
                """ % (marker, marker)


    part2 = """Content-Type: text/plain
                    Content-Transfer-Encoding:8bit

                                %s
                                --%s
            """ % (body,marker)

    
    # Define the attachment section
    part3 = """Content-Type: multipart/mixed; name=\"%s\"
                Content-Transfer-Encoding:base64
                Content-Disposition: attachment; filename=%s
                    %s
                    --%s--
                """ %(filename, filename, encodedcontent, marker)
    msg=part1 + part2 + part3

    
    server = smtplib.SMTP(SERVER, 1025)
    server.sendmail(FROM, TO, message)
    server.quit()
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, reciever, msg)
    print ("Successfully sent email")
    






 