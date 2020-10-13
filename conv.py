import re
a = open("raspis.json", "r", encoding='utf-8')
d = ['<?xml version="1.0" encoding="UTF-8" ?>', '<root>']
puti = ['root']
mass = 'ol' 
for i in a:
    match1 = re.match(r' *".*": {', i)
    match2 = re.match(r' *\[', i) 
    match3 = re.match(r' *".*":', i)
    match4 = re.match(r' *".*"', i)
    match5 = re.match(r' *]', i) 
    match6 = re.match(r' *}', i)
    if match1:
        match = match1[0][4*len(puti)+1:len(match1[0])-4:]
        puti.append(match)
        d.append(('    '*(len(puti)-1)) + '<'+ match + '>')
    elif match2:
        puti.append(mass)
        d.append(('    '*(len(puti)-1)) + '<'+ mass + '>')
    elif match3:
        k = len(match3[0])
        match = match3[0][4*len(puti)+1:len(match3[0])-2:]
        inf = ('    '*(len(puti))) + '<'+ match + '>' + i[k+2:i.rfind('"'):] + "</"+ match + '>'
        d.append(inf)
    elif match4:
        d.append(match4[0])
    elif match5:
        d.append(('    '*(len(puti)-1)) + "</" + str(puti[len(puti)-1]) + '>')
        puti.pop(len(puti)-1)
    elif match6:
        d.append(('    '*(len(puti)-1)) + "</" + str(puti[len(puti)-1]) + '>')
        puti.pop(len(puti)-1)

for i in d:
	print(i)
