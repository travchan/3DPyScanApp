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
        self.password = password

    def login(self):
        pass


if __name__ == '__main__':
    parser = MailParser('test@email.com', 'password')