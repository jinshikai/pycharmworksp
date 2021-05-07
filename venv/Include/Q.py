#coffee
string=intput("black or white :").lower()
size=intput("size? :").lower()
cost=0
if string=="black":
    if size=="small":
        cost=4
    elif size=="midium":
        cost=5
    elif size=="large":
        cost=6
    else:
        cost=6
elif string=="white":
    if size=="small":
        cost=5
    elif size=="midium":
        cost=6
    elif size=="large":
        cost=7
    else:
        cost=7
else:
    if size=="small":
        cost=5
    elif size=="midium":
        cost=6
    elif size=="large":
        cost=7
    else:
        cost=7

print(f"cost:{cost}")


