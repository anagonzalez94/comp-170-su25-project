from Friend import Friend
from Birthday import Birthday

# ANSI values for prettier text
def red(text):
    return f"\x1b[91{text}\x1b[0m"
def blue(text):
    return f"\x1b[34m{text}\x1b[0m"
def magenta(text):
    return f"\x1b[95m{text}\x1b[0m"
def bold(text):
    return f"\x1b[1m{text}\x1b[21m"
def underlined(text):
    return f"\x1b[4m{text}\x1b[24m"

friendslist = []

#Fix later
#def loadFriendsList():
    #with open("friendslist.csv") as file:
        #for line in file

def createFriend():
    print(bold(f"Please enter the following information about your friend :)"))
    firstName = input("First name: ")
    lastName = input("Last name: ")
    friend = Friend(firstName, lastName)
    birthDay = input("Birth day: ")
    birthMonth = input("Birth month: ")
    friend.set_birthday(birthMonth, birthDay)
    friend.streetAddress = input("Street address: ")
    friend.city = input("City: ")
    friend.state = input("State (code): ")
    friend.zipCode = input("Zip code: ")
    friendslist.append(friend)

# Run reports menu
def runReports():
    print(underlined(f"\Reports Menu"))
    print("3.1 - List of friends alphabetically")
    print("3.2 - List of friends by upcoming birthdays")
    print("3.3 - Mailing labels for friends")
    print(red(f"3.9 - Return to previous menu"))
    reportSelect = input("Enter your selection: ")

# Main menu loop
def mainMenu():
    print(bold(f"Welcome to MyFriends!"))
    print(underlined(f"\nMain Menu"))
    print("1 - Create new friend record")
    print("2 - Search for a friend")
    print("3 - Run reports")
    print(red(f"4 - Exit"))
    selection = input("Enter your selection: ")

    if selection == "1":
        print("1.1 - Create new friend manually")
        print("1.2 - Load friends from CSV file")
        subSelection = input("Enter your selection: ")
        if subSelection == "1.1":
            createFriend()
        elif subSelection == "1.2":
            print("Still working on it")
        else:
            print(red(f"Invalid input. Try again!"))
    elif selection == "2":
        print("Searching for friend...")
    elif selection == "3":
        print("Reports Menu")
    else:
        print(red(f"Invalid input. Try again!"))

# Startup
if __name__ == "__main__":
    mainMenu()