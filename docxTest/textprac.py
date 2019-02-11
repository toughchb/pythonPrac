import sys
from googletrans import Translator
translator = Translator()

print("Please enter input text file name.")
source = input().strip()

fr = open( source + ".txt",'r', encoding='UTF8')
fw = open("ouput.txt",'w', encoding='UTF8')

while True:
    r_line = fr.readline()
    if not r_line: break
    #print(r_line)
    outline = translator.translate(r_line, src='en', dest='ko')
    #print(outline.text)
    outline.text = outline.text + '\n'
    fw.write(r_line)
    fw.write(outline.text)


fr.close()
fw.close()