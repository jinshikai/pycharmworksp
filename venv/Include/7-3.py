 #seconds display
def convertSeconds(seconds):
    min=int(seconds/60)
    last_second=seconds-(min*60)
    print(f"{seconds} seconds is {min}m {last_second}s")
def main():
    while True:
        seconds=int(input("Enter seconds"))
        if seconds<0:
            break
        else:
            convertSeconds(seconds)
main()