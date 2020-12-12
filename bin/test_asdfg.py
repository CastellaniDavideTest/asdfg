"""Test asdfg file
"""
from asdfg import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-12-12"

def test():
	"""Tests the asdfg function in the asdfg class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert asdfg.asdfg() == "asdfg", "test failed"
	#assert asdfg.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
