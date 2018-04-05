#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colors import bcolors
from api import Selic

print bcolors.OKGREEN + "\n__________________________________________________\n"
print "# # # # # # # # " + bcolors.WARNING + "WELCOME TO PYNVEST" + bcolors.OKGREEN + " # # # # # # # #" 
print "__________________________________________________\n" + bcolors.ENDC

selic = Selic()

