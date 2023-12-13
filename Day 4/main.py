import time
def PrintData(card_no, winning_numbers, user_numbers, Active):
    if Active == True:
        print(f"card = {card_no}")
        print(f"winningNumbers = {winning_numbers}")
        print(f"userNumbers = {user_numbers}\n")



with open('Day 4\Data.txt', 'r') as data:
    lines = data.readlines()

# Format the data into CardNo, Winning Numbers, UserNumbers
CardArray = []
WinningNumbersArray = []
UserNumbers = []
CorrectNumbers = 0
Result = 0
TotalResult = 0

t0 = time.time()

for line in lines:
    card_no, numbers = line.split(":")
    winning_numbers, user_numbers = numbers.split("|")
    PrintData(card_no, winning_numbers, user_numbers, False)
    # Add to array of lists for each type
    WinningNumbersArray.append(list(filter(None, (winning_numbers.rstrip().split(" ")))))
    UserNumbers.append(list(filter(None, (user_numbers.rstrip().split(" ")))))

for x, y in zip(WinningNumbersArray, UserNumbers):
    CorrectNumbers = len(set(x) & set(y))
    if CorrectNumbers > 0:
        Result = 2 ** (CorrectNumbers - 1)
    else:
        Result = 0
    #print(f"Result of Card {Result}\n")
    TotalResult += Result

t1 = time.time()
totalTime = 1000 * (t1 - t0)
print(f"TotalResult = {TotalResult}")
print(f"TotalTime {round(totalTime, 5)} milliseconds")





