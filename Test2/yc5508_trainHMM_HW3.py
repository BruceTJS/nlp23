from collections import defaultdict


def calculate_prior_probabilities(corpus):
    """
    Calculate the prior probabilities of each tag bigram.
    """
    bigram_counts = defaultdict(int)
    tag_counts = defaultdict(int)
    
    for sentence in corpus:
        previous_tag = None
        for _, tag in sentence:
            if previous_tag is not None:
                bigram_counts[(previous_tag, tag)] += 1
            tag_counts[tag] += 1
            previous_tag = tag
            
    prior_probabilities = defaultdict(float)
    for (tag_i, tag_j), count in bigram_counts.items():
        prior_probabilities[(tag_i, tag_j)] = count / tag_counts[tag_i]
        
    return prior_probabilities


def create_likelihood_table(corpus):
    """
    Create a likelihood table for each word with each POS tag.
    """
    word_tag_counts = defaultdict(int)
    tag_counts = defaultdict(int)
    
    for sentence in corpus:
        for word, tag in sentence:
            word_tag_counts[(word, tag)] += 1
            tag_counts[tag] += 1
    
    likelihood_table = defaultdict(float)
    for (word, tag), count in word_tag_counts.items():
        likelihood_table[(word, tag)] = count / tag_counts[tag]
        
    return likelihood_table


def get_unique_words(corpus):
    """
    Extract a set of all unique words found in the training corpus.
    """
    unique_words = set()
    for sentence in corpus:
        for word, _ in sentence:
            unique_words.add(word)
    return unique_words


# The Viterbi algorithm implementation and the handling of OOV items can be added here.

def viterbi_algorithm(sentence, unique_words, prior_probabilities, likelihood_table):
    """
    Implement Viterbi algorithm to tag a sentence.
    """
    # Initialization
    n = len(sentence)
    states = list(prior_probabilities.keys())
    viterbi = defaultdict(lambda: defaultdict(float))
    backpointer = defaultdict(lambda: defaultdict(str))
    oov_prob=0.0001
    # Handle the first word
    word_0 = sentence[0]  # You might decide to assign a different initial probability for OOV words.
    for state in states:
        if word_0 not in unique_words:
            # Handle OOV word
            viterbi[state][0] = oov_prob  
        else:
            viterbi[state][0] = prior_probabilities[state] * likelihood_table.get((word_0, state), 0)
    
    # Recursive step
    for t in range(1, n):
        word_t = sentence[t]
        for state in states:
            max_prob = float('-inf')
            max_state = ""
            for previous_state in states:
                prob = viterbi[previous_state][t - 1] * prior_probabilities.get((previous_state, state), 0)
                if word_t not in unique_words:
                    # Handle OOV word
                    prob *= oov_prob
                else:
                    prob *= likelihood_table.get((word_t, state), 0)
                if prob > max_prob:
                    max_prob = prob
                    max_state = previous_state
            viterbi[state][t] = max_prob
            backpointer[state][t] = max_state
    
    # Termination step
    best_path = []
    max_prob = float('-inf')
    best_last_state = ""
    for state in states:
        if viterbi[state][n - 1] > max_prob:
            max_prob = viterbi[state][n - 1]
            best_last_state = state
    best_path.append(best_last_state)
    
    # Backtrack to find the best path
    for t in range(n - 1, 0, -1):
        best_last_state = backpointer[best_last_state][t]
        best_path.insert(0, best_last_state)
    
    return best_path  # Returns the best sequence of states (tags) for the given sentence.

