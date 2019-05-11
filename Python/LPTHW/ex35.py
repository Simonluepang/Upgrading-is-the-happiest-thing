#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        pass