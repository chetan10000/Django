import requests
import json
import os


ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = "C:\\Users\\chetan\\AppData\\Local\\Programs\\Python\\Python36\\Environment\\statusapp\\static\\status\\chetan\\l1.jpg"

def do(method='get' , data={} , id=4):
	r = requests.request(method , ENDPOINT +"?id=" + str(id) , data = data)
	print(r.text)
	return r
	
	
do()

def do_img(method = 'get' , data= {} , is_json=True , img_path= None):
	headers = {}
	if is_json:
		headers['content/type']='application/json'
		data = json.dumps(data)
	if img_path is not None:
		with open(image_path ,'rb') as image:
			file_data ={
							'image':image
							
							}
			r = requests.request(method ,ENDPOINT,  data=data , files=file_data , headers = headers)
	else:
		r = requests.request(method ,ENDPOINT,  data=data , headers=headers)
			
	print(r.text)
	print(r.status_code)
	return r
		
do_img(method='post' , data={'user':1 , "content":""},is_json=False , img_path = image_path)