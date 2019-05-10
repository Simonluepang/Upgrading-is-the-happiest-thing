from missionfunctions import MissionFunctions as MF1
from time import sleep

def run_the_mission():

	sleep(2)
	MF1().measure_point_management()
	sleep(2)
	MF1().setting()
	sleep(2)
	MF1().measure_report()
	print("\n>>>>>>>>任务完成")