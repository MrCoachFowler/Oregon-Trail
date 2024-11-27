from random import randrange

wagon = {
    'food': 500,
    'milesTraveled': 0,
    'milesLeft': 2000,
    'wagonMembers': [] #first member is the leader
}

leaderName = input('what is the name of your leader?')
leaderDict = {
    'name': leaderName,
    'health': 5
}

wagon['wagonMembers'].append(leaderDict)

for i in range(4):
    memberName = input('what is the name of your ' + str(i + 1) + ' wagon member?')
    memberDict = {
        'name': memberName,
        'health': 5
    }
    wagon['wagonMembers'].append(memberDict)

for key, value in wagon.items():
    print(key + ": " + str(value))

def travel(wagon):
    moveDistance = randrange(30, 60)
    foodEaten = len(wagon['wagonMembers']) * 3
    wagon['milesTraveled'] += moveDistance
    wagon['milesLeft'] -= moveDistance
    wagon['food'] -= foodEaten

    for member in wagon['wagonMembers']:
        if randrange(1,100) < 20:
            member['health'] -= 1

travel(wagon)

for key, value in wagon.items():
    print(key + ": " + str(value))