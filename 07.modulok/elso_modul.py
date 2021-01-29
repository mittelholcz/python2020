"""
pelda modul

tartalmaz par valtozot es fuggvenyt
"""

import string

text = 'alma, alma, piros alma'

def get_words():
    """visszater a text-ben levo szavak listajaval.
    """
    words = []
    for i in text.split():
        words.append(i.rstrip(string.punctuation))
    return words
