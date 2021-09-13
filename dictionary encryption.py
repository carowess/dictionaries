encryptCode = {'a':'#', 'b':'!', 'c':'*', 'd':'$',
                'e':'@', 'f':'%', 'h':'^', 'i':'&',
                'j':'(', 'k':')', 'l':'-', 'm':'_',
                'n':'=', 'o':'+', 'q':'|', 'r':';',
                's':':', 't':'<', 'u':'>', 'v':'?',
                'w':'`', 'x':'~', 'y':'.', 'z:':','}

infile = open('info_security.txt', 'r')
outfile = open('new_info_security.txt', 'w')

file_material = infile.read()

for word in file_material:
    for letter in word.lower():
        text_encrypted = ''
        if letter in encryptCode:
            text_encrypted += str(encryptCode[letter])
            outfile.write(text_encrypted)
        else:
            text_encrypted += letter
            outfile.write(text_encrypted)