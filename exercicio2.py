#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:40:19 2024

@author: sanfins
"""
#Sementes da sequência de Fibonacci

s0 = 0 
s1 = 1
s = 0
value = int(input("Conferir se este número pertence à sequência de Fibonacci: "))

while value > s:
    
    s = s1+s0
    s0 = s1
    s1 = s
    
    if value == s:
        print(f"{value} pertence à Fibonacci!")
    elif (value < s):
        print(f"{value} não pertence à Fibonacci!")
    