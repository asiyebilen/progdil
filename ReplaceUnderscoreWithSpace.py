import sys

def ReplaceUnderscoreWithSpace(p_Dil):
	liste = list(p_Dil)
	newstr = ""
	for i in range(len(liste)):
		if i == 0:
			newstr = liste[i]
			continue
		elif i == (len(liste)-1):
			newstr = newstr + liste[i]
			continue
		elif liste[i] == "_":
			newstr = newstr + " "
		else:
			newstr = newstr + liste[i]
	return newstr

if __name__=='__main__':
	kelime = raw_input("Bir Kelime Giriniz: ")
	yenikelime = ReplaceUnderscoreWithSpace(kelime)	
	print("eski kelime = " + kelime + "\nyeni kelime = " + yenikelime);