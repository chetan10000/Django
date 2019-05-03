import requests
import json

import os
AUTH_ENDPOINT="http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "/refresh"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = "C:\\Users\\chetan\\AppData\\Local\\Programs\\Python\\Python36\\Environment\\statusapp\\static\\status\\chetan\\l1.jpg"



headers = {
    "Content-Type":"application/json"
 
        }

data = {
    'username':'chetan',
    'password':'chetan1990'
    }

r = requests.post(AUTH_ENDPOINT, data = json.dumps(data) , headers=headers)
Token = r.json()['token']
JWT1= "JWT"+" "+ Token
print(JWT1)


### below methos is how to use JWT ###
headers1 = {
    "Content-Type" : "application/json",
    "Authorization" :  JWT1 ,
}
data1 = {
    
    "content":"new content"
}

post_data = json.dumps({"content":"hey "})
req_data = requests.post(ENDPOINT , data=post_data , headers=headers1)
print(req_data.text)





"""
def do(method='get' , data={} , id=4):
	r = requests.request(method , ENDPOINT +"?id=" + str(id) , data = data)
	print(r.text)
	return r
	
	
do()
"""

"""
#print(token)
refresh_data ={
  "token":Token
}

new_r = requests.post("http://127.0.0.1:8000/api/auth/jwt/refresh", data = json.dumps(refresh_data) , headers = headers)
Token2 = new_r.json()['token']
"""
