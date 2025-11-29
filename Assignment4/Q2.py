import re
def verify_passwd(s):
    c1=r"^[A-Za-z0-9@#$%^&*!]{8,}$"
    c2=r"\d"
    c3=r"[A-Za-z]"
    c4=r"[@#$%^&*!]"
    return re.fullmatch(c1,s) and re.search(c2,s) and re.search(c3,s) and re.search(c4,s)
passwords=["Password1!","pass","Passw0rd","P@ssw0rd","12345678","abcdEFGH@","Abc1@","Valid@123"]
for p in passwords:
    if verify_passwd(p):
        print(p,"-Valid Password")
    else:
        print(p,"-Invalid Password")