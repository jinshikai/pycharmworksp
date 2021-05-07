#bill calculator
meal_amount=float(input("Enter meal amount($):"))
discount_meal_amount=meal_amount*0.50
service_charge=discount_meal_amount*0.10
gst=(discount_meal_amount+service_charge)*0.07
total=gst+service_charge+discount_meal_amount
print(" ")
print("Receipt")
print("cost of meal : $%.2f"%meal_amount)
print("50% discount ${:.2f} ".format(discount_meal_amount))
print("service charge ${:.2f} ".format(service_charge))
print("GST ${:.2f} ".format(gst))
print("total amount ${:.2f} ".format(total))

