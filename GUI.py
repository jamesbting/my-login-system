import tkinter as tk
from LoginSystem import LoginSystem
class GUI():
# data type that represents the GUI

    def __init__(self,file_name,master):
        #constructor
        self.login_system = LoginSystem(file_name)

        self.window = master
        self.window.title('Login System')

        #displays the place where you can enter your credentials to log in
        self.login_frame = tk.Frame(self.window)
        self.message_label = tk.Label(self.window, text='Enter your username and password')
        self.message_label.grid(row=0, column=0)

        #determines if the user has logged in or not yet
        self.logged_in = False

        # display the login and button frames
        self.display_login()
        self.login_frame.grid(row = 1, column = 0)

        # display the possible options
        self.options_frame = tk.Frame(self.window)
        self.display_options()
        self.options_frame.grid(row = 1, column = 1, sticky = 'n')

    # function that displays the items wthat will be created in the login window
    def display_login(self):

        self.clear_interaction_pane()
        self.login_frame = tk.Frame(self.window)
        row = self.create_interaction_pane()
        row +=1

        self.login_in_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_in_button.grid(row = row, column=1)

        self.login_frame.grid(row = 1, column = 0)

    # function that displays the items wthat will be created in the options window
    def display_options(self):
        self.main_menu_button = tk.Button(self.options_frame, text='Main Menu', command=self.main_menu,
                                          width=15)

        self.create_button = tk.Button(self.options_frame, text = 'Create an account', command = self.create_account,
                                       width = 15)
        self.change_button = tk.Button(self.options_frame, text = 'Change Password', command = self.change_password,
                                       width = 15)

        self.main_menu_button.grid(row=0, column=0)
        self.create_button.grid(row = 1,column = 0)
        if self.logged_in:
            self.change_button.grid(row = 2, column = 0)

    # function that returns the user to the main menu when clicked
    def main_menu(self):
        self.logged_in = False
        self.display_login()
        self.display_options()
        self.update_message('Enter your username and password')
        self.login_frame.grid(row = 1, column = 0)

    # function that will create an account when the button is clicked
    def create_account(self):
        self.update_message('Enter the username and the password for your new account')
        self.clear_interaction_pane()
        self.login_frame = tk.Frame(self.window)
        row = self.create_interaction_pane(confirm = True)
        row += 1

        self.submit_button = tk.Button(self.login_frame, text = 'Submit',command = self.submit_new_account)
        self.submit_button.grid(row = row, column = 1)
        self.login_frame.grid(row = 1, column = 0)

    # function that, when clicked, will attempt to submit the credentials provided by the user, and checking if
    # they are valid
    def submit_new_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()
        if (password != confirm_password):
            self.create_account()
            self.update_message('The passwords must match!')
        elif self.login_system.create_account(username, password):
            self.main_menu()
            self.update_message('Account created sucessfully!')
        else:
            self.create_account()
            self.update_message('Hmmm, something went wrong. Verify that the specified account dosen\'t exist already.')

    # function asks the user to change the passwords, and then passes them to the method below this one to see if they
    # are valid
    def change_password(self):
        self.update_message("Enter the username, the old password and the new password")
        self.clear_interaction_pane()
        self.login_frame = tk.Frame(self.window)
        row = self.create_interaction_pane(old_password = True, confirm = True)
        row += 1
        self.login_in_button.destroy()
        self.submit_button = tk.Button(self.login_frame, text='Submit', command=self.submit_changed_password)
        self.submit_button.grid(row=row, column=1)
        self.login_frame.grid(row = 1, column = 0)

    # checks if the new password is valid, and then see if it is valid
    def submit_changed_password(self):
        username = self.username_entry.get()
        old_password = self.old_password_entry.get()
        new_password = self.password_entry.get()

        if self.login_system.change_password(username,old_password,new_password):
            self.main_menu()
            self.update_message('Password changed succesfully.')
        else:
            self.update_message('That didn\'t work. Please try again')
            self.change_password()

    #functiont hat determins if the credientials provided are correct
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.login_system.login_function(username, password):
            self.logged_in = True
            self.display_options()
            self.display_login()
            self.update_message('Logged in succesfully. Welcome!')
        else:
            self.update_message('The username or password is incorrect')

    # function that will update the message to the user with the given string
    def update_message(self,message):
        self.message_label.destroy()
        self.message_label = tk.Label(self.window, text=message)
        self.message_label.grid(row=0, column=0)

    # clears the interaction pane
    def clear_interaction_pane(self):
        self.login_frame.destroy()

    # rebuilds the interaction pane
    def create_interaction_pane(self, old_password = False, confirm = False):

        # labels
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.password_label = tk.Label(self.login_frame, text="Password:")

        # entry fields where the user can type
        self.username_entry = tk.Entry(self.login_frame)
        self.password_entry = tk.Entry(self.login_frame, show='*')

        # place labels and entry fields into the login frame
        self.username_label.grid(row=0, column=0)
        self.password_label.grid(row=1, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        curr_row = 1
        if old_password: #check if we need a old password field, and if we do then we place it in 
            curr_row += 1
            self.old_password_label = tk.Label(self.login_frame, text='Old Password:')
            self.old_password_entry = tk.Entry(self.login_frame, show='*')
            self.old_password_label.grid(row=curr_row, column=0)
            self.old_password_entry.grid(row=curr_row, column=1)
            self.password_label = tk.Label(self.login_frame, text=" New Password:")
        else:
            self.password_label = tk.Label(self.login_frame, text="Password:")

        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_label.grid(row=curr_row, column=0)
        self.password_entry.grid(row=curr_row, column=1)

        if confirm: #check if we need a confirm field, and if we do then we place it in
            curr_row += 1
            self.confirm_label = tk.Label(self.login_frame, text="Confirm Password:")
            self.confirm_entry = tk.Entry(self.login_frame, show='*')

            self.confirm_label.grid(row=curr_row, column=0)
            self.confirm_entry.grid(row=curr_row, column=1)
        return curr_row

def main():
    root = tk.Tk()
    gui = GUI('database_name.yaml', root)
    root.mainloop()

main()