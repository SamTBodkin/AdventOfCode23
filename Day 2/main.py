data = open('Day 2\Data.txt', 'r')

# only 12 red cubes, 13 green cubes, and 14 blue cubes
#Game 1: 6 green, 3 blue; 3 red, 1 green; 4 green, 3 red, 5 blue
cubeBagDict = {"green" : 13, "blue" : 14, "red" : 12}
Total = 0
for x in data:
    x = x.rstrip()
    gameState = True
    cubeDict = {"green" : 0, "blue" : 0, "red" : 0}

    game, dataRow = (x.split(":"))
    for dataSet in dataRow.split(";"):
        for x in dataSet.split(","):
            _ , value,key = x.split(" ")
            cubeDict[key] = int(value)

            if not all(cubeDict[key] <= cubeBagDict[key] for key in cubeDict):
                print("Unsuccessful Game")
                gameState = False
                break

    if gameState == True:
        Total += int(game.split(" ")[1])
print(Total)

