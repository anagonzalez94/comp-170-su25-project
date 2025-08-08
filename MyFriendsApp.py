from Friend import Friend
from Birthday import Birthday
import csv

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

# Load existing friend data on startup, reading CSV file to avoid manually inputting everything
def loadFriendsList():
    with open("friendslist.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            friend = Friend(row["firstName"],row["lastName"])
            friend.set_birthday(int(row["birthMonth"]),int(row["birthDay"]))
            friend.streetAddress(row["streetAddress"])
            friend.city(row["city"])
            friend.state(row["state"])
            friend.zipCode(row["zipCode"])
            friendslist.append(friend)

# Creates new friend
# Manual process for entering each value
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

# Loads friends from existing CSV
def loadFriendsCSV():
    filePath = input("Enter CSV file path you would like to use: ")
    with open(filePath, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            friend = Friend(row["firstName"], row["lastName"])
            friend.set_birthday(int(row["birthMonth"]),int(row["birthDay"]))
            friend.streetAddress(row["streetAddress"])
            friend.city(row["city"])
            friend.state(row["state"])
            friend.zipCode(row["zipCode"])
            friendslist.append(friend)
        print(blue("Loaded friends!"))

# Searches for friends by first name
# Edit or delete friend's profile
def searchFriend():
    searchName = input("Enter friend's first name: ").lower()
    for friend in friendslist:
        if friend.firstName.lower() == searchName:
            foundFriend = [f for f in friendslist if f.firstName.lower() == searchName]
            print(f"{friend.firstName} {friend.lastName} is your friend!")
            print(underlined("What would you like to do?"))
            print("1 - Edit friend profile")
            print("2 - Delete friend")
            print("3 - Return")
            searchSelect = input("Enter your selection: ")
            if searchSelect == "1":
                print("Working on it")
            elif searchSelect == "2":
                confirmation = input("Are you sure you want to delete this friend? (Y/N)")
                if confirmation == "Y":
                    friendslist.remove(foundFriend)
            else:
                print("Invalid input. Try again!")
                return

# Run reports menu
def runReports():
    while True:
        print(underlined(f"\Reports Menu"))
        print("3.1 - List of friends alphabetically")
        print("3.2 - List of friends by upcoming birthdays")
        print("3.3 - Mailing labels for friends")
        print(red(f"3.9 - Return to previous menu"))
        reportSelect = input("Enter your selection: ")
        if reportSelect == "3.1":
            friendsSorted = sorted(friendslist, key = lambda f: (f.lastName))
            for friend in friendsSorted:
                print(f"{friend.lastName}, {friend.firstName}")
        elif reportSelect == "3.2":
            birthdaysSorted = sorted(friendslist, key = lambda f: (f.birthday.days_until()))
            for friend in birthdaysSorted:
                print(f"{friend.firstName} {friend.lastName}'s birthday is on {friend.birthday}")
        elif reportSelect == "3.3":
            for friend in friendslist:
                print(f"{friend.firstName} {friend.lastName}'s address is {friend.streetAddress} {friend.city}, {friend.state} {friend.zipCode}")
        else:
            print("Returning to Main Menu")
            break

# Main menu loop
def mainMenu():
    while True:
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
                loadFriendsCSV()
            else:
                print(red(f"Invalid input. Try again!"))
        elif selection == "2":
            searchFriend()
        elif selection == "3":
            runReports()
        elif selection == "4":
            print("See you next time!")
            break
        else:
            print(red(f"Invalid input. Try again!"))

# Startup
if __name__ == "__main__":
    mainMenu()