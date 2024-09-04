#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:38:23 2024

@author: sanfins

"""


data = [["SP","RJ","MG","ES","Outros"],[67836.43, 36678.66, 29229.88, 27165.48, 19849.53]]

total = 0

for valor in data[1]:
    total += valor

for i in range(5):
    print(f"O estado de {data[0][i]} teve uma representação de {round(100*data[1][i]/total, 2)}%")
