import sqlite3
from tkinter import StringVar, Label, Entry, Button, Tk


class Login:
    def __init__(self):
        print("Inside Login Module")
        self.login = Tk()  # Login Frame
        self.login.wm_title("E-mail Scheduler")
        self.login.withdraw()
        self.authenticate = False
        self.username = None
        self.password = None

    def check(self):
        """
        Verify Credential
        """
        if self.username.get() == "" or self.password.get() == "":
            Label(self.login, width=30, text="Wrong Username or Password").grid(row=3, column=1)
            return

        print("Username: ", self.username.get())
        print("Password: ", self.password.get())

        self.authenticate = False
        self.login.destroy()

    def login_window(self):
        """
        Front End of Login Module.
        """

        self.login.deiconify()

        Label(self.login, text="Username", height=2, width=12, borderwidth=2,
              relief="groove", font=("Times New Roman", 12)).grid(row=0, padx=5, pady=5)

        Label(self.login, text="Password", height=2, width=12, borderwidth=2, relief="groove",
              font=("Times New Roman", 12)).grid(row=1, padx=5, pady=5)

        self.username = Entry(self.login, width="30", borderwidth=2, relief="groove", font=("Times New Roman", 12))
        self.username.grid(row=0, column=1, ipady=5, padx=5, pady=5)
        self.username.focus()

        self.password = Entry(self.login, width="30", show="*", borderwidth=2, relief="groove",
                              font=("Times New Roman", 12))
        self.password.grid(row=1, column=1, ipady=5, padx=5, pady=5)

        Button(self.login, text="Log In", command=self.check).grid(row=4, column=1, padx="40", sticky="w", pady=5)
        Button(self.login, text="Register ").grid(row=4, column=1, padx="40", sticky="e", pady=5)

        self.login.mainloop()

    # TODO: Add below module for login feature 
    # def check_creds(self):
    #     c.execute("SELECT username,password from users")
    #     for s in c.fetchall():
    #         if v1.get()==s[0]:        # Checking Username in Database
    #             if v2.get()==s[1]:    # Checking Password against that username
    #                 self.login.withdraw()
    #                 select()
    #             else:
    #                 Label(self.login,
    #                 text="Username and Password Combination not matched").grid(row=3,column=1)
    #         else:
    #             Label(self.login,
    #             text="Username and Password Combination not matched").grid(row=3,column=1)

    def __del__(self):
        print("Object deleted SuccessFully")
