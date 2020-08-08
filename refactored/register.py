from tkinter import Tk, Label, Entry, Button


class Register:
    def __init__(self):
        self.reg = Tk()            # Register frame
        self.reg.wm_title("E-mail Scheduler")
        self.reg.withdraw()

    def back(self):
        pass

    def register_window(self):

        self.reg.deiconify()

        # Defined Labels to display some text 

        labels_text = ["Username", 'Name', 'Email', 'Password', 'Confirm Password']

        for row,text in enumerate(labels_text):    
                Label(self.reg, text=text, height=2, width=18, borderwidth=2,
                relief="groove", font=("Times New Roman", 12)).grid(
                    row=row, sticky='w', padx=10, pady=10)         

        # Label(self.reg, text='Username', height=2, width=20, borderwidth=2,
        #     relief="groove", font=("Times New Roman", 12)).grid(
        #         row=0, sticky='w', padx=5, pady=5)                                            # Username
        # Label(self.reg, text='Name ',  height=2, width=20, borderwidth=2,
        #       relief="groove", font=("Times New Roman", 12)).grid(
        #           row=1, sticky='w', padx=5, pady=5)                                          # Name
        # Label(self.reg, text='Email',  height=2, width=20, borderwidth=2,
        #       relief="groove", font=("Times New Roman", 12)).grid(
        #           row=2, sticky='w', padx=5, pady=5)                                          # Email
        # Label(self.reg, text='Password ',  height=2, width=20, borderwidth=2,
        #       relief="groove", font=("Times New Roman", 12)).grid(
        #           row=6, sticky='w', padx=5, pady=5)                                          # Password 
        # Label(self.reg, text='Confirm Password ',  height=2, width=20, borderwidth=2,
        #       relief="groove", font=("Times New Roman", 12)).grid(
        #           row=7, sticky='w', padx=5, pady=5)                                          # Confirm Password
        
        # Entry Box Defined to take input from user.  

        self.username = Entry(self.reg, width='35', borderwidth=2, 
                            relief="groove", font=("Times New Roman", 12))
        self.username.grid(row=0, column=1, padx=10, pady=5, ipady = 10)                        # Username

        self.name = Entry(self.reg, width='35', borderwidth=2,
                         relief="groove", font=("Times New Roman", 12))
        self.name.grid(row=1, column=1, padx=10, pady=5, ipady = 10)                            # Name

        self.email = Entry(self.reg, width='35', borderwidth=2,
                         relief="groove", font=("Times New Roman", 12))
        self.email.grid(row=2, column=1, padx=10, pady=5, ipady = 10)                           # Email

        self.password = Entry(self.reg, show='*', width='35', borderwidth=2,
                             relief="groove", font=("Times New Roman", 12))
        self.password.grid(row=3, column=1, padx=10, pady=5, ipady = 10)                        # Password

        self.confirm_password = Entry(self.reg, show='*', width='35', borderwidth=2,
                                     relief="groove", font=("Times New Roman", 12))
        self.confirm_password.grid(row=4, column=1, padx=10, pady=5, ipady = 10 )               # Confirm password

        # defined buttons to perform oprations

        Button(self.reg, text = 'Sign Up', command = self.save_details).grid(   
            row = 10, column = 1, padx = 20, sticky = 'w')
        Button(self.reg, text = ' Cancel', command = self.back).grid(
            row = 10, column = 1, padx = 20, sticky = 'e')

        self.reg.mainloop()


    def save_details(self):         # to store in database

        new_user_info = {
            "username" : self.username.get(),
            "name" : self.name.get(),
            "email" : self.email.get(),
            "password" : self.password.get(),
            "confirm_password" : self.confirm_password.get()
        }


        if new_user_info["password"] != new_user_info["confirm_password"]:
            Label(self.reg, text="Please Enter Same password ").grid(
                row=8, column=1)
            return

        print( f'''usernmae: { new_user_info['username'] } \n name:{new_user_info['name']}
        email: {new_user_info['email']} \n password: {new_user_info['password']} 
        confirm_pass: {new_user_info['confirm_password']}''' )

if __name__ == "__main__":
    regis = Register()
    regis.register_window()