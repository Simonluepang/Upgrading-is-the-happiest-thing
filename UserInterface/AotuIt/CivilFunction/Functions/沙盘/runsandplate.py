from patternfunctions import PattrenFuncitons as PF1
from statusfunctions import StatusFunctions as SF
from monitoringfunctions import MonitoringFunctions as MF
from cockpitfunctions import CockpitFunctions as CF
from time import sleep


def run_sand_plate():

	sleep(20)
	PF1().sand_table_pattern()
	print("\n>>>>>>>>工作集已完成")
	sleep(2)
	PF1().project_time()
	print("\n>>>>>>>>沙盘模式已完成")
	sleep(2)
	SF().status_manage()
	sleep(5)
	SF().define_status()
	sleep(5)
	SF().format_painter()
	sleep(5)
	SF().statistics_panel()
	sleep(2)
	SF().state_statistics()
	sleep(2)
	SF().refresh_data()
	sleep(2)
	print("\n>>>>>>>>沙盘状态已完成")
	MF().add_monitor()
	sleep(2)
	MF().monitor_management()
	sleep(2)
	MF().service_setting()
	sleep(2)
	MF().monitoring_panel()
	sleep(2)
	print("\n>>>>>>>>监控已完成")
	CF().sand_table_cockpit()
	sleep(2)
	CF().upload_picture()
	print("\n>>>>>>>>驾驶舱及总进度图已完成")

