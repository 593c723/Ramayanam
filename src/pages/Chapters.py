import streamlit as st
import streamlit.components.v1 as components

from modules import components as comp
from  modules import books
from modules import cantos

from PIL import Image

#test
# import pandas as pd 

import path
import sys

st.set_page_config(page_title="Chapters", layout="wide",) #this has to be the first call


style = "<style>h2,p, h1, .iframe, h3 {text-align: center;}  h3 {font-size: 20px;} </style>" # centers header, titles and p
st.markdown(style, unsafe_allow_html=True)


dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)


graphs = cantos.get_graphs()
# themes = cantos.sent_clusts(graphs)
st.header("Pick a Book!")
rad = st.radio('', ['Book1','Book2', 'Book3', 'Book4', 'Book5', 'Book6'])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;line-height: 200%;}</style>', unsafe_allow_html=True)
if rad == 'Book1':
    ch_book = 1
if rad == 'Book2':
    ch_book = 2
if rad == 'Book3':
    ch_book = 3
if rad == 'Book4':
    ch_book = 4
if rad == 'Book5':
    ch_book = 5
if rad == 'Book6':
    ch_book = 6
st.title(f"Book: {ch_book}")

boo_keys = ['Book I.', 'BOOK II.', 'BOOK III.', 'BOOK IV.', 'BOOK V.', 'BOOK VI.']
boos = [i for i in range(1, 7)]
boo_keys_num = dict(zip(boos, boo_keys))
# boo = "book"
boo = boo_keys_num[ch_book] # map 1: "book I." etc


all_chapters = comp.get_all_chaps()
all_cantos_dict = comp.books_to_chaps()
my_chaps = all_cantos_dict[boo] # all chaps in given boo my_book
book_start = all_chapters.index(my_chaps[0])
book_end = all_chapters.index(my_chaps[len(my_chaps)-1])# last chptr


st.sidebar.markdown('''

## Hey There!
- <a href="https://jignyasa.streamlit.app/~/+/#swagatam" target="_self">Introduction </a>
## Books View
- <a href="https://jignyasa.streamlit.app/~/+/#centralities" target="_self">Centralities </a>
- <a href="https://jignyasa.streamlit.app/~/+/#network" target="_self">Networks </a>
- <a href="https://jignyasa.streamlit.app/~/+/#summary-kcore" target="_self">K-Core </a>
- <a href="https://jignyasa.streamlit.app/~/+/#ask-the-network" target="_self">Nodes - Characters </a>

## Chapter View
- <a href="http://localhost:8501/Chapters#evolution-characters" target="_self">Plot Evolution </a>
- <a href="http://localhost:8501/Chapters#pick-a-canto" target="_self">Cantos </a>
-------
<p style="font-size:17px; text-align: center;">Got Questions? Criticism? Feedback? Wanna Collaborate? 
                    Chat about mutual interests? Feel free to reach out to me!</p>

- [LinkedIn](https://www.linkedin.com/in/sumana-sridharan/)                  
- [sumanasridharan@gmail.com](sumanasridharan@gmail.com)             
''', unsafe_allow_html=True)

# evolution plot
st.header("Evolution : Characters")
st.subheader("""Change the Book above to see the evolution of the plot in the graph below. It plots the existing(continued appearances), newly introduced and disappearing characters over different chapters in the book.""")

centre_cols = st.columns([0.3,0.6,0.3,2.0,0.3, 0.5, 0.3])
with centre_cols[3]:
    char_evol = cantos.plot_evol()
    cantos.get_evol_graphs(book_start, book_end, char_evol)
    try:
        pth = "/tmp/"
        img_evol = Image.open(f"{pth}evol_plot.png")
    except:
        pth = ""
        img_evol = Image.open(f"{pth}evol_plot.png")
    st.image(img_evol)

st.markdown("""---""")

st.header("Pick a Canto!")

my_chap_name = st.selectbox('Select', my_chaps)
chap_idx = all_chapters.index(my_chap_name)

# my_chap = st.slider('', book_start, book_end)
my_chap = chap_idx
deg = books.top_n_central_nodes(my_chap, graphs, 'Degree', 10)
btw = books.top_n_central_nodes(my_chap, graphs, 'Betweenness', 10)
pgr = books.top_n_central_nodes(my_chap, graphs, 'PageRank', 10)

cols = st.columns(3)
with cols[0]:
    cols[0].header('Degree Centrality Ranks')
    for node in deg:
        st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")
with cols[1]:
    cols[1].header('Betweenness Centrality Ranks')
    for node in btw:
        st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")
with cols[2]:
    cols[2].header('Page Rank Centrality Ranks')
    for node in pgr:
        st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")

cols= st.columns([1,3,1])

# with cols[0]:
#     st.header('Dendogram')
#     cantos.dendo(my_chap)
#     try:
#         pth = "/tmp/"
#         img = Image.open(f"{pth}dendo.png")
#     except:
#         pth = ""
#         img = Image.open(f"{pth}dendo.png")
    
    # cols[0].image(img)
with cols[1]:
    st.header('Network')
    chap_network = cantos.get_network(graphs[my_chap])
    components.html(chap_network.read(), height = 750)
# gradio_interface_url = "https://2d7e9408cfac270118.gradio.live/"  

# st.write(f'<iframe src="{gradio_interface_url}" width="800" height="600"></iframe>',
#  unsafe_allow_html=True) 
