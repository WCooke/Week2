usermac = input ("What is your Mac Address?")
import urllib.request

data = urllib.request.urlretrieve("https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD", "list.txt")

print (data)
