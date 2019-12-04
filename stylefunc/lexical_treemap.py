from matplotlib import pyplot as plt
import matplotlib.colors as mpcolors
import  matplotlib.cm as cm
import numpy as np
import squarify

from stylefunc.stanford_tagger import *

# MODELS
from models.tree_el import TreeMapEl

cmap = cm.gist_rainbow
# cmap = cm.rainbow # Another color possibility

cat_list = []
categories = ('Adjectives','Conjunctions','Determiners','Interjections','Nouns','Pronouns','Adverbs','Prepositions','Verbs','Dates','Numerals')
cat_leters = ('a','c','d','i','n','p','r','s','v','w','z')

for c  in categories:
    cat_list.append(list())

def get_token_stanford_tags(most_common):
    token_freq_dic = {}
    freqs = []
    data_labels = []
    
    # build token_freq_dic
    for token_value in most_common:
        token_freq_dic.update({token_value[0]: TreeMapEl(token_value[0], token_value[1], "")})

    # build cat list
    get_token_tag(token_freq_dic)

    # get charts
    get_chart_by_tag()


def get_token_tag(token_freq_dic):
    # get tags
    tags = get_stanford_tags(token_freq_dic.keys())
    
    # assgn tag
    for token_value in token_freq_dic.values():
        for tag in tags:
            if token_value.token == tag[0]:
                token_value.tag = tag[1]
                break
        cat_list_append(token_value)


def cat_list_append(value):
    for index, cat in enumerate(cat_leters):
        if value.tag.startswith(cat):
            cat_list[index].append(value)


def get_chart_by_tag():
    plt.axis('off')
    counter = 0
    for sublist in cat_list:
        chart_labels = list()
        chart_data = list()
        for item in sublist:
            # print(item.token + " : " + item.tag + " : " +  str(item.freq))
            chart_labels.append(item.token + " : " + item.tag + " : " +  str(item.freq))
            chart_data.append(item.freq)            
            # print(i.token, i.freq, i.tag)
        chart_title = categories[counter]
        
        min_val = min(chart_data, default= 0)
        max_val = max(chart_data, default= 0)
        norm = mpcolors.Normalize(vmin=min_val, vmax=max_val)
        colors = [cmap(norm(value)) for value in chart_data]
    
        squarify.plot(sizes= chart_data, label=chart_labels, color=colors, alpha=.6,  text_kwargs={'fontsize':9})
        
        plt.title(chart_title)
        plt.show()
        counter = counter + 1