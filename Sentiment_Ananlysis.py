#!/usr/bin/python3

import textblob
import os
import  webbrowser
#import random
from textblob import TextBlob
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen as ureq


#text to be taken as input from voice automation
text = '''
I am finally with my family today! Talked a lot with my parents. NOw feeling cool..
'''

blob = TextBlob(text)

for sentence in blob.sentences:
	print(sentence.sentiment.polarity)
	if sentence.sentiment.polarity>0.00 :
		print("Seems like u are happy today. I can make it a happier day for u..\n Choose any code from below.\n 1. Music\n2. Book/Novel\n3. Both\n")
		choice = input("Enter the code of your choice\n") 
		if choice== '1':
			webbrowser.open_new_tab('https://www.youtube.com/results?search_query= '+"cool fundo songs")            
		if choice== '2':
			webbrowser.open_new_tab('https://www.techsupportalert.com/free-ebooks-audio-books-read-online-download.htm')
		if choice== '3':
			webbrowser.open_new_tab('https://www.youtube.com/results?search_query= '+"cool fundo songs")            
			webbrowser.open_new_tab('https://www.techsupportalert.com/free-ebooks-audio-books-read-online-download.htm')


	elif sentence.sentiment.polarity<0.00 :
		print("i think u are sad today. Can i help u in someway?\n I can make your mood a little better one\n Type 'Y' for proceeding with me else type 'N'")
		choice = input ("Enter your choice here: ")
		if choice == 'Y':
			webbrowser.open_new_tab('https://www.youtube.com/watch?v=hGt_T6bCEMU')
	else :
		print("hey, is everything ok")

# will print about what exactly user wanna say 
print ("This text is about : ")

print (blob.noun_phrases)

# Open google link of the about the same 
for np in blob.noun_phrases:
	print (np)
	webbrowser.open_new_tab('https://www.google.com/search?q= ' + np)

