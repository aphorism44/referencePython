'''
Created on Nov 15, 2018

@author: domje
'''

carPrice = float(input("Please enter the base car price: "))
carTax = carPrice * .14
carLicense = carPrice * .024
carDealerPrep = 200.00

print("Base car price, plus tax and license: ", carPrice + carTax + carLicense)
print("With prep: ", carPrice + carTax + carLicense + carDealerPrep)