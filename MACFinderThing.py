def SearchForMacAddress():
    UserInput = input("Enter part of the MAC address you want to search for: ")
    CheckUserInput(UserInput)
    SearchResults = "\n".join(x for x in DataList if UserInput in x)
    SearchArray = SearchResults.splitlines()
    print("*"*70)
    if len(SearchArray) == 1:
        Result = SearchArray[0]
        SeperatedResult = str.split(Result)
        FullName = ""
        for x in range(3, len(SeperatedResult)):
            FullName = FullName + SeperatedResult[x] + " "
        print("The partial MAC address " + UserInput + " is sold by " + FullName)
        SearchAgain()
    elif len(SearchArray) > 1:
        print("The partial MAC address containing " + UserInput + " is sold by one of these groups: ")
        for Result in SearchArray:
            SeperatedResult = str.split(Result)
            FullName = ""
            for x in range(3,len(SeperatedResult)):
                FullName = FullName + SeperatedResult[x] + " "
            print(SeperatedResult[0] + " ---------- " + FullName)
        SearchAgain()
    else:
        print("There are no MAC address matching your input of " + UserInput)
        SearchAgain()

def CheckUserInput(UserInput):
    CheckList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
                 "A", "B", "C", "D", "E", "F", ".", "-", ":",] 
    if len(UserInput) > 17: 
        print("*"*70)
        print("That is too long to be a MAC Address please try again")
        SearchForMacAddress()
    for Letter in UserInput: 
        if ("\n".join(x for x in CheckList if Letter in x)) == "":
            print("*"*70)
            print("You have entered an incorrect value for a MAC address please try again")
            SearchForMacAddress()

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
        sys.exit()

def GatherData():
    try: 
        import urllib.request
        Url = 'https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD' 
        Response = urllib.request.urlopen(Url)
        Data = Response.read()
        Text = Data.decode('utf-8')
        for Line in Text.splitlines():
            DataList.append(Line) 
        print("*"*70)
        SearchForMacAddress() 
    except urllib.error.URLError: 
        print("*"*70)
        print("Please check your connection to the internet then press any key to try again")
        input()
        SearchForMacAddress()

print("Loading......")
DataList = []
GatherData()
