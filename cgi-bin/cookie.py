#!/usr/bin/env python3

# simple cookie
print("Set-cookie: name=value; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly")

print("Content-type: text/html\n")
print("Cookies!!!")

'''
# or delete optional parameters
print("Set-cookie: name=value")

print("Content-type: text/html\n")
print("Cookies!!!")
'''
