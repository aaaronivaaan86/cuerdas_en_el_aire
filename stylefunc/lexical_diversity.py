def lexical_diversity(text):
    print('Total of words: ' +  str(len(text))   )
    print('Total of words whitout repetiotion:'+  str(len(set(text)))  )
    # length of tokens in a text divided by length of the tokens ia text without repetition 
    return len(text) / len(set(text))

def lexical_diversity_percentage(count, total):
    # token frequency divided by total of tokens
    return 100 * count / total
