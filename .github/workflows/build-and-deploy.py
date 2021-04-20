# -*- coding: utf-8 -*-

import os,json,requests,traceback;

with open("./config.json", "r") as fp:
	users = json.load(fp);
	print(json.dumps(users));
	content = "";
	with open("./config.json", "r" , encoding="utf-8") as f:
		for line in f.readlines():
			content += line + "<br />";
	try:
		print(requests.post("https://www.pushplus.plus/send", data=json.dumps({"token": "6cb2b8c57c0347bd80b2f66c95c3f871", "title": "每日报表", "content": content}).encode(encoding="utf-8"), headers={"Content-Type": "application/json; charset=utf-8"}));
	except Exception as e:
		print('push+通知推送异常，原因为: ' + str(e));
		print(traceback.format_exc());
