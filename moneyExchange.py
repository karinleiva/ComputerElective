#!/ user/bin/python
# -*- coding: iso-8859-15 -*-
# -*- coding: iso-4217 -*-
import os, sys

currency= raw_input("What is your currency?: (dollars/euros/yens)")
money = input ("Please insert your amount: ")
dollars = 0.00
euros= 0.00
yens = 0.00

if currency == "Dollar":
    euros = money * 0.92
    yens = money * 124.35
    print "Your $", money, "are: €", euros, "and ¥", yens 
    
elif currency == "Euro":
    dollars = money * 1.09
    yens = money * 135.39
    print "Your €", money, "are: $",dollars, "ane ¥", yens 
  
elif currency == "Yens":
    dollars = money * 0.0081
    euros = money * 0.0074
    print "Your ¥", money, "are: $", dollars, "and ¥", euros 
else :
    print "Select the correct currency, please try again"
