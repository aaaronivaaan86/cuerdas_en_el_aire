## Python modules
import nltk
import math
from matplotlib import pyplot as plt
## Our Module
from stylefunc.files_into_strings import files_into_strings

authors = {'Bolivar', 'Marx', 'Benjamin'}
papers =  {
    'Bolivar': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'Marx': [16],
    'Benjamin': [17]
}

text_by_author_token = {}
whole_corpus = []

##* Building the corpus 
for author, files in papers.items():
    for f in files:
        text_by_author_token[author] = files_into_strings(f)
# print(text_by_author_token.get('Marx'))

# Combine every paper except our test case into a single corpus
for author in authors:
    tokens = nltk.word_tokenize(text_by_author_token[author])
    text_by_author_token[author] = ([token for token in tokens 
                                            if any(c.isalpha() for c in token)])
    whole_corpus += text_by_author_token[author]

# Get a frequency distribution
whole_corpus_freq_dist = list(nltk.FreqDist(whole_corpus).most_common(500) )
# print('Delta Method Beggin. whole_corpus_freq_dist')
# print(whole_corpus_freq_dist[:10])

## //* Calculating features for each subcorpus
## The main data structure
features = [word for word,freq in whole_corpus_freq_dist[:500]]
feature_freqs = {}
print('Delta Method Beggin. features')

for author in authors:
    # A dictionary for each candidate's features
    feature_freqs[author] = {} 
    
    # A helper value containing the number of tokens in the author's subcorpus
    overall = len(text_by_author_token[author])
    print("Overall by author " + author + ": " +  str(overall) )
    
    # Calculate each feature's presence in the subcorpus
    for feature in features:
        presence = text_by_author_token[author].count(feature)
        feature_freqs[author][feature] = presence / overall
        # print("feature_freqs by Author by feature")
        # print(feature_freqs[author][feature])
# print("Benjamin frequency: " )
# print(feature_freqs['Benjamin'])


# //* Calculating feature mean and standard deviations
print("##### Standar derivation  ######")
# The data structure into which we will be storing the "corpus standard" statistics
corpus_features = {}
# For each feature...
for feature in features:
    # Create a sub-dictionary that will contain the feature's mean 
    # and standard deviation
    corpus_features[feature] = {}
    
    # Calculate the mean of the frequencies expressed in the subcorpora
    feature_average = 0
    for author in authors:
        feature_average += feature_freqs[author][feature]
    feature_average /= len(authors)
    corpus_features[feature]["Mean"] = feature_average
    # print("corpus_features MEAN: " + str(corpus_features[feature]["Mean"])  )
    #print(corpus_features[feature]["Mean"])
    
    #Calculate the standard deviation using the basic formula for a sample
    feature_stdev = 0
    for author in authors:
        diff = feature_freqs[author][feature] - corpus_features[feature]["Mean"]
        feature_stdev += diff*diff
    feature_stdev /= (len(authors) - 1)
    feature_stdev = math.sqrt(feature_stdev)
    corpus_features[feature]["StdDev"] = feature_stdev
    # print( "StdDev: " + str(corpus_features[feature]["StdDev"])  )


# //*  Calculating z-scores
feature_zscores = {}
for author in authors:
    feature_zscores[author] = {}
    for feature in features:        
        # Z-score definition = (value - mean) / stddev
        # We use intermediate variables to make the code easier to read
        feature_val = feature_freqs[author][feature]
        feature_mean = corpus_features[feature]["Mean"]
        feature_stdev = corpus_features[feature]["StdDev"]
        feature_zscores[author][feature] = ((feature_val-feature_mean) / 
                                            feature_stdev)

# //* Calculating features and z-scores for our test case
# Tokenize the test case
testcase_tokens = text_by_author_token["Bolivar"]
# Filter out punctuation and lowercase the tokens
testcase_tokens = [token.lower() for token in testcase_tokens 
                   if any(c.isalpha() for c in token)]
 
# Calculate the test case's features
overall = len(testcase_tokens)
testcase_freqs = {}
for feature in features:
    presence = testcase_tokens.count(feature)
    testcase_freqs[feature] = presence / overall
    
# Calculate the test case's feature z-scores
testcase_zscores = {}
for feature in features:
    feature_val = testcase_freqs[feature]
    feature_mean = corpus_features[feature]["Mean"]
    feature_stdev = corpus_features[feature]["StdDev"]
    testcase_zscores[feature] = (feature_val - feature_mean) / feature_stdev
    # print("Test case z-score for feature", feature, "is", testcase_zscores[feature])


# //* Calculating Delta
for author in authors:
    delta = 0
    for feature in features:
        delta += math.fabs((testcase_zscores[feature] - 
                            feature_zscores[author][feature]))
    delta /= len(features)
    print( "Delta score for candidate", author, "is", delta )




