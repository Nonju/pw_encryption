#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import encrypt


#autorun
if __name__ == '__main__': 
    
    #username = input('Input your username: ')
    password = input('Input your password: ')
    seed = input('Enter a seed for your PW: ')
    
    #nr = encrypt.seed_test('')
    #print('nr:',nr)
    
    #enc_pw = encrypt.encrypt_pw('testPW', 'test')
    
    enc_pw = ''
    
    while True:
        selection = int(input('What encryption do you want to use? (1 or 2): '))
        
        if selection == 1:
            enc_pw = encrypt.encrypt_pw(password, seed, prime_start=50, key_string_method=selection)
            break
        elif selection == 2:
            enc_pw = encrypt.encrypt_pw(password, seed, prime_start=50, key_string_method=selection)
            break
        else:
            print('Chose one of the available selections')
        
    
    
    print('encrypted password:', enc_pw)

