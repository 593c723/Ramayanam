import pandas as pd
import networkx as nx
from pyvis.network import Network
import community
import numpy as np
#pip install python-louvain
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from modules import components
from unidecode import unidecode
import re
import colorsys
import scipy
import scipy.cluster.hierarchy as sch

import path
import sys

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent.parent)



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
    try:
        ctbw = pd.read_csv("data/csv/sentiments_chaps.csv", encoding = 'utf-8')
    except:
        ctbw = pd.read_csv("../data/csv/sentiments_chaps.csv", encoding = 'utf-8')
    ctbw['weight_inv'] = 1/ctbw.Weight
    ctbw.head()
    graphs = [nx.from_pandas_edgelist(
          ctbw[ctbw.Canto_no==i],
          source='Source', target='Target',
          edge_attr=['Weight', 'weight_inv', 'vader'])
          for i in range(494)]
    return graphs

def louvain(graphs):
    partitions = []
    for i in range(494):
        G = graphs[i]
        # Find modularity
        part = community.best_partition(G)
        partitions.append(part) # returns dict = node: cluster
    return partitions
# p = louvain()
# p[1]['rama']

   
def girvan_newman(graphs):
    partitions = []
    for i in range(494):
        G = graphs[i]
        # Find modularity
        part = nx.community.girvan_newman(G)
        # mod = community.modularity(part,G)
        clusters = tuple(sorted(c) for c in next(part))
        parts = {}
        for i in range(len(clusters)):
            for node in clusters[i]:
                parts[node] = i
        partitions.append(parts)
    return partitions


def sem_color(val):
    if val > 0.05:
        #positive
        color = 'green'
    if val < 0.05:
        color = 'red'
    return color

def sent_clusts(graphs): 
    theme = [] # themes for 0-493 chaps
    for i in range(494):
        graph = graphs[i]
        # partitions = girvan_newman() 
        partitions = louvain(graphs)
        part = partitions[i]
        nodes = graph.nodes()
        values = [part.get(node) for node in nodes] # from dict(part)

        nmap = {k:scalar_to_hex(v, 1, 42) for k, v in zip(nodes, values)} # node clusters
        emap = {} # sentiment colors +ve- red, -ve blue
        pos = 0
        neg = 0
        for (source, target), attr in graph.edges.items():
            emap[(source, target)] = scalar_to_hex(attr['vader'], -1, 1)
            if attr['vader'] > 0.05:
                pos += 1
            elif attr['vader'] < 0.05:
                neg += 1
            # emap[(source, target)] = sem_color(attr['vader'])
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
    for i in range(1, len(graphs)): #cos here 0th book has only 2 characters
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
    

def get_network(graph): #graphs[n] element for nth graph
    nt = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", directed = False, filter_menu=False)
    nt.from_nx(graph)
    # nt.show('g3.html', notebook=False)
    try:
        path = '/tmp/'
        nt.save_graph(f'{path}ch_netvis.html')
    except:
        path = ""
        nt.save_graph(f'{path}ch_netvis.html')
    HtmlFile = open(f'{path}ch_netvis.html', 'r', encoding='utf-8')
    # nt.save_graph('netvis.html')
    # HtmlFile = open(f'netvis.html', 'r', encoding='utf-8')
    return HtmlFile

def dendo(canto):
    try:
        cpo = pd.read_csv("data/csv/clusts.csv", encoding = 'utf-8')
    except:
        cpo = pd.read_csv("../data/csv/clusts.csv", encoding = 'utf-8')
    r = (
    cpo.query(f"Canto == {canto}"))
    occ = r.Values.to_list()
    chap = r.Canto.to_list()
    labels = r.Person.to_list()

    #need condensed distance matrix
    x = np.array([[occ[i]] for i in range(len(occ))])

    cond_mat = scipy.spatial.distance.pdist(x)

    hclust = sch.linkage(cond_mat)
    plt.figure(figsize=(10,10))
    dend = sch.dendrogram(hclust, labels=labels, orientation='right') #leaf-rotation
    try:
        path = "/tmp/"
        plt.savefig(f"{path}dendo.png")
    except:
        path = ""
        plt.savefig(f"{path}dendo.png")

def plot_evol(): #chapter name
    try:
        df = pd.read_csv("data/csv/c_b_t.csv", encoding = 'utf-8')
    except:
        df = pd.read_csv("../data/csv/c_b_t.csv", encoding = 'utf-8')
    chars = components.get_char_list()[0]
    existing = []
    char_evol = {}
    for idx, row in df.iterrows():
        present = []
        for word in row.Text.split():
            if ((word.lower()) in chars) and (unidecode(word) not in present):
                present.append(unidecode(word))
        # present = [word for word in row.Text.split() if ((word.lower()) in chars) and (word not in present)] # all chars in current chapter
        disappearing = [unidecode(word) for word in existing if (unidecode(word) not in present)] # all chars leaving
        new = [unidecode(word) for word in present if (unidecode(word) not in existing)] # new chars appearing
        existing = present
        char_evol[row["Chapter"]] = (present, disappearing, new) 
        # present-new+disappearing = old
        # old - disappearing = carryover = existing
        # ie., existing = present-new
    return char_evol

def get_evol_graphs(fro, to, char_evol): #boo_start, boo_end
    existing = [] # of len range with each element=length of char list at that chapter<=>index
    intro =[]
    disappearing = []
    all_chaps = components.get_all_chaps()
    for i in range(fro, to):
        present, dis, new = char_evol[all_chaps[i]]
        exist = [word for word in present if word not in new] 
        existing.append(len(exist))
        intro.append(len(new))
        disappearing.append(len(dis))
    legends = ["existing", "introduced", "disappearing"]
    fig, ax = plt.subplots(1, 1)
    ax.plot(existing)
    ax.plot(intro)
    plt.plot(disappearing)
    plt.legend(legends)
    maxs = [max(existing), max(intro), max(disappearing)]
    x_labels_evol = [i for i in range(fro, to, 10)]
    x_evol = [i for i in range(0, to-fro, 10)]
    # y_labels = [i for i in range(fro, to, 5)]
    y_evol = [i for i in range(0, max(maxs) + 5, 5)]
    plt.xticks(x_evol, x_labels_evol) 
    plt.yticks(y_evol)
    try:
        ax.figure.savefig("/tmp/evol_plot.png")
    except:
        ax.figure.savefig("evol_plot.png")

