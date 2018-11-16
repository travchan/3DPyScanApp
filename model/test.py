def getMail(self, scan_type):
    """ Parses through email to download attachments
    """

    mailBox = self.__connectToServer()
    try:
        log_stat = self.__login(mailBox)

        try:
            mailBox.select()
            searchQuery = '(BODY "SDK")'
            unSeen = '(UNSEEN)'
            if scan_type == 1:
                result, data = mailBox.uid('search', None, searchQuery)
            else:
                result, data = mailBox.uid('search', None, searchQuery, unSeen)
            ids = data[0]
            # list of uids
            id_list = ids.split()

            i = len(id_list)
            for x in range(i):
                latest_email_uid = id_list[x]

                # fetch the email body (RFC822) for the given ID
                result, email_data = mailBox.uid(
                    'fetch', latest_email_uid, '(RFC822)')

                raw_email = email_data[0][1]

                # converts byte literal to string removing b''
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)

                fileName = self.__downloadAttachments(email_message)

                subject = str(email.header.decode_header(
                    email_message['Subject'])[0][0])
                print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(
                    file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))

            mailBox.close()
            mailBox.logout()
            return log_stat
        except IMAP4.error:
            print('Unable to get mail. Please check your email and password.')
    except AttributeError:
        pass