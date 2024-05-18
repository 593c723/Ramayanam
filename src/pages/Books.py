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

st.set_page_config(page_title="Books",  layout="wide",) #this has to be the first call

style = "<style>h2,p, h1, .iframe, h3 {text-align: center;}  h3 {font-size: 20px;} </style>" # centers header, titles and p
st.markdown(style, unsafe_allow_html=True)

st.sidebar.markdown('''

## Hey There!
- <a href="https://jignyasa.streamlit.app/~/+/#swagatam" target="_self">Introduction </a>
## Books View
- <a href="https://jignyasa.streamlit.app/~/+/Books#centralities" target="_self">Centralities </a>
- <a href="https://jignyasa.streamlit.app/~/+/Books#network" target="_self">Networks </a>
- <a href="https://jignyasa.streamlit.app/~/+/Books#summary-kcore" target="_self">K-Core </a>
- <a href="https://jignyasa.streamlit.app/~/+/Books#ask-the-network" target="_self">Nodes - Characters </a>

## Chapter View
- <a href="https://jignyasa.streamlit.app/~/+/Chapters#evolution-characters" target="_self">Plot Evolution </a>
- <a href="https://jignyasa.streamlit.app/~/+/Chapters#pick-a-canto" target="_self">Cantos </a>
-------
<p style="font-size:17px; text-align: center;">Got Questions? Criticism? Feedback? Wanna Collaborate? 
                    Chat about mutual interests? Feel free to reach out to me!</p>

- [LinkedIn](https://www.linkedin.com/in/sumana-sridharan/)                  
- [sumanasridharan@gmail.com](sumanasridharan@gmail.com)             
''', unsafe_allow_html=True)
dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)
sys.path.append(dir.parent)
# st.write(sys.path)

graphs = books.get_graphs()
partitions = books.get_partitions(graphs)
themes = books.sent_clusts(graphs, partitions)
st.subheader("""Take a look at [this]() if you want to know more about any of the following visuals !""")
st.title('CENTRALITIES')
st.subheader("""Normalised Centrality plots for different characters(refer legend below), over the six books""")


col1, col2, col3 = st.columns([3,3,1])
col1.header('Degree')
col2.header('Betweenness')
col3.write(" ")
col3.subheader('Legend')
col3.write(" ")
col3.write(" ")
col3.write(" ")
col3.write(" ")
#centrality plots
# arrange these horizontally
# """Write a dropdown with node selections, to get list as input to display centrality ranks 
# with only people chosen by user, """
cents = books.DegreeCentrality(graphs)

books.gen_centrality_plot(cents)
try:
    pth = "/tmp/"
    img = Image.open(f"{pth}centrality.png")
except:
    pth = "pages/"
    img = Image.open(f"{pth}centrality.png")

col1.image(img)

cents = books.BtwCentrality(graphs)
books.gen_centrality_plot(cents)
try:
    pth = "/tmp/"
    img = Image.open(f"{pth}centrality.png")
except:
    pth = "pages/"
    img = Image.open(f"{pth}centrality.png")
col2.image(img)

try:
    labels = Image.open('src/legends.png')
except:
    labels = Image.open('legends.png')
col3.image(labels)
# #book-spcific data
# # is a slider the best option?



st.markdown("""---""")
st.header("Pick a Book!")
st.subheader("""All visuals henceforth will change to mirror what you pick.""")

# st.subheader("Bala Kand, Ayodhya Kand, Aranya Kand, Kishkindha Kand, Sunder Kand, Yuddha Kand")
# cols_rad= st.columns([1,6,1])
# with cols_rad[1]:
radio = st.radio('', ['Book 1','Book 2', 'Book 3', 'Book 4', 'Book 5', 'Book 6'])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;line-height: 200%;}</style>', unsafe_allow_html=True)



if radio == 'Book 1':
    my_book = 1
if radio == 'Book 2':
    my_book = 2
if radio == 'Book 3':
    my_book = 3
if radio == 'Book 4':
    my_book = 4
if radio == 'Book 5':
    my_book = 5
if radio == 'Book 6':
    my_book = 6   



# my_book = st.select_slider('', options=[1,2,3,4,5])
theme = books.get_theme(themes, my_book)
# st.write(len(themes))
st.header(f'Book: {my_book}')
st.subheader(f'Themes - Positive : {"{:.2f}".format(theme[1])}%, Negative : {"{:.2f}".format(theme[2])}%')

deg = books.top_n_central_nodes(my_book, graphs, 'Degree', 10)
btw = books.top_n_central_nodes(my_book, graphs, 'Betweenness', 10)
pgr = books.top_n_central_nodes(my_book, graphs, 'PageRank', 10)

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


# book networks

# HtmlFile = open("kcore.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read() 
# components.html(source_code, height = 900)
st.markdown("""---""")

st.header('Network')
st.subheader("The network corresponding to the book you picked! ")
st.subheader("""Feel free to zoom-in and look at the characters and their relationships, click on, drag and play around a little! Use the 'Ask the Network' component at the end of this page to find information on a specific character. Scroll down to the k-core below for the condensed version!""")


book_network = books.get_network(graphs[my_book])
components.html(book_network.read(), height = 750)



cols= st.columns([1,4,1])
st.markdown("""---""")
with cols[1]:
    st.header('Summary - KCore')
    st.subheader("""A k-core representation of the main network. k = 4 for book 6, and 6 for all others.""")

    if my_book == 6:
        kcore = books.get_kcore(graphs[my_book], 4)
    else:
        kcore = books.get_kcore(graphs[my_book], 6)
    kcore_net = books.get_network(kcore)
    components.html(kcore_net.read(), height = 750)

st.subheader("""If you have a specific character in mind, select them from the dropdown to view their centrality scores and neighbors. """)
st.subheader("Need some inspiration? Use the wordcloud!")

cols_nodes= st.columns(2)
# query the network : node - to return - centralities, neighbours
with cols_nodes[0]:

    st.header('Ask the Network')

    node_options = graphs[my_book].nodes
    my_node = st.selectbox('Select Character', node_options)

    all_cents = books.DegreeCentrality(graphs)
    dc = all_cents[my_book]
    st.subheader("Centralities")
    st.write("Degree Centrality : ", f"{'{:.2f}'.format(dc[my_node])}")
    all_cents = books.BtwCentrality(graphs)
    bc = all_cents[my_book]
    st.write("Betweenness Centrality : ", f"{'{:.2f}'.format(bc[my_node])}")
    all_cents = books.PRCentrality(graphs)
    pc = all_cents[my_book]
    st.write("Page Rank Centrality : ", f"{'{:.2f}'.format(pc[my_node])}")
    d_neighs = graphs[my_book][my_node]
    neighs = [k for k, v in d_neighs.items()]
    st.subheader("Neighbours")
    for neighbour in neighs:
        st.write(neighbour.title())
with cols_nodes[1]:
    st.header("Character Wordcloud")
    try:
        img = Image.open('src/wordcloud.png')
    except:
        img = Image.open('wordcloud.png')
    st.image(img)

