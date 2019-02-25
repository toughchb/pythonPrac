import sys
import time
from googletrans import Translator
translator = Translator()

#print("Please enter input text file name.")
#source = input().strip()

#fr = open("input.txt", 'r')
fr = open("input.txt", 'r', encoding='UTF8')

#fw = open("ouput.txt", 'w')
fw = open("ouput.txt", 'w', encoding='UTF8')
count =0;
while (count < 1000):
    time.sleep(0.05)
    r_line = fr.readline()
    if not r_line: break
    print(r_line)
    outline = translator.translate(r_line, src='en', dest='ko')
    print(outline.text)
    outline.text = outline.text + '\n'
    fw.write(r_line)
    fw.write(outline.text)
    count += 1


fr.close()
fw.close()