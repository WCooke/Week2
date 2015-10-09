# This block of code opens the webpage that contains the list
# of MAC addresses and their vendors, downloads, and decodes the information
######################################
import urllib.request
Url = 'https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD'
Response = urllib.request.urlopen(Url)
Data = Response.read()
Text = Data.decode('utf-8')
######################################

# This section creates a list and then stores the decodes information
# line by line in that list
######################################
DataList = []
for Line in Text.splitlines():
    DataList.append(Line)
######################################

# This section performs the search on the list storing all the data
# it will also output the results of the search showing the MAC Address
# and the vendors short and long names
# After searching will check if user wants to perform another search if not
# the program closes
######################################   
while True:
    UserInput = input("Enter part of the MAC address you want to search for: ")
    
    SearchResults = "\n".join(x for x in DataList if UserInput in x)
    SearchArray = SearchResults.splitlines()
    TopResult = SearchArray[0]
    SeperatedTopResults = str.split(TopResult)

    FullName = ""
    for x in range(3, len(SeperatedTopResults)):
        FullName = FullName + SeperatedTopResults[x] + " "

    print("*"*60)
    print("The partial MAC address " + SeperatedTopResults[0] + " is sold by " + SeperatedTopResults[1])
    print("Otherwise known as: " + FullName)
    print("*"*60)

    UserInput = input("Would you like to search again? (y or n) ")
    if UserInput == "n":
       break
######################################
