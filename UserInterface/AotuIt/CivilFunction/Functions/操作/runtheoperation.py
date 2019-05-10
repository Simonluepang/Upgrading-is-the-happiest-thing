from operationfunctions import OperationFunctions as OF
from time import sleep

def run_the_operation():

	sleep(2)
	OF().component_search()
	sleep(2)
	OF().export_the_qr_code()
	sleep(2)
	OF().add_node()
	sleep(2)
	OF().node_management()
	print("\n>>>>>>>>操作已完成")