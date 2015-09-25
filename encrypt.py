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
    if nr > high:
        while nr > high:
            nr -= nr
    elif nr < low:
        while nr < low:
            nr += nr
        
    #extra saftey measure
    if nr > high:
        nr = high
    elif nr < low:
        nr = low
    
    return

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
    
    keystring = ''
    
    for char in pw:
        #convert to unicode
        tmp_nr = ord(char) 
        #make number in range of capital english letters (65 - 90)
        make_nr_inrange(tmp_nr, low=65, high=90)
        #append nr to keystring
        keystring += str(tmp_nr)
    
    return keystring

def encrypt_pw(pw, seed=' '):
    """Encrypts a password and returns it 
    as a keystring
    """
    
    #get prime numbers
    prime_list = load_primes('prime_numbers_short.txt')
    
    #random primelist after seed
    random.seed(seed)
    prime_list = random.sample(prime_list, len(pw))
    
    keystring = make_keystring(prime_list, pw)
    
    return keystring
    
    
    
    
    