import re
rule="[a-z]+@gmail.com"
pattern=input("ENTER THE MAIL ID:")
match=re.fullmatch(rule,pattern)
if match==None:
    print("INVALID")
else:
    print("VALID")