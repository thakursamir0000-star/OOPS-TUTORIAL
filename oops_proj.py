class chatbook:

    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input=input("""Welcome to Chatbook
                             1. press 1 to signup
                             2. press 2 to login
                             3. press 3 to write a post
                             4. press 4 to msg a friend
                             5. press any other key to exit
                             """
                               )
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.login()
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()

    def signup(self):
        self.username=input('Enter your username')
        self.password=input('set your password')
        print('Signup successful')
        
        self.menu()
    def login(self):
        if self.username=='' and self.password=='':
            print('No user found, please signup first')
        else:    
            username=input('Enter your username')
            password=input('Enter your password')
            if self.username==username and self.password==password:
                print('Login successful')
                self.loggedin=True
            else:
                print('Invalid credentials')
        print("\n")
        self.menu()

obj=chatbook()