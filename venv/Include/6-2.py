 #parity
def displayparity(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

def getparity(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'

def odd(num):
    if num%2==0:
        return False
    else:
        return True

displayparity(2)
print(getparity(2))
print(odd(2))