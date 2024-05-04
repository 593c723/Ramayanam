import pandas as pd
import re
import nltk
from nltk import Text
from unidecode import unidecode
import path
import sys

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent.parent)

def sys_path():
    return sys.path

def get_char_list():
    #would have been better to use the above option- manual cleaning is disgraceful
    not_nouns = ['air', 'beauty', 'buddhist', 'cancer', 'fame', 'fate', 'fire', 'fortune', 'glory', 'honour', 'java', 'justice', 'passim', 'lava', 'modesty', 'ocean', 'rain', 'right', 'thunderer', 'trident', 'virtue', 'wind', 'moon', 'sun']
    # refer text_pre_proc ipynb
    
    ch = open("data/txt/chars.txt", 'r+', encoding='utf-8')
    # ch = open("../data/txt/chars.txt", 'r+', encoding='utf-8')
    chs = ch.readlines()
    c_list = []
    characters = []
    for line in chs:
        line = line.strip().replace(".", "")
        components = line.split(",")
        charac = components[0]
        occ = components[1:]
        if (bool(re.search('[0-9]+', charac)) == False) and (charac != ""):
            characters.append(charac)
        c_list.append({ "Character": components[0], "Occurences" : occ})
    characters = [c.lower() for c in characters]
    pn = [word for word in characters if (word not in not_nouns)] # proper-nouns; hopefully:')

    return (pn, not_nouns, characters)

#use english dict from nltk or smthn to filter out words[form a new list] of english words like- fortune, virtue, fame
#Go through the rest and separate location/places (maybe use a ml model for this?
#  - will need to be unsupervised, and will need to pick out location reference in text
# (mythical, so no models pre-trained on other data))

def nltk_text():
    p = open("../data/txt/proc.txt", 'r', encoding='utf-8')
    text = p.readlines()
    tx = open("../data/txt/d.txt", 'r', encoding = 'utf-8')
    txt = tx.readlines()
    orig_text = ""
    for t in txt:
        orig_text += unidecode(t.lower())

    tokzr = nltk.tokenize.WhitespaceTokenizer()
    T_orig = Text(tokzr.tokenize(orig_text)) #from original text
    T_proc = Text(tokzr.tokenize("".join(text))) #from processed text
    
    return (text, T_orig, T_proc)
    #returns list of len 1 - processed string; Text : Processed and original

def boot(): #book to text
    file = open("data/txt/d.txt", 'r', encoding = 'utf-8')
    # file = open("../data/txt/d.txt", 'r', encoding = 'utf-8')
    books = {}
    i = 0
    curr_boo = []
    while True:
        data = file.readline()
        if not data:
            break
        if data[:4] != 'BOOK':
            # data = re.sub("'s", "", data)
            curr_boo.append(data.strip())
        else:
            books['BOOK ' + str(i)] = " ".join(curr_boo)
            i += 1
            curr_boo = []
    books['BOOK ' + str(i)] = "".join(curr_boo)
    return books

def books_to_chaps(): #book to chapters map
    f = open('data/txt/chaps.txt', 'r', encoding = 'utf-8')
    # f = open('../data/txt/chaps.txt', 'r', encoding = 'utf-8')
    d = f.readlines()
    b_c = {}
    c_li = []
    b_name = "book"
    for x in d:
        if x.strip()[:4].lower() != "book":
            c_li.append(x.strip())
        else:
            b_c[b_name] = c_li
            b_name = x.strip()
            c_li = []
    b_c[b_name] = c_li
    b_c['BOOK VI.'] = b_c['BOOK VI.'][:-1]
    b_c['BOOK VI.'].append('Canto CXXX. The Consecration.')
    return b_c #dict_keys(['book', 'Book I.', 'BOOK II.', 'BOOK III.', 'BOOK IV.', 'BOOK V.', 'BOOK VI.'])


def get_all_chaps():
    # df = pd.read_csv("src/streamlit_data/c_b_t.csv", encoding = 'utf-8')
    df = pd.read_csv('data/csv/c_b_t.csv')
    all_chaps = df["Chapter"].to_list()
    return all_chaps