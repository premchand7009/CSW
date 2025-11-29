import re
list=["student123@gmail.com", "teacher.name@soa.edu", "abc.xyz@abc.in", "xyz#12@abc.com", "bad@1n.com"]
def filter_emails(list):
    pattern=r"^[a-zA-Z0-9][a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,4}$"
    f_list=[]
    for i in list:
        if re.match(pattern,i):
            f_list.append(i)
    return f_list

l=filter_emails(list)
print(l)