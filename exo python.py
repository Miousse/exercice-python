# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:34:25 2024

@author: abdulbaki.karatepe
"""

def lpp(a,b):
    if a<b:
        return a
    else:
        return b
print(lpp(2.1,1.3))


def valeur_absolue(x):
    if x<0:
        x=x*-1
    else:
        return x
    return x
print(valeur_absolue(-5))


def est_entier(x):
    if x==int:
        return True
    else:
        return False
print(est_entier(2.8))


def est_pair(n):
    if n%2==0:
        return True
    else:
        return False
print(est_pair(13))


def intervalle1(x):
    if -2<x<=3:
        return True
    else:
        return False
print(intervalle1(1))



def intervalle2(x):
    if x<=-3 or x>=5:
        return True
    else:
        return False
print(intervalle2(1))


def intervalle3(x):
    if -5<x<=-3 or 0<=x<2:
        return True
    else:
        return False
print(intervalle3(667))


def intervalle4(x):
    if x>1:
        return True
    else:
        return False
print(intervalle4(2))


def signe(x):
    if x<0:
        return ("negatif")
    elif x>0:
        return ("positif")
print(signe(-5))


def est_bissextile(n):
    if n%400==0:
        return (n,"est s% bissextile")
    if n%100==0:
        return (n,"est pas bissextile")
    if n%4==0:
        return (n,"est bissextile")
print(est_bissextile(2000))