# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:34:25 2024

@author: abdulbaki.karatepe
"""
#exo 7
def lpp(a,b):
    if a<b:
        return a
    else:
        return b
print(lpp(2.1,1.3))

#exo 8
def valeur_absolue(x):
    if x<0:
        x=x*-1
    else:
        return x
    return x
print(valeur_absolue(-5))

#exo 9
def est_entier(x):
    if x==int:
        return True
    else:
        return False
print(est_entier(2.8))

#exo 10
def est_pair(n):
    if n%2==0:
        return True
    else:
        return False
print(est_pair(13))

#exo 11
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

#exo 12
def signe(x):
    if x<0:
        return ("negatif")
    elif x>0:
        return ("positif")
print(signe(-5))

#exo 13
def est_bissextile(n):
    if n%400==0:
        return (n,"est s% bissextile")
    if n%100==0:
        return (n,"est pas bissextile")
    if n%4==0:
        return (n,"est bissextile")
print(est_bissextile(2000))
#exo 14
def seuil(eps):
    u = 1
    n = 0
    while (u > eps):
        u = u/(n+1)
        n = n+1
    return n

S = 0
for i in range(1, 10):
    S = S + i**2
print (S)
#exo 15
def somme_puissance_trois(n):
    S = 0
    for j in range(4,n):
        S = S+3**j
    return S
#exo 16
def somme_puissance(n,p):
    for i in range(1,n):
        n = n**p
    return n
#exo 17
    counter = 0
    for i in range(1,n):
        if i%7==0:
            counter+=1
    return counter
#exo 17
def mult_7_pas_3_5(n):
    counter = 0
    for i in range(1,n+1):
        if i%7==0 and (i%3!=0 and i%5!=0):
            counter +=1
    return counter
print(mult_7_pas_3_5(22))
#exo 18
def est_parfait(num):
     sum=0
     for i in range(1,num+1):
         if num % i==0:
             sum+=i
     return sum == 2*num
