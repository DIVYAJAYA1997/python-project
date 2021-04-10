import re
pattern='[a-zA-Z]'
match=re.finditer(pattern,"abc_Z7K@")
for matchs in match:
    print(matchs.start())
    print(matchs.group())