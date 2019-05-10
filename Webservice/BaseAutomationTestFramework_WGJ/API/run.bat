@echo START
python setup.py
pytest -s -q  TestCase\TestCase_Integration  -p no:warnings -n 2 --alluredir report
allure generate report\ -o report\html --clean
pause
