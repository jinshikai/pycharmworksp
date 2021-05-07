#coffee brew ratio
def test():
    print("test")
def get_coffee_style(yiel,dose):
   ratio=yiel/dose

   if 0.5<=ratio<1:
        return 'ristretto'
   elif 0.3<=ratio<0.5:
       return 'normale'
   else:
       return 'lungo'
def test_coffee():
    test()
    style=get_coffee_style(1,2)
    print(style)
    style=get_coffee_style(1,3)
    print(style)
    style=get_coffee_style(1,5)
    print(style)
test_coffee()