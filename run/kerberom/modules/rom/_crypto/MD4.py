# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <eddy (dot) maaalou (at) gmail (dot) com> wrote this file.  As long as you 
# retain this notice you can do whatever you want with this stuff. If we meet 
# some day, and you think this stuff is worth it, you can buy me a beer in 
# return.   Fist0urs
# ----------------------------------------------------------------------------

#!/usr/bin/python

# -*- coding: utf-8 -*-

# by Fist0urs

import hashlib

def new(*args):
    return hashlib.new('md4', *args)
