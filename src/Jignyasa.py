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

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# - <a href="" target="_self">Blog 1 </a>
# - <a href="" target="_self">Blog 2 </a>

st.sidebar.markdown('''

## Hey There!
- <a href="https://ramayanam.streamlit.app/~/+/#swagatam" target="_self">Introduction </a>
## Books View
- <a href="https://ramayanam.streamlit.app/~/+/Books#centralities" target="_self">Centralities </a>
- <a href="https://ramayanam.streamlit.app/~/+/Books#network" target="_self">Networks </a>
- <a href="https://ramayanam.streamlit.app/~/+/Books#summary-kcore" target="_self">K-Core </a>
- <a href="https://ramayanam.streamlit.app/~/+/Books#ask-the-network" target="_self">Nodes - Characters </a>

## Chapter View
- <a href="https://ramayanam.streamlit.app/~/+/Chapters#evolution-characters" target="_self">Plot Evolution </a>
- <a href="https://ramayanam.streamlit.app/~/+/Chapters#pick-a-canto" target="_self">Cantos </a>
-------
<p style="font-size:17px; text-align: center;">Got Questions? Criticism? Feedback? Wanna Collaborate or 
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
         comprehending the original Sanskrit version - an endeavour that has failed as of yet to 
         do anything but elicit a sense of protracted annoyance at my own excruciatingly slow progress. """)
st.write("""
         I decided then, to employ something that I was more familiar with - something that was 
         sure to give me the results that had so far managed to evade me. I turned thus to my trusty 
         set of analytical tools - and what answers have they given me! 
         """)
st.write("""I have compiled in this app, a few interactive visualisations that were the products of my analysis.
         I have had a lot of fun playing around with them, I hope you do too!""")

# st.write("""( [Here's]() 
#          a little something I wrote on the insights I worked out from the book. Feel free to check it out!)""")
# st.write("""(Go [here]() 
#          if you wanna get technical!)""")
st.write("")
st.write("Best,")
st.write("Sumana")
