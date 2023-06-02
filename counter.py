def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    handle = open(file_name)

    days = dict()
    for line in handle:
        if line.startswith("From"):
            words = line.split()
            if len(words) > 2:
                day = words[2]
                days[day] = days.get(day,0) +1
                
    print(days)
## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
