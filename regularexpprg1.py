import re
var=input("ENTER THE NUM:")
rule="[7-9][0-9]{9}"
match=re.fullmatch(rule,var)
if match==None:
    print(" INVALID")
else:
    print(" VALID")

