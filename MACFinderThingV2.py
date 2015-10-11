# Searches the Data list based on what a user inputs and then outputs the results of that search
def SearchForMacAddress():
    UserInput = input("Enter part of the MAC address you want to search for: ")
    CheckUserInput(UserInput)
    SearchResults = "\n".join(x for x in DataList if UserInput in x) # Searches through the Data List for any parts of each line that match what the user input
    SearchArray = SearchResults.splitlines()    # turns the results of the search into a array/list
    print("*"*70)
    if len(SearchArray) == 1: # if there is only one element in the list
        Result = SearchArray[0] # the single result is placed in a string
        SeperatedResult = str.split(Result) # the string is then split based upon white space/ spaces and placed in a list (SeperatedResult)
        FullName = "" # creates a string variable
        for x in range(3, len(SeperatedResult)): # the for loop counts from the 3rd value in the string list up to the total number of elements in the SeperatedResult list
            FullName = FullName + SeperatedResult[x] + " " # each part of the string list is then placed in a single string FullName
        print("The partial MAC address " + UserInput + " is sold by " + FullName)
        SearchAgain()
    elif len(SearchArray) > 1: # if the search produces several possible results
        print("The partial MAC address containing " + UserInput + " is sold by one of these groups: ")
        for Result in SearchArray: # goes through each result of the search line by line
            SeperatedResult = str.split(Result) # the result is split up into a list (SeperatedResult) based on white space/ spaces
            FullName = ""
            for x in range(3,len(SeperatedResult)):
                FullName = FullName + SeperatedResult[x] + " "
            print(SeperatedResult[0] + " ---------- " + FullName)
        SearchAgain()
    else: # if the search produces no results
        print("There are no MAC address matching your input of " + UserInput)
        SearchAgain()

# Checks what the user input to see if its at least part of a MAC address 
def CheckUserInput(UserInput):
    CheckList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
                 "A", "B", "C", "D", "E", "F", ".", "-", ":",] # list containing all possible characters of a MAC address
    if len(UserInput) > 17: # if the user input a string that was bigger than 17 characters then its almost certain that it wasnt a MAC address
        print("*"*70)
        print("That is too long to be a MAC Address please try again")
        SearchForMacAddress()
    for Letter in UserInput: # goes through each charater that the User Input
        if ("\n".join(x for x in CheckList if Letter in x)) == "": # Compares what the user input to the list of possible charaters
            print("*"*70)
            print("You have entered an incorrect value for a MAC address please try again")
            SearchForMacAddress()

# Runs at the end of each search in case the user wants to search again without rerunning the program
def SearchAgain():
    print("*"*70)
    UserInput = input("Would you like to search again? (y or n) ")
    if UserInput == "y":
        print("*"*70)
        SearchForMacAddress()
    elif UserInput != "n":
        print("*"*70)
        print("Please only enter either a y or an n")
        SearchAgain()
    elif UserInput == "n":
        import sys
        sys.exit() # if the user choses "n" then the program closes

# Takes the required data from a website and places that data into a list
def GatherData():
    try:    # As the program will error if there is no connection to website this will catch that error and provides some simple handling for it
        import urllib.request
        Url = 'https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD' # The URL all the data is downloaded 
        Response = urllib.request.urlopen(Url) # Opens the URL
        Data = Response.read() # Draws the data from the URL
        Text = Data.decode('utf-8') # Turns the data into a readable string format
        for Line in Text.splitlines():
            DataList.append(Line) # goes through the data line by line and adds it to the Global list
        print("*"*70)
        SearchForMacAddress() 
    except urllib.error.URLError: # The error if there is no connection
        print("*"*70)
        print("Please check your connection to the internet then press any key to try again")
        input()
        SearchForMacAddress()

# The Program starts here
print("Loading......")
DataList = [] # Global Variable to store all MAC Addresses and vendors in
GatherData()
