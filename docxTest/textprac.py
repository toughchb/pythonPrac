import sys
from googletrans import Translator
translator = Translator()

fr = open("input.txt",'r')
fw = open("ouput.txt",'w')

while True:
    r_line = fr.readline()
    outline = translator.translate(r_line, src='en', dest='ko')
    print(type(r_line))
    print(r_line)
    if not r_line: break
    fw.write(outline.text)

fr.close()
fw.close()