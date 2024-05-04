import pandas as pd
import networkx as nx
from pyvis.network import Network
import community.community_louvain as plc # py louvain
import numpy as np
#pip install python-louvain
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from modules import components
import unidecode
import re
import colorsys
import path
import sys

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

def sys_path():
    return sys.path

def scalar_to_hex(old_value, old_min, old_max):
    # old_min = -1, old_max = 1 :: vader
    # frequencies(range - 0,42)
    new_max = 1
    new_min = 0.1
    new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

    rgb = colorsys.hsv_to_rgb(new_value, 1, 1)
    rgbhex = "".join("%02X" % round(i*255) for i in rgb)

    return '#' + rgbhex
scalar_to_hex(0.80520, -1, 1)

def get_graphs():
    ctbw = pd.read_csv("src/streamlit_data/sentiments_books.csv", encoding = 'utf-8')
    # ctbw = pd.read_csv("ramayanam/data/csv/sentiments_books.csv", encoding = 'utf-8')
    ctbw['weight_inv'] = 1/ctbw.Weight
    ctbw.head()
    graphs = [nx.from_pandas_edgelist(
          ctbw[ctbw.Book==i],
          source='Source', target='Target',
          edge_attr=['Weight', 'weight_inv', 'vader'])
          for i in range(1, 8)]
    return graphs

def get_partitions(graphs):
    partitions = []
    for i in range(0, 7):
        G = graphs[i]
        # Find modularity
        part = plc.best_partition(G)
        partitions.append(part) # returns dict = node: cluster
        mod = plc.modularity(part,G)
    return partitions
def sem_color(val):
    if val > 0.05:
        #positive
        color = 'green'
    if val < 0.05:
        color = 'red'
    return color
def sent_clusts(graphs, partitions): #set colors for graphs, returns themes
    # sets colors(node, edges), calcs theme(ie., sentiment aggregate for each relation)
    theme = [] #pos, neg tuple for each book
    for i in range(7):
        graph = graphs[i] 
        part = partitions[i]
        nodes = graph.nodes()
        values = [part.get(node) for node in graph.nodes()]

        nmap = {k:scalar_to_hex(v, 1, 42) for k, v in zip(nodes, values)} # node clusters
        emap = {} # sentiment colors +ve- red, -ve blue
        pos = 0 #no. of p+ve relations
        neg = 0
        for (source, target), attr in graph.edges.items():
            # emap[(source, target)] = scalar_to_hex(attr['vader'], -1, 1)
            emap[(source, target)] = sem_color(attr['vader'])
            if attr['vader'] > 0.05:
                pos += 1
            elif attr['vader'] < 0.05:
                neg += 1

        # print(nmap['rama'])
        for (source, target), attr in graph.edges.items():
            graph.nodes[source]['color'] = nmap[source]
            graph.nodes[target]['color'] = nmap[target]
            graph.edges[(source, target)]['color'] = emap[((source, target))]
        theme.append((pos, neg))
    return theme

"""Centralities - two actionable funcitons: ranks list and character spread over books"""


def DegreeCentrality(graphs):
    # key = book no. ; value = node:centrality
    deg = {}
    for i in range(1, len(graphs)): #cos here 0th book has only 2 characters; where 1-5 corresponds to 'books' 1-5
        deg[i] = nx.degree_centrality(graphs[i])
    return deg

def PRCentrality(graphs): #weighted pagerank
    pgr = {}
    for i in range(1, len(graphs)):
        pgr[i] = nx.pagerank(graphs[i], weight='Weight')
    return pgr

def BtwCentrality(graphs):# weighted
    btw = {}
    for i in range(1, len(graphs)):
        btw[i] = nx.betweenness_centrality(graphs[i], weight='Weight')
    return btw


def top_n_central_nodes(book_no, graphs, centrality, n):
    #book_no = book i
    # centrality = string: PageRank, Degree, Betweenness
    # n : top n nodes
    if centrality == 'PageRank':
        pgr = PRCentrality(graphs)
        ranks = pgr[book_no]
    if centrality == 'Degree':
        deg = DegreeCentrality(graphs)
        ranks = deg[book_no]
    if centrality == 'Betweenness':
        btw = BtwCentrality(graphs)
        ranks = btw[book_no]
    rank_list = sorted(ranks.items(),
        key=lambda x:x[1], reverse=True)[0:n]
    return rank_list
    

def gen_centrality_plot(centralities):#ip dict of centralities of all books
    deg = centralities
    deg_list = [] #normalised dict of dcs for each book
    for d in deg.values(): #for each book
        new_vals = {}
        sorted_vals = sorted(d.items(), key=lambda x:x[1], reverse=True)
        for k in d:
            old_value = d[k]
            old_min = sorted_vals[-1][1]
            old_max = sorted_vals[0][1]
            new_max = 1
            new_min = 0
            new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
            new_vals[k] = new_value
        deg_list.append(new_vals)

    evol_df = pd.DataFrame.from_records(deg_list, index=[i+1 for i in range(len(deg))]).fillna(0)
    plot_list = ['rama', 'kaikeyi','lakshman', 'sita', "dasaratha", 'hanuman', 'bharat', 'ayodhya',
                'ravan', 'kumbhakarna', 'vibhishan']
    print(evol_df.shape)
    plt.figure(figsize=(10,10))

    evol_df[plot_list].plot()
    plt.yticks(np.arange(0.0, 1.0, 0.1))
    plt.xticks(np.arange(1, 6, 1))

    plt.savefig("../outputs/centrality.png")

def get_network(graph): #graphs[n] element for nth graph
    nt = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", directed = False, filter_menu=False)
    nt.from_nx(graph)
    # nt.show('g3.html', notebook=False)
    nt.save_graph('../outputs/netvis.html')
    HtmlFile = open(f'../outputs/netvis.html', 'r', encoding='utf-8')
    return HtmlFile

def get_kcore(graph, k):
    kcore = nx.k_core(graph, k)
    return kcore

def get_theme(themes, book): #get_themes() object, book no.
    pos = themes[book][0]
    neg = themes[book][1]
    if pos > neg:
        th = 'Positive'
    else:
        th = 'Negative'
    posp = (pos/(pos+neg))*100
    negp = (neg/(pos+neg))*100
    return th, posp, negp