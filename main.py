#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import encrypt




#autorun
if __name__ == '__main__': 
    
    #username = input('Input your username: ')
    password = input('Input your password: ')
    
    #nr = encrypt.seed_test('')
    #print('nr:',nr)
    
    #enc_pw = encrypt.encrypt_pw('testPW', 'test')
    enc_pw = encrypt.encrypt_pw(password, 'seed')
    
    print('encrypted password:', enc_pw)

