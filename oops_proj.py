class chatbook():

    __user_id = 0

    def __init__(self):
        # self.name = 'Default User'
        self.__name = 'Default User'
        self.user_id = chatbook.__user_id
        chatbook.__user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    def menu(self):
        user_input = input("""Welcome to chatbook ! How would you like to proceed ?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.msg_frnd()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here --> ")
        password = input("Set up your password here --> ")
        self.username = email
        self.password = password

        print("you have signedup successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username== '' and self.password== '':
            print('Sign up by pressing 1 in the main menu')
        else:
            uname = input("Enter your username or email here --> ")
            pwd = input("Enter your password here --> ")
            if self.username == uname and self.password==pwd:
                print("you have signed in successfully.")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()

    def write_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here --> ")
            print(f"Your post reads like this: {txt}")
        else:
            print("You need to signin first to post something.")

        print("\n")
        self.menu()

    def msg_frnd(self):
        if self.loggedin == True:
            txt = input("Enter your message here --> ")
            frnd = input("Whom to send the message? --> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print('You need to sign in first')
        print("\n")
        self.menu()


# obj = chatbook()