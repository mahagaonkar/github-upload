list = [70,70,70,20,30,70,50,60,40,50,40]

list.sort()
print(list)

for x in list:
    duplicates= list.count(x)
    print(f"{x} = {duplicates}")
    while duplicates > 1:
        list.remove(x)
        duplicates -= 1

print(list)