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
numberDictionary = {}
t0 = time.time()

for i in range(1, len(lines)+1):
    numberDictionary[i] = 1

for line in lines:
    card_no, numbers = line.split(":")
    winning_numbers, user_numbers = numbers.split("|")
    PrintData(card_no, winning_numbers, user_numbers, False)
    # Add to array of lists for each type
    WinningNumbersArray.append(list(filter(None, (winning_numbers.rstrip().split(" ")))))
    UserNumbers.append(list(filter(None, (user_numbers.rstrip().split(" ")))))
    CardArray.append(card_no.split(" ")[-1])


for x, y, z in zip(WinningNumbersArray, UserNumbers, CardArray):
    CorrectNumbers = len(set(x) & set(y))
    if CorrectNumbers > 0 :
        #print(f"CorrectNumbers: {CorrectNumbers} for Card {z}")
        for num in range(int(z) + 1, int(z) + CorrectNumbers + 1):
            #print(f"Adding 1 to dictionary {num}")
            numberDictionary[int(num)] += numberDictionary[int(z)]


t1 = time.time()
totalTime = 1000 * (t1 - t0)
print(f"TotalResult = {sum(numberDictionary.values())}")
print(f"TotalTime {round(totalTime, 5)} milliseconds")





