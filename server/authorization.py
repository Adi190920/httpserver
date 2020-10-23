from socket import *
import sys
import os
import datetime
from support_functions import *
from log_functions import *

#normally we have to read this from some file at the start of server
CHECK_AUTH = ["../var/www/html/", "../var/www/html/index.html"]


def authorize(dict1, client, addr, ROOT):
	#Here we need to check authorization but just checking if client has send the authorization then
	#assuming that its true
	if find_value("Authorization:", dict1) == None:
		return False
	else:
		 return True