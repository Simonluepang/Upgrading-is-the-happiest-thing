from datafunctions import DataFunctions as DF
from time import sleep

def run_the_data():

	sleep(2)
	DF().viewing_reports()
	sleep(2)
	DF().corresponding_output()
	print("\n>>>>>>>>数据已完成")