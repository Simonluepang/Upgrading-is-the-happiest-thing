from informationfunctions import InformationFunctions as IF
from time import sleep

def run_the_information():

	sleep(2)
	IF().upload_information()
	sleep(2)
	IF().information_management()
	print("\n>>>>>>>>资料已完成")