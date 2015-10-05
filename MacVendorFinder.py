usermac = input ("What is your Mac Address?")
import urllib.request
response = urllib.urlopen.urlsopen('https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD')
html = response.read()
