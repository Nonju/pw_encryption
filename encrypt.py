#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random #muy importante

def test():
    "test function to see if shit's working or not"
    
    print('hello, this is working')
    
def seed_test(seed):
    
    random.seed(seed) #makes nr the same every time
    nr = random.randrange(10) #generates single number
    return nr
    
#serious shit below

def make_nr_inrange(nr, low=0, high=1):
    """Makes a number fit a certain interval"""
    
    #sets number in interval_range
    while True:
        if nr > high:
            nr -= high
        elif nr < low:
            nr += low
        #else: #number is in range
            #break
        if nr < high and nr > low: #number is in range
            break
            
    """            
    if nr > high:
        while nr > high:
            nr -= high
    if nr < low:
        while nr < low:
            nr += low
   """ 
    #extra saftey measure
    if nr > high:
        nr = high
    elif nr < low:
        nr = low
    
    return nr

#def #turn keystring into capital_letters
def numbers_to_keystring(number_list):
    pass

def load_primes(filename):
    """loads prime_numbers from a txt-file
    meant to load all primes every single 
    time to make encryption slower --> 
    slower to breach
    """
    
    prime_list = []
    with open(filename) as f:
        tmp_list = []
        for line in f:
            tmp_list = line.split()
            for nr in tmp_list:
                prime_list.append(nr)
        
    return prime_list

def make_keystring(prime_list, pw):
    """Creates a encoded keystring from a pw"""
    
    number_list = [] #container for generated numbers
    for char in pw:
        #convert char to unicode
        tmp_nr = ord(char)
        
        #get index of char, multiply tmp_nr by the
        #entry in prime_list that has that index
        combined_nr = tmp_nr * int(prime_list[pw.index(char)])
        
        #make number in range of capital english letters (65 - 90)
        combined_nr = make_nr_inrange(combined_nr, low=65, high=90)
        
        #append nr to number_list
        number_list.append(combined_nr)
    
    
    key_string = '' #container for finished key_string
    key_string = numbers_to_keystring(number_list)
    
    #return key_string
    return number_list

def encrypt_pw(pw, seed=' '):
    """Encrypts a password and returns it 
    as a keystring
    """
    
    #get prime numbers
    prime_list = load_primes('TextFiles/prime_numbers_short.txt')
    
    #random primelist after seed
    random.seed(seed)
    prime_list = random.sample(prime_list, len(pw))
    
    keystring = make_keystring(prime_list, pw)
    
    return keystring
    
    
    
    
    