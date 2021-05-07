#happy product
i=True
while i:
    choice=input("Menu:\n(I)nstructions\n(C)alculate\n(Q)uit")
    if choice=='I':
        print("Enter the number of products you want to buy and your chosen price")
        choice2=input("Menu:\n(I)nstructions\n(C)alculate\n(Q)uit")

        j=True
        while j:
            if choice2=="C":
                number=int(input("number of product :"))
                price=int(input("price of product "))
                if 0<number<5:
                    count=number*price
                    j=False
                else:
                    lowprice=price*0.9
                    count=lowprice*number
                    j=False
            else:
                print("error")
        i=False
    else:
        print("error")
print(f"{number}*{price}={count}")




