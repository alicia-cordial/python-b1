def arrondis(listenote):
    listearrondies=[]
    for item in listenote:
        if  item % 5 == 3:
            item=item+2
        elif item % 5 == 4:
            item=item+1
        listearrondies.append(item)
    return listearrondies

print(arrondis([56, 84, 76, 55, 4]))