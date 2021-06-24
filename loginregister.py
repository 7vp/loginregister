#start
 
users = {}
status = ""
 
def displayMenu():
    status = input("[BOT] Are you registered user? y/n?")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
    createLogin = input("[BOT] Create your username!: ")
 
    if createLogin in users:
        print("[BOT] Login name already exist!")
    else:
        createPassw = input("[BOT] Create password: ")
        users[createLogin] = createPassw
        print("[BOT] User created!")
 
def oldUser():
    login = input("[BOT] Enter login name: ")
    passw = input("[BOT] Enter password: ")
 
    if login in users and users[login] == passw:
        print("[BOT] Login successful!")
    else:
        print("[BOT] User doesn't exist or wrong password!")
 
while status != "q":
    displayMenu()
    
#end

@idiol
