#repetition2
low=int(input("low value:"))
high=int(input("high value:"))
sum=0
for i in range(low,high+1):
    print(i,end="")
    sum=i+sum
print(" ")
print(f"sum:{sum}")
