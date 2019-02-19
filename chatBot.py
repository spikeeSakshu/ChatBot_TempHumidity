# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:49:33 2019

@author: Spikee
"""


import random
import requests
import json

API_KEY="Your API KEY"
API_EndPoint="https://api.openweathermap.org/data/2.5/weather?zip=122413,in&APPID="


greeting_inputs=('hello','hi','greetings','sup',"what's up",'hey',)
greeting_responses=['hi','hey','*nods*','hi there','hello','I am glad! You are talking to me']


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)


def response():
    call=requests.get(API_EndPoint+API_KEY)
    
    data=json.loads(call.text)    
    temp=data['main']['temp']-273
    humidity=data['main']['humidity']
    print("Sure. The temp is ",round(temp,2),"Celcius","and the humidity is ",humidity,"%")
    
    
    return temp
def start():
    flag=True
    
    print("Welcome to Sakshu's ChatBot .....")
    
    while flag==True:
        user_response=input("... ")
        user_response=user_response.lower()
        
        if user_response!='bye':
            if (user_response is 'thanks' or user_response is 'thank you'):
                print('Welcome')
                
            else:
                if greeting(user_response)!= None:
                    print('ROBO:'+greeting(user_response))
                    
                else:
                    print("ROBO:",end=" ")
                    response()
                    
        else:
            flag=False
            print('ROBO: BYE!')
            
start()



