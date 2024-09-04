#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:03:33 2024

@author: sanfins
"""

import pandas as pd
# Open and read the JSON file

fat = pd.read_json("dados.json")

contador = 0
valores = 0

for vendas in fat["valor"]:
    if vendas != 0:
        valores += vendas
        contador += 1
        
        
media = valores/contador
media = round(media,2)

print(fa"O valor médio das vendas no mês foi de R$ {media}")