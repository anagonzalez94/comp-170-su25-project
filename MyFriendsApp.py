from Friend import Friend
from Birthday import Birthday

friendslist = []

def createFriend():
    firstName = input("First name: ")
    lastName = input("Last name: ")

# Main menu loop
def mainMenu():
    print("1 - Create new friend record")
    print("2 - Search for a friend")
    print("3 - Run reports")
    print("4 - Exit")
    selection = input("Enter your selection: ")

# Startup
if __name__ == "__main__":
    mainMenu()