## Python modules
import nltk
import math
from matplotlib import pyplot as plt

## Our Module
from stylefunc.files_into_strings import files_into_strings
from stylefunc.lexical_diversity  import *
from stylefunc.lexical_treemap import get_token_stanford_tags
from stylefunc.lexical_network import *

##* Declare variables
bolivar_papers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
text_by_author = {}
essay_tokens = {}
essay_tokens_length_distribution = {}
filter_essay_tokens_length_distribution = {}
sentence_avgs = []

whole_corpus = []
bolivar_trigrams = list()


##* Get files as strings
for paper in bolivar_papers:
    text_by_author[str(paper)]  = files_into_strings(str(paper))

## TODO: uncomment if you want all lines in one plot
# plt.ion()
## loop over each essay as strings
for essay in bolivar_papers:    
    ##* TOKENIZE essays
    tokens = nltk.word_tokenize(text_by_author.get(str(essay)), 'spanish')

    ## * FREQUENCY DISTRIBUTION
    eche_essay_freq_dist = nltk.FreqDist(tokens)
    sentence_length_counter =  eche_essay_freq_dist[','] 
    + eche_essay_freq_dist['.']
    + eche_essay_freq_dist[';']
    + eche_essay_freq_dist['¿']
    + eche_essay_freq_dist['?']
    + eche_essay_freq_dist['!']
    + eche_essay_freq_dist['¡']
    + eche_essay_freq_dist['(']
    + eche_essay_freq_dist[')']
    + eche_essay_freq_dist['-']

   # Filter punctuation marks
    essay_tokens[essay] = ([token for token in tokens
                            if any(c.isalpha() for c in token  )])
    
    # add filtered tokens to whole corpus
    whole_corpus += essay_tokens[essay]
    
    # ## * GET LEXICAL DIVERSITY BY ESSAY
    # print( 'Lexical Diversity: ' ,lexical_diversity(essay_tokens[essay]))
    # print( 'Lexical Diversity Percetage : ', lexical_diversity_percentage(tokens.count('valor'), len(essay_tokens[essay])))    
    
    ## * GET SENTENCE LENGTH AVERANVE
    # print( 'Sentence AVG: ', len(essay_tokens[essay]) /  sentence_length_counter)
    # append each averange and at finish calculate the averange of averanges
    sentence_avgs.append(len(essay_tokens[essay]) /  sentence_length_counter)

    ## * GET TOKEN LENGTH DIST
    # recalculate freq without marks 
    # eche_essay_freq_dist = nltk.FreqDist(essay_tokens[essay])
    # essay_tokens_length_distribution = nltk.FreqDist([ len(token) for token in  essay_tokens[essay]])

    ## TODO: plot graph
    #essay_tokens_length_distribution.plot(30,title='Token Length Distribution by Essay',  label=essay )
    # eche_essay_freq_dist.plot(50)
    bolivar_trigrams.append(get_trigrams(tokens))


## TODO: uncomment if you want all line in one plot, related to line 58
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# plt.ioff()
# plt.show()

## ? WHOLE CORPUS BEGIN
# print('* * WHOLE CORPUS * *')
# * GET WHOLE CORPUS LEXICAL DIVERSITY 
print( 'WHOLE CORPUS Lexical Diversity: ' ,lexical_diversity(whole_corpus))
print( 'WHOLE CORPUS Lexical Diversity Percetage (modernidad) : ', lexical_diversity_percentage(whole_corpus.count('modernidad'), len(whole_corpus)))
print( 'WHOLE CORPUS Lexical Diversity Percetage (valor) : ', lexical_diversity_percentage(whole_corpus.count('valor'), len(whole_corpus)))
print( 'WHOLE CORPUS Lexical Diversity Percetage (uso) : ', lexical_diversity_percentage(whole_corpus.count('uso'), len(whole_corpus)))
print( 'WHOLE CORPUS Lexical Diversity Percetage (cambio) : ', lexical_diversity_percentage(whole_corpus.count('cambio'), len(whole_corpus)))
print( 'WHOLE CORPUS Lexical Diversity Percetage (ethos) : ', lexical_diversity_percentage(whole_corpus.count('ethos'), len(whole_corpus)))

# get sentence averange
sentence_avg = sum(sentence_avgs) / len(sentence_avgs)
print('Sentece Averange: ' + str(sentence_avg))

# ## * GET FREQ DIST
whole_freq_dist =  nltk.FreqDist(whole_corpus)

# ## * GET FREQ DIST LENGTH
whole_corpus_token_length_dist = nltk.FreqDist(  [len(token) for token in whole_corpus]   )

# ## TODO: plot graph Whole Token Length Dist
# whole_freq_dist.plot(100, title= 'Most common 100')
# whole_corpus_token_length_dist.plot(20,title= 'Whole Corpus Token Length Dist')

## * GET DISPERTION PLOT
# whole_corpus_text = nltk.Text(whole_corpus)
# whole_corpus_text.dispersion_plot(['valor', 'uso', 'cambio', 'vida', 'muerte', 'sí', 'no', 'ethos', 'barroco' ])

## *  TREEMAP STAMPS, LEXICAL AND GRAMMAR ANALYSIS
whole_freq_dist_most_common = whole_freq_dist.most_common(100)
get_token_stanford_tags(whole_freq_dist_most_common)

# ## * GET NETWORK CHART
# get_network_chart(trigram_freq(bolivar_trigrams))



