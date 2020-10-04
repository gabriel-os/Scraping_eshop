
def getPass():
    f=open("/credentials/cred.txt","r")
    lines=f.readlines()
    password=lines[0]
    f.close()

    return password
