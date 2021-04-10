import re
rule="[K][L]\d{2}[a-zA-Z]{2}\d{4}"
variable_name=input("ENTER ")
match=re.fullmatch(rule,variable_name)
if match==None:
    print("invalid")
else:
    print("valid")