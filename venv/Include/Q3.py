#coffee
i=True
while i:
    string=intput("black or white :").lower()
    size=intput("size? :").lower()
    cost=0
    if string=="black":
        if size=="small":
            cost=4
            break
        elif size=="midium":
            cost=5
            break
        elif size=="large":
            cost=6
        else:
            continue
    elif string=="white":
        if size=="small":
            cost=5
            break
        elif size=="midium":
            cost=6
            break
        elif size=="large":
            cost=7
            break
        else:
            continue
    else:
        continue

print(f"cost:{cost}")


