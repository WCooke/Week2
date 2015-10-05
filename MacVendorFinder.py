usermac = input ("What is your Mac Address?")
import urllib2
response = urllib2.urlopen('https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD')
html = response.read()
