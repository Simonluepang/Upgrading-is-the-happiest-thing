import requests

def websocket_test(num):
	url = "http://192.168.13.195:8082/myluban/rest/qrcodelogin/qrcode"
	response = requests.get(url=url).json()
	token = response.get("data").get('token')
	url_wbs = "http://192.168.13.195:8082/myluban/loginpage/" + token
	# 普通HTTP地址链接升级为websocket链接，只需要在headers中传递一下参数，即可变为websocket
	# websocket是一个持久化的协议，也就是我们常说的长连接
	headers_wbs = {
			'Connection': 'Upgrade',
			'Upgrade': 'websocket',
			'Sec-WebSocket-Version': '13',
			'Sec-WebSocket-Key': '5/xaMEFuckEIYh'+ num +'MiAG+dg==',
			}
	response_wbs = requests.get(url=url_wbs, headers=headers_wbs)
	code = response_wbs.status_code
	if code == 101:
		pass
	else:
		raise Exception('长连接状态状态不正确')

if __name__ == '__main__':

	for i in range(3000):
		websocket_test(str(i))
		print(i)
