import sys

def ReplaceUnderscoreWithSpace(p_Kelime):
	liste = list(p_Kelime)
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

def main():
	kelime = raw_input("Bir Kelime Giriniz: ")
	yenikelime = ReplaceUnderscoreWithSpace(kelime)	
	print("eski kelime = " + kelime + "\nyeni kelime = " + yenikelime);

if __name__=='__main__':
	main()
