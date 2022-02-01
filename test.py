#!/usr/bin/env python
# coding: utf-8

# <p><font size="6"><b>Examen Versionning de code et Programmation Python: Implémentation de fonction mathématiques et intégration à Github</b></font></p>
# 
# 
# > 
# 
# 
# 
# ---

# In[59]:


import numpy as np
def Polynome(list,value):
    return(np.polyval(list,value ))


# In[60]:


list = [1, -1.5, -6, 5]
Polynome(list,5)


# Implémenter la fonction factorielle (Approche récursive ou classique)

# In[66]:


def factorielle(n):
    if n == 1:
        return n
    else:
        return n * factorielle(n - 1)
# Demande à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre: "))
if n < 0:
    print("Factoriel ne peut être trouvé pour les nombres négatifs")
elif n == 0:
    print("Factorielle de 0 est 1")
else:
    print("Factorielle de", n, "est: ", factorielle(n))

    


# Implémenter la suite de Fibonnaci

# In[65]:


entre = int(input("Entrez un nombre: "))
v1 = 0
v2 = 1
print("\n la suite fibonacci est :")
print(v1, ",", v2, end=", ")
 
for i in range(2, entre):
  suivant = v1 + v2
  print(suivant, end=", ")
 
  v1 = v2
  v2 = suivant


# In[77]:


#Création de fonction comportant des modules de gestions des exceptions 
from math import *

def factor():
    while True:
            try:
                
                a=input("Entrer la valeur de a ?")
            
                if('j' in a):
                     print("nombre valide, ce n'est pas complex")
                
                   a=float(a)
            except ValueError:
                if(type(a)==str):
                     print("nombre valide, ce n'est pas Srting")
                    
                print("Entrer un entier ou un float")
                continue
                  if  0.5 <= a <= 100 :
                break
                  elif 0.5 <= a < 0.5 :
                print ("entrez un grand nombre")
                  elif a < 0 :
                print ("entrez un nombre positif")
                  elif a > 100 :
                print ("entrez un petit nombre")
                  elif a == 1 :
                return a
                  else 
                return a * factorielle(a - 1)     
   


# In[63]:


#Question Bonus : Implémentation de la formule Pricer d’option avec Python
from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np


def d1(S,X,T,r,sigma):
    return(log(S/X)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))
def d2(S,X,T,r,sigma):
    return d1(S,X,T,r,sigma)-sigma*sqrt(T)


# In[64]:


def relation_C(S,X,T,r,sigma):
    return S*norm.cdf(d1(S,X,T,r,sigma))-X*exp(-r*T)*norm.cdf(d2(S,X,T,r,sigma))
  
def relation_p(S,X,T,r,sigma):
    return X*exp(-r*T)-S+bs_call(S,X,T,r,sigma)


# In[ ]:




