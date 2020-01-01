# my-login-system
This is a login system that I built in Python as a personal project. It started out as just a single .py file reading from a .txt file, that I built to practice OOD and File IO.

As an upgrade, I hoped to include a cryptographic hash function that will hide the password in the text file and prevent it from being read by opening the text file. 

In the process of developing the upgrade, the program now has a GUI that was built using the tkinter library,a SHA 256 encryption to hide the passwords from prying eyes, a config file to manage the name of the database, and a .db file that stores all the passwords and is accessed using the SQLite3 library.

NOTE: For version 1.0, the files 'Account List.txt' and 'Account.py' is no longer necessary and unused
