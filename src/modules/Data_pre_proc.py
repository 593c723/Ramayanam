import re
import string
import nltk
from unidecode import unidecode
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
stopwords = stopwords + ['thou', 'thy', 'thine', 'thus', 'thee', 'may']
punc = ['.', ',', '()', ';', ':']

def rem_stp(txt):
    txt = txt.split()
    op = [i for i in txt if i not in stopwords]
    return " ".join(op)

def pre_proc(df):
    df['Text'] = df['Text'].apply(lambda x : re.sub("([0-9]*)", '', x))
    df['Text'] = df['Text'].apply(lambda x : unidecode(x))
    # for p in punc:
    #    df['Text'] = df['Text'].apply(lambda x : x.replace(p, " "))
    df['Text'] = df['Text'].apply(lambda x : x.replace(string.punctuation, " "))
    df['Text'] = df['Text'].apply(lambda x : x.replace(",", " ").replace("(", "").replace(")", ""))
    df['Text'] = df['Text'].apply(lambda x: x.lower())
    df['Text'] = df['Text'].apply(lambda x : rem_stp(x))

    return df
