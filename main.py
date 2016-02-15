import time

# Environment
# Set bounds for elevator car's travel
floors_accessible = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cars = [1]

# State
# Elevator car starts at the ground floor and is not in motion
car_pos = floors_accessible[0]
direction = 0 # 0: not moving, 1: up, 2: down

# Setup
dir = 0
floor_from = 0
floor_to = 0

# Store instructions
queue = []

def updateQueue():
    print(queue)

def checkDoors():
    doors_closed = raw_input('Doors closed? (T/F): ')

    if doors_closed == "T":
        return True
    else:
        print("Doors not closed. Please close.")
        checkDoors()

def hasStops():
    has_stops = raw_input("Any more stops? (T/F): ")

def moveCar(dir, floor_from, floor_to):
    if checkDoors() == True:
        print("Car traveling %s from floor %s to floor %s" % (dir, floor_from, floor_to))

        if hasStops() == True:
            callElevator()
        else:
            updateQueue()

    else:
        checkDoors()

def carCurrentPos():
    car_pos = currentFloor

def getCarPos(car_pos):
    return car_pos

def addDirection():
    dir = raw_input('Up (1) or Down (2)?: ')

    getCurrentFloor(dir)

def getCurrentFloor(dir):
    floor_from = raw_input('From what floor?: ')

    addToQueue(dir, floor_from)

def addToQueue(dir, floor):
    floor_to = raw_input('To what floor?: ')

    queue.append([dir, floor_from, floor_to])

    print('The queue has been updated to: ', queue)

    moveCar(dir, floor_from, floor_to)

def callElevator():
    addDirection()

callElevator()

