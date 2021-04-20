# -*- coding: utf-8 -*-

import os,json;

with open('./config.json','r') as fp:
	users = json.load(fp);
	print(json.dumps(users));
