command = ""
started = False
while command != 'quit':
    command = str(input(">").lower())
    if command == 'start':
        if not started:
            print("car is already started")
        print("you are ready to go.")
    elif command == 'stop':
        if started:
            print("car is already stopped")
        print("car has stopped!")
    elif command == 'help':
        print(''' start for start car
              stop for stop car
              help for hrlping
              quit to exit
              ''')
    else:
        print("game over")
print("close!")