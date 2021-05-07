#dog year

def calDogYears(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
        return  dog_years
    else:
        dog_years = 21 + 4 * (human_years - 2)
        return dog_years
def main():
    i=True
    while i:
        human_years=int(input("Enter human years:"))
        if human_years<0:
            print("end program")
            i=False
        else:
            dog_years = calDogYears(human_years)
            print(f"This dog is {dog_years} years old")
main()