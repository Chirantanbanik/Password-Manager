from cryptography.fernet import Fernet
from getpass import getpass

main_pwd = input("What is the main password?")
    

def view():
  with open('password.docx', 'r') as f:
    for line in f.readlines():
      print(line.rstrip())
   
def add():
  name = input('Account name: ')
  pwd = getpass('Password: ')
  with open('password.docx', 'a') as f:
    f.write(name + " and " + pwd + "\n")
    
    
while True:
  mode = input("Would you like to add a new password or view the existing ones (view, add), press q to quit?").lower()
  if mode == "q":
      break
  if mode == "view":
    view()
  elif mode == "add":
    add()
  else:
    print("Invalid mode.")
    continue