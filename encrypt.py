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
            
    #extra saftey measure
    if nr > high:
        nr = high
    elif nr < low:
        nr = low
    
    return nr

def numbers_to_keystring(number_list):
    """turns a number into a char matching it's unicode value"""
    
    key_string = ''
    for nr in number_list:
        key_string += chr(nr)
    
    
    return key_string

def make_keystring(prime_list, pw):
    """Creates an encoded Capital_Letter key_string from a pw"""
    
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
    
    #container for finished key_string
    key_string = numbers_to_keystring(number_list)
    
    return key_string
    #return number_list

def make_keystring_v2(prime_list, pw):
    """Creates an numeric number_list that later
    is remade into a unicode char in a different
    way than v.1"""
    
    key_string = ''
    number_list = []
    
    #multiply unicode for each letter with matching prime_number (has same index)
    for i in range(0, len(pw)):
        tmp = pw[i]
        tmp_add = ord(tmp) * int(prime_list[i])
        #tmp_add -= prime_list[i+1]
        number_list.append(tmp_add)
    
    number_string = ''.join(map(str, number_list)) #make number_list into one long number_string
    #print(int(number_string))
    
    
    return number_list
    #return key_string

def encrypt_pw(pw, seed=' ', prime_start=1, key_string_method=2):
    """Encrypts a password and returns it 
    as a key_string
    """
    
    #get prime numbers
    tmp_prime_list = load_primes('TextFiles/prime_numbers_short.txt')
    
    #make a prime list starting at 'prime_start' (start at ex. the 100th prime_number)
    prime_list = []
    for i in range(prime_start, len(tmp_prime_list)):
        prime_list.append(tmp_prime_list[i])
    
    #random primelist after seed
    random.seed(seed)
    prime_list = random.sample(prime_list, len(pw))
    
    if key_string_method == 1:
        key_string = make_keystring(prime_list, pw)
    elif key_string_method == 2:
        key_string = make_keystring_v2(prime_list, pw)
    
    return key_string
    
    
    
    
    