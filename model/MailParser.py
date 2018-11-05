from imaplib import IMAP4_SSL
from os import mkdir, path
from base64 import b64encode, b64decode

import email.header

class MailParser:
    """ Parses emails for files sent by the Scanner application
    """

    def __init__(self, email, password):
        """ Uses user input email and password to login to retrieve mesh files
        
        Arguments:
            email {string} -- user's email
            password {string} -- user's password
        """

        self.email = email
        self.password = b64encode(password.encode('ascii'))

        self.__assignHost(self.email)

    def __assignHost(self, email_str):
        """ determines the host address based on the user email input
        
        Arguments:
            email_str {string} -- email pulled from the user input
        """

        email_str = self.email.split('@')

        if email_str[1] == 'outlook.com':
            self.host = 'imap-mail.' + email_str[1]
        elif email_str[1] == 'gmail.com':
            self.host = 'imap.' + email_str[1]

    def __connectToServer(self):
        """ Connects to email server
        
        Returns:
            mailbox -- connection to email server database
        """

        print('Connecting to ' + self.host)
        return IMAP4_SSL(self.host)

    def __login(self, mailbox):
        """ Uses login credentials to access email server
        
        Arguments:
            mailbox {mailbox} -- connection to email server database
        
        Returns:
            list -- list of all the emails in the inbox
        """

        mailbox.login(self.email, b64decode(self.password).decode('ascii'))
        return mailbox.list()

    def __downloadAttachments(self, email_message):
        """ downloads attachments from the users email
        
        Arguments:
            email_message {object} -- current email message
        
        Returns:
            filepath -- filepath of the saved objects
        """

        fileName = ""
        # downloading attachments
        for part in email_message.walk():
            # this part comes from the snipped I don't understand yet...
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()

            if bool(fileName):
                try:
                    mkdir('C:/Users/Public/scans')
                except:
                    pass
                filePath = path.join('C:/Users/Public/scans', fileName)
                if not path.isfile(filePath):
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()

        return fileName    
            

    def getMail(self):
        """ Parses through email to download attachments
        """

        mailBox = self.__connectToServer()
        self.__login(mailBox)

        mailBox.select()
        searchQuery = '(BODY "SDK")'

        result, data = mailBox.uid('search', None, searchQuery)
        ids = data[0]
        # list of uids
        id_list = ids.split()

        i = len(id_list)
        for x in range(i):
            latest_email_uid = id_list[x]

            # fetch the email body (RFC822) for the given ID
            result, email_data = mailBox.uid('fetch', latest_email_uid, '(RFC822)')
            # I think I am fetching a bit too much here...

            raw_email = email_data[0][1]

            # converts byte literal to string removing b''
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)

            fileName = self.__downloadAttachments(email_message)

            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(
                file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))

        mailBox.close()
        mailBox.logout()

if __name__ == '__main__':
    import credentials as creds
    parser = MailParser(creds.OUTLOOK_EMAIL, creds.OUTLOOK_PASSWORD)
    parser.getMail()
