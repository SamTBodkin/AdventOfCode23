data = open('Day 2\Data.txt', 'r')

# only 12 red cubes, 13 green cubes, and 14 blue cubes
#Game 1: 6 green, 3 blue; 3 red, 1 green; 4 green, 3 red, 5 blue
cubeBagDict = {"green" : 13, "blue" : 14, "red" : 12}
Total = 0
for x in data:
    gameState = True
    cubeDict = {"green" : 0, "blue" : 0, "red" : 0}
    x = x.rstrip()
    # Getting data extracted from the line 
    game, dataRow = (x.split(":"))
    print(game)
    dataRow = dataRow.split(";")
    print(dataRow)

    for x in dataRow:
        dataSet = x.split(";")
        for x in dataSet:
            cubes = x.split(",")
            for x in cubes:
                z , value,key = x.split(" ")
                cubeDict[key] = int(value)

            if((cubeDict["green"] <= cubeBagDict["green"]) & (cubeDict["red"] <= cubeBagDict["red"]) & (cubeDict["blue"] <= cubeBagDict["blue"])):
                print("Successful Game")
                pass
            else:
                print("Unsuccessful Game")
                gameState = False
    if gameState == True:
        Total += int(game.split(" ")[1])
print(Total)

