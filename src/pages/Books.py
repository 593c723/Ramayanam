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

style = "<style>h2, h1, p, .iframe, h3 {text-align: center;} #tabs-bui1800-tab-0 {font-size: 40px;} </style>" # centers header, titles and p
st.markdown(style, unsafe_allow_html=True)


dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

st.write(sys.path)

graphs = books.get_graphs()
partitions = books.get_partitions(graphs)
themes = books.sent_clusts(graphs, partitions)
st.title('CENTRALITIES')
col1, col2, col3, col4 = st.columns([3,3,3,1])
col1.header('Degree')
col2.header('Betweenness')
col3.header('PageRank')
col4.write(" ")
col4.subheader('Legend')
col4.write(" ")
col4.write(" ")
col4.write(" ")
#centrality plots
# arrange these horizontally
# """Write a dropdown with node selections, to get list as input to display centrality ranks 
# with only people chosen by user, """
cents = books.DegreeCentrality(graphs)

books.gen_centrality_plot(cents)
try:
    pth = "/pages/tmp/"
    img = Image.open(f"{pth}centrality.png")
except:
    pth = "pages/"
    img = Image.open(f"{pth}centrality.png")

col1.image(img)

cents = books.BtwCentrality(graphs)
books.gen_centrality_plot(cents)
try:
    pth = "/tmp/pages/"
    img = Image.open(f"{pth}centrality.png")
except:
    pth = "pages/"
    img = Image.open(f"{pth}centrality.png")
col2.image(img)

cents = books.PRCentrality(graphs)
books.gen_centrality_plot(cents)
try:
    pth = "/tmp/pages/"
    img = Image.open(f"{pth}centrality.png")
except:
    pth = "pages/"
    img = Image.open(f"{pth}centrality.png")
col3.image(img)
try:
    labels = Image.open('src/legends.png')
except:
    labels = Image.open('legends.png')
col4.image(labels)
# #book-spcific data
# # is a slider the best option?




st.header("Pick a Book!")
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

st.header('Network')
book_network = books.get_network(graphs[my_book])
components.html(book_network.read(), height = 750)



cols= st.columns([1,4,1])

with cols[1]:
    st.header('Summary - KCore')
    if my_book == 6:
        kcore = books.get_kcore(graphs[my_book], 4)
    else:
        kcore = books.get_kcore(graphs[my_book], 6)
    kcore_net = books.get_network(kcore)
    components.html(kcore_net.read(), height = 750)


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

