from math import *
import time

## tak se ukaž vole! e na x numerickou metodou nekonečným rozvojem

def enax (x,presnost):
	vysledek = 0
	iterace = 0
	rozdil = inf
	while (rozdil > presnost):
		mezivysledek = (pow(x,iterace)/factorial(iterace))
		rozdil = mezivysledek
		vysledek = vysledek + mezivysledek
		iterace = iterace + 1
		'''
		print ("*********")
		print (iterace)
		print (mezivysledek)
		print (rozdil)
		print (vysledek)
		print ("*********")
		'''
	return vysledek

start = time.time()
vysledek = enax(10,0.00000001)
stop = time.time()
print (vysledek)
print ("Cas vypoctu: {} s".format(stop-start))	