from imaplib import IMAP4_SSL
from imaplib import IMAP4
from os import mkdir, path
from base64 import b64encode, b64decode

import email.header
import os
import sys
import zipfile
from os import mkdir, path
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

        try:
            print('Connecting to ' + self.host)
            return IMAP4_SSL(self.host)
        except AttributeError:
            print('Invalid Host Address')

    def __login(self, mailbox):
        """ Uses login credentials to access email server

        Arguments:
            mailbox {mailbox} -- connection to email server database

        Returns:
            list -- list of all the emails in the inbox
        """

        try:
            mailbox.login(self.email, b64decode(self.password).decode('ascii'))
            print('Login Successful')
            return mailbox.list()
        except IMAP4.error:
            print('Login Failed.')

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
            subjectline = email.header.decode_header(email_message['Subject'])[0][0].replace(" ", "_").replace(":", "_")
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            try:
                mkdir('C:/Users/Public/scans')
            except:
                pass
            if part.get_content_type() == 'application/zip':
                try:
                    open( path.join('C:/Users/Public/scans', '%s.zip' % subjectline), 'wb').write(part.get_payload(decode=True))
                    unzipfile = zipfile.ZipFile(path.join('C:/Users/Public/scans', '%s.zip' % subjectline), 'r')
                    unzipfile.extractall(
                       'C:/Users/Public/scans')
                    unzipfile.close()
                    os.rename(path.join('C:/Users/Public/scans', 'Model.obj'),
                           path.join('C:/Users/Public/scans','%s.obj' % subjectline))
                    os.remove(path.join('C:/Users/Public/scans' , '%s.zip' % subjectline))
                except FileExistsError:
                    print('Error Duplicated File Name: "%s"' % subjectline)
                    os.remove(path.join('C:/Users/Public/scans' , '%s.zip' % subjectline))
                    os.remove(path.join('C:/Users/Public/scans' , 'Model.obj'))


        return fileName


    def getMail(self):
        """ Parses through email to download attachments
        """

        mailBox = self.__connectToServer()
        try:
            self.__login(mailBox)
        
            try: 
                mailBox.select()
                searchQuery = '(BODY "SDK")'
                unSeen = '(UNSEEN)'

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

                    subject = str(email.header.decode_header(email_message['Subject'])[0][0])
                    print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(
                        file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))

                mailBox.close()
                mailBox.logout()
            except IMAP4.error:
                print('Unable to get mail. Please check your email and password.')
        except AttributeError:
            pass        

if __name__ == '__main__':
    import credentials as creds # credentials.py is a local file containing email credentials; hidden on GitHub by .gitignore
    parser = MailParser(creds.OUTLOOK_EMAIL, creds.OUTLOOK_PASSWORD)
    parser.getMail()
