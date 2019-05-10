import os

if __name__ == "__main__":
	pid = 620
	os.popen('taskkill.exe /pid:'+str(pid))
	os.popen('TASKKILL /F /IM QQ.exe')