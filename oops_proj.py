class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    def menu(self):
        user_input = input("""welcome to chatbook!How would you like to proceed
                         1.press 1 to signup
                         2. press 2 to signin
                         3. press 3 to writa a post
                         4. press 4 to message a friend
                         5. press other key to exit""") 
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    def signup(self):
        email=input("enter email here")
        pwd=input("enter password here")
        self.username = email
        self.password = pwd
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username== '' and self.password=='':
            print("please signup first by pressing 1 in the main menu")
        else:
            uname=input("enter email/username here")
            pwd=input("enter password here")  
            if self.username==uname and self.password==pwd:
                print("Logged in successfully")
                self.loggedin= True
            else:
                Print("Input correct credentials")
        print("\n")
        self.menu()

            



obj=chatbook()


