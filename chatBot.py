# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:49:33 2019

@author: Spikee
"""


import random

greeting_inputs=('hello','hi','greetings','sup',"what's up",'hey',)
greeting_responses=['hi','hey','*nods*','hi there','hello','I am glad! You are talking to me']


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)


def start():
    flag=True
    
    print("Welcome to Sakshu's ChatBot .....")
    
    while flag==True:
        user_response=input("...")
        user_response=user_response.lower()
        
        if user_response!='bye':
            if (user_response is 'Thanks' or user_response is 'Thank you'):
                flag =False
                
                print('Welcome')
                
            else:
                if greeting(user_response)!= None:
                    print('ROBO:'+greeting(user_response))
                    
                else:
                    print("ROBO: ",end=" ")
                    print(responses(user_response))
                    sent_tokens.remove(user_response)
            
        else:
            flag=False
            print('ROBO: BYE!')
            
start()