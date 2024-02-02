#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

__author__ = "Pablo MD"

radio = float(input("Por favor, introduzca el radio de su circunferencia: "))

area : float = round((math.pi * math.pow(radio, 2)),3)
perimetro : float = round((2 * math.pi * radio),3)

print(f"Una circunferencia de radio {radio} tiene un área de {area} y un perimetro {perimetro}")