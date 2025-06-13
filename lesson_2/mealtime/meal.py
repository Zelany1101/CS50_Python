# 7:00-8:00 is breakfast
# 12:00-13:00 is lunch
# 18:00-19:00 is dinner

def main():
    time = input('What time is it? ')
    time = convert(time)

    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')
    else:
        pass

def convert(time):
    hour, second = time.split(':')
    second = int(second) / 60
    hour = int(hour)
    return hour + second


if __name__ == "__main__":
    main()
