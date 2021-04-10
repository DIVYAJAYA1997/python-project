cricket={
    "AUS":{"rank":2,"rating":275,"points":6877},
    "NEW":{"rank":6,"rating":248,"points":6952},
   "SAF":{"rank":5,"rating":251,"points":5776},
    "PAK":{"rank":4,"rating":260,"points":8321},
    "IND":{"rank":3,"rating":268,"points":10186},
    "ENG":{"rank":1,"rating":275,"points":6877}

}
id=input("ENTER THE COUNTRY NAME: ")
prop=input("enter the detail want to know: ")
if id in cricket:
    print(cricket[id])
    if prop in cricket[id]:
        print(cricket[id][prop])
    else:
        print("INVALID")
else:
    print("invalid")
