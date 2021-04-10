import re
pattern='a{2,3}'
match=re.finditer(pattern,"aaaaaaabaaaabaaaaba _ZK7@")
for matchs in match:
    print(matchs.start())
    print(matchs.group())


