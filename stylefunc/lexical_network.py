import nltk
import math
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
from nltk.tag import StanfordNERTagger
from nltk.tag import StanfordPOSTagger
from itertools import groupby

from stylefunc.stanford_tagger import *

# MODELS
from models.tree_el import TreeMapEl

signs = ('“', '”', "(", ")", ",", ".")
bolivar_trigrams = list()
finder_ratio = 50
words = list()
token_freq_dic = list()

def get_trigrams(tokens):
    filter_words = [w for w in tokens if w not in signs]
    trigram_finder = TrigramCollocationFinder.from_words(filter_words)
    return list(trigram_finder.nbest(TrigramAssocMeasures.likelihood_ratio, finder_ratio))

    
def trigram_freq(trigrams):
    results = {}
    for trigram in trigrams:
        for t in trigram:
            if t[0] == 'de':
                words.append(t[2])

    results = { value: len(list(freq)) for value, freq in groupby(sorted(words)) }
    tags = get_sort_stanford_tags(results)
    
    for r in results.items():
        for e in tags:
            if r[0] == e[0]:
                token_freq_dic.append(TreeMapEl(r[0], r[1], e[1]))
                break

    tuples_list = sorted(token_freq_dic, key=lambda x: x.freq, reverse=True)
    return tuples_list

def get_network_chart(tuples_list):
    eche_graph =nx.Graph()
    eche_graph.add_nodes_from(tuples_list)
    eche_graph.add_node(TreeMapEl("de la", eche_graph.number_of_nodes() - 2, "x"))
    
    end_node = eche_graph.number_of_nodes()

    for n in list(eche_graph.nodes):
        eche_graph.add_edge(end_node, n)

    # print( eche_graph.number_of_nodes())
    # print("Nodes / Edges")
    # print( eche_graph.number_of_edges())

    node_colors = get_boliver_graph_colors(tuples_list)[0]
    edge_colors = get_boliver_graph_colors(tuples_list)[1]
    graph_lables = get_boliver_graph_colors(tuples_list)[2]

    nx.draw(eche_graph, node_color = node_colors, edge_color = edge_colors, labels=graph_lables, with_labels = True)
    plt.show()

def get_boliver_graph_colors(tuples_list):
    node_colors = []
    edge_colors = []
    graph_labels = {}
    ## categories = ('Adjectives','Conjunctions','Determiners','Interjections','Nouns','Pronouns','Adverbs','Prepositions','Verbs','Dates','Numerals')
    color_cat = {
        'a': "#829FD9", # blue
        'c': "#027368", # dark green
        'd': "#BFB634", 
        'i': "#574F73",
        'n': "#8BBDC8", # light blue
        'p': "#F27777",
        'r': "#F2D5D5",
        's': "#C9C95A", # green
        'v': "#E1473D", # red
        'w': "#FBD099",
        'z': "#3B2F39"
    }

    for t in tuples_list:
        node_colors.append(color_cat.get(t.tag[0], '#D89A47'))
        edge_colors.append(color_cat.get(t.tag[0], '#D89A47'))
        graph_labels[t] = (t.token).strip() + ": " + str(t.freq)
    
        # print(color_cat.get(t.tag[0], '#D89A47'), (t.token).strip() + ": " + str(t.freq))

    node_colors.append("#D89A47")
    node_colors.append("#D89A47")
        
    edge_colors.append("#3B2F39")
    return (node_colors, edge_colors, graph_labels)
