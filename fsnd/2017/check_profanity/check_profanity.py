import os
import errno

def file_picker():
	file_path = raw_input("Please enter the file to check: ")
	file_path = str(file_path)
	print("Attempting to open file: "+file_path)
	try:
		file = open(file_path,"r") #open file for 'r' READing
	except IOError as e:
		if e.errno == errno.ENOENT:
			return "unusable input"
		raise
	else: 
		return file

def check_profanity(file):
	data = {}
	profane = 1
	list_profanity = ['shit','fuck','ass']
	for LineNumber, Line in enumerate(iter(file.readline, b'')):
		for WordNumber, Word in enumerate(Line.split()):
			Word = Word.strip(".,;:")
			for swear in list_profanity:
				if Word.lower() == swear:
					print("LINE: "+str(LineNumber)+
						" WORD: "+str(WordNumber)+
						" <"+Word+
						"> is most profane!!")
					profane = 0
	if(profane):
		print("Good Job! You responded without swearing!")

def main():
	file=file_picker()
	check_profanity(file)

main()