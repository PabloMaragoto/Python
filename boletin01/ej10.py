#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Pablo MD"

libras = float(input("Introduzca la cantidad de libras que quiera pasar a euros: "))

#1 libra = 1,10 euros

euros : float = round((libras * 1.10),2)

print(f"La cantidad de euros que recibe al convertir {libras} libras es de {euros} euros.")
