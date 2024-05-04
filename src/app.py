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

st.set_page_config(layout="wide") #this has to be the first call

style = "<style>h2, h1, p, .iframe, h3 {text-align: center;} #tabs-bui1800-tab-0 {font-size: 40px;} </style>" # centers header, titles and p
st.markdown(style, unsafe_allow_html=True)

# st.markdown(
#     """
# <style>
# .appview-container {
#     background-color: black;
#     color : white;
# }

# .Widget>label {
#     color: white;
#     font-family: monospace;

# }

# </style>
# """,
#     unsafe_allow_html=True,
# )


# dir = path.Path(__file__).abspath()
# sys.path.append(dir.parent.parent)

# st.write(books.sys_path())

# st.write(dir)
# st.write(sys.path)
# test = pd.read_csv("src/streamlit_data/sentiments_books.csv")

tab1, tab2 = st.tabs(["Book View", "Chapter View"])

with tab1:
    graphs = books.get_graphs()
    partitions = books.get_partitions(graphs)
    themes = books.sent_clusts(graphs, partitions)
    st.title('CENTRALITIES')
    col1, col2, col3 = st.columns(3)
    col1.header('Degree Cenratality')
    col2.header('Betweenness Centrality')
    col3.header('PageRank Centrality')



    #centrality plots
    # arrange these horizontally
    # """Write a dropdown with node selections, to get list as input to display centrality ranks 
    # with only people chosen by user, """
    cents = books.DegreeCentrality(graphs)


    # books.gen_centrality_plot(cents)
    # img = Image.open("src/outputs/centrality.png")
    # col1.image(img)

    # cents = books.BtwCentrality(graphs)
    # books.gen_centrality_plot(cents)
    # img = Image.open("src/outputs/centrality.png")
    # col2.image(img)

    # cents = books.PRCentrality(graphs)
    # books.gen_centrality_plot(cents)
    # img = Image.open("src/outputs/centrality.png")
    # col3.image(img)

    # #book-spcific data
    # # is a slider the best option?




    st.header("Pick a Book!")
    st.subheader("Bala Kand, Ayodhya Kand, Aranya Kand, Kishkindha Kand, Sunder Kand, Yuddha Kand")
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
    st.write(len(themes))
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



    cols= st.columns(2)

    with cols[0]:
        st.header('Summary - KCore')
        if my_book == 6:
            kcore = books.get_kcore(graphs[my_book], 4)
        else:
            kcore = books.get_kcore(graphs[my_book], 5)
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
        img = Image.open('../outputs/wordcloud.png')
        st.image(img)



with tab2:
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
        st.header(f"Book: {ch_book}")

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

        # evolution plot
        st.subheader("Evolution : Characters")
        centre_cols = st.columns([0.3,0.6,0.3,2.0,0.3, 0.5, 0.3])
        with centre_cols[3]:
            char_evol = cantos.plot_evol()
            cantos.get_evol_graphs(book_start, book_end, char_evol)
            img_evol = Image.open("../outputs/evol_plot.png")
            st.image(img_evol)

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

        cols= st.columns(2)

        with cols[0]:
            st.header('Dendogram')
            cantos.dendo(my_chap)
            img = Image.open("../outputs/dendo.png")
            cols[0].image(img)
        with cols[1]:
            st.header('Network')
            chap_network = cantos.get_network(graphs[my_chap])
            components.html(chap_network.read(), height = 750)
        # gradio_interface_url = "https://2d7e9408cfac270118.gradio.live/"  

        # st.write(f'<iframe src="{gradio_interface_url}" width="800" height="600"></iframe>',
        #  unsafe_allow_html=True) 
