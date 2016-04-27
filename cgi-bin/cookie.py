#!/usr/bin/env python3
# set cookies if they are absent
import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
if name is None:
    print("Set-cookie: name=value")
    print("Content-type: text/html\n")
    print("Cookies!!!")
else:
    print("Content-type: text/html\n")
    print("Cookies:")
    print(name.value)

'''
# simple cookie
print("Set-cookie: name=value; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly")

print("Content-type: text/html\n")
print("Cookies!!!")


# or delete optional parameters
print("Set-cookie: name=value")

print("Content-type: text/html\n")
print("Cookies!!!")
'''
