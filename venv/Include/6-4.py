#add fuctions to previous pracs

def main():
    speed_in_m=get_valid_number("speed in m")
    speed_in_km = convert_m_to_km(speed_in_m)
    speed_limit_in_km = get_valid_number("speed limit in km")
    fine = determine_fine(speed_in_km, speed_limit_in_km)
    print(fine)

def get_valid_number(string):
    speed=float(input(f"{string}"))
    print(speed)
    return speed
def convert_m_to_km(speed_in_m):
    speed_limit_in_km=speed_in_m/0.621371
    return speed_limit_in_km
def determine_fine(speed_in_km, speed_limit_in_km):
    over_speed=speed_in_km-speed_limit_in_km
    if 0<over_speed<=13:
        Penalty_amount=177
        Demerit_points=1
    elif 13<over_speed<=20:
        Penalty_amount=266
        Demerit_points=3
    elif 20<over_speed<=30:
        Penalty_amount=444
        Demerit_points=4
    elif 30<over_speed<=40:
        Penalty_amount=622
        Demerit_points=6
    else:
        Penalty_amount=1245
        Demerit_points=8

main()
