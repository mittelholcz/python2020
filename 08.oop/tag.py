def get_text():
    print('Melyik fájlt elemezzük?')
    filename = input()
    if len(filename) > 0:
        f = open(filename, 'r')
        text = f.read()
        f.close()
    else:
        text = 'Kutya macska.'
    return text

def get_format():
    print('Milyen formátumú legyen az elemzés? xml vagy tsv?')
    valasz = input()
    return valasz

A = ['nagy', 'kicsi', 'piros']
N = ['kutya', 'macska', 'alma']
V = ['eszik', 'iszik']

def elemzo(text):
    text = text.lower()
    text = text.split()
    res = []
    for word in text:
        if word in A:
            res.append((word, 'A'))
        elif word in V:
            res.append((word, 'V'))
        elif word in N:
            res.append((word, 'N'))
        else:
            res.append((word, ''))
    return res

def kiiro(elemzett, formatum):
    if formatum == 'tsv':
        for word, pos in elemzett:
            if pos:
                print(word, pos, sep='\t')
            else:
                print(word, '-', sep='\t')
    elif formatum == 'xml':
        xml = []
        for word, pos in elemzett:
            #if len(i[1]) > 0:
            if pos:
                xml.append('<{1}>{0}</{1}>'.format(word, pos))
            else:
                xml.append(word)
        print(' '.join(xml))
    else:
        pass
