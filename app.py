command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car has been started")
    elif command == "stop":
        if started:
            print("Car has been stopped")
        else:
            print("Car already stopped!")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - for starting the car
stop - for stopping the car
quit - for quiting the program
        """)
    else:
        print("Sorry, invalid input")