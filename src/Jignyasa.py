import streamlit as st
import streamlit.components.v1 as components

from modules import components as comp

from PIL import Image

#test
# import pandas as pd 

import path
import sys

st.set_page_config(page_title="Swagatam!",  layout="wide",) #this has to be the first call

style = "<style>p{font-size:20px;}</style>"
# style = "<style>h2, h1, p, .iframe, h3 {text-align: center;} #tabs-bui1800-tab-0 {font-size: 40px;} </style>" # centers header, titles and p
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

# st.write(books.sys_path())

# st.write(dir)
# st.write(sys.path)
# test = pd.read_csv("src/streamlit_data/sentiments_books.csv")

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# - <a href="" target="_self">Blog 1 </a>
# - <a href="" target="_self">Blog 2 </a>

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

st.subheader("Swagatam!")
st.write("")
st.write("There are some things in life that try their best to be constants.")
st.write("""The Ramayanam has been one such thing for me. A great epic passed down over the ages, 
         there are not many in India who haven’t heard its name. The fascination that 
         this story never fails to provoke in me is rooted in childish wonder - born of tales told 
         in confidant tones, after much pleading and persuasion; furthered, by the encounters with 
         different versions; a fascination that evinced in me interest enough to try my hand at 
         comprehending the original Sanskrit version - an endeavour that has failed of yet to bear 
         any fruit but to elicit protracted annoyance at my own excruciatingly slow progress. """)
st.write("""
         I decided then, to employ something that I was more familiar with - something that was 
         sure to give me the results that had so far managed to evade me. I turned thus to my trusty 
         set of analytical tools - and what answers have they given me! 
         """)
st.write("""I have compiled in this app, a few interactive visualisations that were the products of my analysis
         I have had a lot of fun playing around with them, I hope you do too!""")

st.write("""( [Here's](https://593c723-ramayanam-srcjignyasa-h045eg.streamlit.app/) 
         a little something I wrote on the insights I worked out from the book. Feel free to check it out!)""")
st.write("""(Go [here](https://593c723-ramayanam-srcjignyasa-h045eg.streamlit.app/) 
         if you wanna get technical!)""")
st.write("")
st.write("Best,")
st.write("Sumana")
# tab1, tab2 = st.tabs(["Book View", "Chapter View"])

# with tab1:
    
#     # st.write(sys.path)
#     # st.write(dir)
#     # st.write(comp.sys_path())


#     graphs = books.get_graphs()
#     partitions = books.get_partitions(graphs)
#     themes = books.sent_clusts(graphs, partitions)
#     st.title('CENTRALITIES')
#     col1, col2, col3, col4 = st.columns([3,3,3,1])
#     col1.header('Degree')
#     col2.header('Betweenness')
#     col3.header('PageRank')
#     col4.write(" ")
#     col4.subheader('Legend')
#     col4.write(" ")
#     col4.write(" ")
#     col4.write(" ")
#     #centrality plots
#     # arrange these horizontally
#     # """Write a dropdown with node selections, to get list as input to display centrality ranks 
#     # with only people chosen by user, """
#     cents = books.DegreeCentrality(graphs)


#     books.gen_centrality_plot(cents)
#     try:
#         pth = "/tmp/"
#         img = Image.open(f"{pth}centrality.png")
#     except:
#         pth = ""
#         img = Image.open(f"{pth}centrality.png")
    
#     col1.image(img)

#     cents = books.BtwCentrality(graphs)
#     books.gen_centrality_plot(cents)
#     try:
#         pth = "/tmp/"
#         img = Image.open(f"{pth}centrality.png")
#     except:
#         pth = ""
#         img = Image.open(f"{pth}centrality.png")
#     col2.image(img)

#     cents = books.PRCentrality(graphs)
#     books.gen_centrality_plot(cents)
#     try:
#         pth = "/tmp/"
#         img = Image.open(f"{pth}centrality.png")
#     except:
#         pth = ""
#         img = Image.open(f"{pth}centrality.png")
#     col3.image(img)
#     try:
#         labels = Image.open('src/legends.png')
#     except:
#         labels = Image.open('legends.png')
#     col4.image(labels)
#     # #book-spcific data
#     # # is a slider the best option?




#     st.header("Pick a Book!")
#     # st.subheader("Bala Kand, Ayodhya Kand, Aranya Kand, Kishkindha Kand, Sunder Kand, Yuddha Kand")
#     # cols_rad= st.columns([1,6,1])
#     # with cols_rad[1]:
#     radio = st.radio('', ['Book 1','Book 2', 'Book 3', 'Book 4', 'Book 5', 'Book 6'])
#     st.write('<style>div.row-widget.stRadio > div{flex-direction:row;line-height: 200%;}</style>', unsafe_allow_html=True)

    
    
#     if radio == 'Book 1':
#         my_book = 1
#     if radio == 'Book 2':
#         my_book = 2
#     if radio == 'Book 3':
#         my_book = 3
#     if radio == 'Book 4':
#         my_book = 4
#     if radio == 'Book 5':
#         my_book = 5
#     if radio == 'Book 6':
#         my_book = 6   

    

#     # my_book = st.select_slider('', options=[1,2,3,4,5])
#     theme = books.get_theme(themes, my_book)
#     # st.write(len(themes))
#     st.header(f'Book: {my_book}')
#     st.subheader(f'Themes - Positive : {"{:.2f}".format(theme[1])}%, Negative : {"{:.2f}".format(theme[2])}%')

#     deg = books.top_n_central_nodes(my_book, graphs, 'Degree', 10)
#     btw = books.top_n_central_nodes(my_book, graphs, 'Betweenness', 10)
#     pgr = books.top_n_central_nodes(my_book, graphs, 'PageRank', 10)

#     cols = st.columns(3)
#     with cols[0]:
#         cols[0].header('Degree Centrality Ranks')
#         for node in deg:
#             st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")
#     with cols[1]:
#         cols[1].header('Betweenness Centrality Ranks')
#         for node in btw:
#             st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")
#     with cols[2]:
#         cols[2].header('Page Rank Centrality Ranks')
#         for node in pgr:
#             st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")


#     # book networks

#     # HtmlFile = open("kcore.html", 'r', encoding='utf-8')
#     # source_code = HtmlFile.read() 
#     # components.html(source_code, height = 900)

#     st.header('Network')
#     book_network = books.get_network(graphs[my_book])
#     components.html(book_network.read(), height = 750)



#     cols= st.columns([1,4,1])

#     with cols[1]:
#         st.header('Summary - KCore')
#         if my_book == 6:
#             kcore = books.get_kcore(graphs[my_book], 4)
#         else:
#             kcore = books.get_kcore(graphs[my_book], 6)
#         kcore_net = books.get_network(kcore)
#         components.html(kcore_net.read(), height = 750)


#     cols_nodes= st.columns(2)
#     # query the network : node - to return - centralities, neighbours
#     with cols_nodes[0]:
#         st.header('Ask the Network')
#         node_options = graphs[my_book].nodes
#         my_node = st.selectbox('Select Character', node_options)

#         all_cents = books.DegreeCentrality(graphs)
#         dc = all_cents[my_book]
#         st.subheader("Centralities")
#         st.write("Degree Centrality : ", f"{'{:.2f}'.format(dc[my_node])}")
#         all_cents = books.BtwCentrality(graphs)
#         bc = all_cents[my_book]
#         st.write("Betweenness Centrality : ", f"{'{:.2f}'.format(bc[my_node])}")
#         all_cents = books.PRCentrality(graphs)
#         pc = all_cents[my_book]
#         st.write("Page Rank Centrality : ", f"{'{:.2f}'.format(pc[my_node])}")
#         d_neighs = graphs[my_book][my_node]
#         neighs = [k for k, v in d_neighs.items()]
#         st.subheader("Neighbours")
#         for neighbour in neighs:
#             st.write(neighbour.title())
#     with cols_nodes[1]:
#         st.header("Character Wordcloud")
#         try:
#             img = Image.open('src/wordcloud.png')
#         except:
#             img = Image.open('wordcloud.png')
#         st.image(img)



# with tab2:
#         graphs = cantos.get_graphs()
#         # themes = cantos.sent_clusts(graphs)
#         st.header("Pick a Book!")
#         rad = st.radio('', ['Book1','Book2', 'Book3', 'Book4', 'Book5', 'Book6'])
#         st.write('<style>div.row-widget.stRadio > div{flex-direction:row;line-height: 200%;}</style>', unsafe_allow_html=True)
#         if rad == 'Book1':
#             ch_book = 1
#         if rad == 'Book2':
#             ch_book = 2
#         if rad == 'Book3':
#             ch_book = 3
#         if rad == 'Book4':
#             ch_book = 4
#         if rad == 'Book5':
#             ch_book = 5
#         if rad == 'Book6':
#             ch_book = 6
#         st.header(f"Book: {ch_book}")

#         boo_keys = ['Book I.', 'BOOK II.', 'BOOK III.', 'BOOK IV.', 'BOOK V.', 'BOOK VI.']
#         boos = [i for i in range(1, 7)]
#         boo_keys_num = dict(zip(boos, boo_keys))
#         # boo = "book"
#         boo = boo_keys_num[ch_book] # map 1: "book I." etc


#         all_chapters = comp.get_all_chaps()
#         all_cantos_dict = comp.books_to_chaps()
#         my_chaps = all_cantos_dict[boo] # all chaps in given boo my_book
#         book_start = all_chapters.index(my_chaps[0])
#         book_end = all_chapters.index(my_chaps[len(my_chaps)-1])# last chptr

#         # evolution plot
#         st.subheader("Evolution : Characters")
#         centre_cols = st.columns([0.3,0.6,0.3,2.0,0.3, 0.5, 0.3])
#         with centre_cols[3]:
#             char_evol = cantos.plot_evol()
#             cantos.get_evol_graphs(book_start, book_end, char_evol)
#             try:
#                 pth = "/tmp/"
#                 img_evol = Image.open(f"{pth}evol_plot.png")
#             except:
#                 pth = ""
#                 img_evol = Image.open(f"{pth}evol_plot.png")
#             st.image(img_evol)

#         st.header("Pick a Canto!")
#         my_chap_name = st.selectbox('Select', my_chaps)
#         chap_idx = all_chapters.index(my_chap_name)

#         # my_chap = st.slider('', book_start, book_end)
#         my_chap = chap_idx
#         deg = books.top_n_central_nodes(my_chap, graphs, 'Degree', 10)
#         btw = books.top_n_central_nodes(my_chap, graphs, 'Betweenness', 10)
#         pgr = books.top_n_central_nodes(my_chap, graphs, 'PageRank', 10)

#         cols = st.columns(3)
#         with cols[0]:
#             cols[0].header('Degree Centrality Ranks')
#             for node in deg:
#                 st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")
#         with cols[1]:
#             cols[1].header('Betweenness Centrality Ranks')
#             for node in btw:
#                 st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")
#         with cols[2]:
#             cols[2].header('Page Rank Centrality Ranks')
#             for node in pgr:
#                 st.write(node[0].title()," : ", f"{'{:.2f}'.format(node[1])}")

#         cols= st.columns([1,3,1])

#         # with cols[0]:
#         #     st.header('Dendogram')
#         #     cantos.dendo(my_chap)
#         #     try:
#         #         pth = "/tmp/"
#         #         img = Image.open(f"{pth}dendo.png")
#         #     except:
#         #         pth = ""
#         #         img = Image.open(f"{pth}dendo.png")
            
#             # cols[0].image(img)
#         with cols[1]:
#             st.header('Network')
#             chap_network = cantos.get_network(graphs[my_chap])
#             components.html(chap_network.read(), height = 750)
#         # gradio_interface_url = "https://2d7e9408cfac270118.gradio.live/"  

#         # st.write(f'<iframe src="{gradio_interface_url}" width="800" height="600"></iframe>',
#         #  unsafe_allow_html=True) 
