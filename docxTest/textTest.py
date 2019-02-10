import sys

fr = open("input.txt",'r')
fw = open("ouput.txt",'w')

while True:
    r_line = fr.readline()
    print(type(r_line))
    print(r_line)
    if not r_line: break

    if r_line[-2:] != '.\n' :
        outline = r_line[:-1] + ' '
    else: outline = r_line
    fw.write(outline)

fr.close()
fw.close()