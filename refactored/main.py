import login
# import register

class main():

    def __init__(self):
        print("Program Begin")

    def control(self):
        log = login.Login()
        log.login_window()
        if log.authernticate == True:
            print("Login Successful")
        else:
            print("Login Failed")
        del log
        print("Got Our Control Back")


if __name__ == "__main__" :
    obj = main()
    obj.control()
