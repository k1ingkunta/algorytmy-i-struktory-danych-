def Top(stos):
    if stos[0] == None:
        print("pusts lista")
        return
    i = 0
    for x in stos:
        if x == None:
            break
        i+=1
    return stos[i - 1]
s1 = [None] * 200
s1[0] = 3
print(s1)

print(Top(s1))