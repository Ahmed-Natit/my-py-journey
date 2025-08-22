while True:
    command = input(">")
    print("echo", command)
    if command.lower() == "quit":
        break
