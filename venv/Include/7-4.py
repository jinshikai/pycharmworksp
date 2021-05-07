 #BNIS
def calculate_bmi(height,weight):
     bmi=weight/height**2
     return bmi
def determine_weight_category(bmi):
    if bmi<18.5:
        return 'underweight'
    elif bmi<25:
        return 'normal'
    elif bmi<30:
        return 'overweight'
    else:
        return 'obese'
def main():
    for i in range(50,100):
        bmi=calculate_bmi(1.75,i)
        category=determine_weight_category(bmi)
        print(f"Height 1.75m, Weight {i}kg = BMI {bmi:.1f}, considered {category}")
        i+2
main()