import pandas as pd
import re
import nltk
from nltk import Text
from unidecode import unidecode
import path
import sys
from modules import Data_pre_proc

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent.parent)

def sys_path():
    return sys.path

def get_char_list():
    #would have been better to use the above option- manual cleaning is disgraceful
    not_nouns = ['air', 'beauty', 'buddhist', 'cancer', 'fame', 'fate', 'fire', 'fortune', 'glory', 'honour', 'java', 'justice', 'passim', 'lava', 'modesty', 'ocean', 'rain', 'right', 'thunderer', 'trident', 'virtue', 'wind', 'moon', 'sun']
    # refer text_pre_proc ipynb
    try:
        ch = open("data/txt/chars.txt", 'r+', encoding='utf-8')
    except:
        ch = open("../data/txt/chars.txt", 'r+', encoding='utf-8')
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
    pn = [word for word in characters if (word not in not_nouns)]

    ch.close()

    return (pn, not_nouns, characters)

#use english dict from nltk or smthn to filter out words[form a new list] of english words like- fortune, virtue, fame
#Go through the rest and separate location/places (maybe use a ml model for this?
#  - will need to be unsupervised, and will need to pick out location reference in text
# (mythical, so no models pre-trained on other data))

def nltk_text():
    try:
        p = open("data/txt/proc.txt", 'r', encoding='utf-8')
    except:
        p = open("../data/txt/proc.txt", 'r', encoding='utf-8')
    text = p.readlines()
    try:
        tx = open("data/txt/d.txt", 'r', encoding = 'utf-8')
    except:
        tx = open("../data/txt/d.txt", 'r', encoding = 'utf-8')
    txt = tx.readlines()
    orig_text = ""
    for t in txt:
        orig_text += unidecode(t.lower())

    tokzr = nltk.tokenize.WhitespaceTokenizer()
    T_orig = Text(tokzr.tokenize(orig_text)) #from original text
    T_proc = Text(tokzr.tokenize("".join(text))) #from processed text
    
    tx.close()
    p.close()

    return (text, T_orig, T_proc)
    #returns list of len 1 - processed string; Text : Processed and original

def boot(): #book to text
    try:
        file = open("data/txt/d.txt", 'r', encoding = 'utf-8')
    except:
        file = open("../data/txt/d.txt", 'r', encoding = 'utf-8')
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

    file.close()

    return books

def books_to_text(): # better dict keys
    try:
        f_df = pd.read_csv("data/csv/c_b_t.csv", encoding='utf-8')
    except:
        f_df = pd.read_csv("../data/csv/c_b_t.csv",  encoding = 'utf-8')   
    f_df['Text'] = f_df['Text'].apply(lambda x : re.sub("'s", "", (x)))
    f_df = Data_pre_proc.pre_proc(f_df)

    bs = [x for x in f_df["Book"].unique()]
    
    dictofbooks = {}
    for i in range(len(bs)):
        text = []
        # texts[i] = [rows["Text"] for idx, rows in f_df.iterrows() if(rows["Book"] == bs[i]) ]
        for idx, rows in f_df.iterrows():
            if rows["Book"] == bs[i]: #ie., text belongs to a certain book
                text.append(rows["Text"])
        dictofbooks.update({i:text})
    return dictofbooks

def books_to_chaps(): #book to chapters map
    try:
        f = open('data/txt/chaps.txt', 'r', encoding = 'utf-8')
    except:
        f = open('../data/txt/chaps.txt', 'r', encoding = 'utf-8')
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

    f.close()

    return b_c #dict_keys(['book', 'Book I.', 'BOOK II.', 'BOOK III.', 'BOOK IV.', 'BOOK V.', 'BOOK VI.'])


def get_all_chaps():
    # df = pd.read_csv("src/streamlit_data/c_b_t.csv", encoding = 'utf-8')
    try:
        df = pd.read_csv('data/csv/c_b_t.csv')
    except:
        df = pd.read_csv('../data/csv/c_b_t.csv')
    all_chaps = df["Chapter"].to_list()
    return all_chaps