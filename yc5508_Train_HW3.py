from collections import defaultdict

def calculate_prior_probabilities(tagged_sentences):
    transitions = defaultdict(lambda: defaultdict(int))
    for sentence in tagged_sentences:
        previous_tag = "<s>"
        for _, tag in sentence:
            transitions[previous_tag][tag] += 1
            previous_tag = tag
        transitions[previous_tag]["</s>"] += 1  # marking the end of sentence

    # Convert counts to probabilities
    for prev_tag, next_tags in transitions.items():
        total_transitions = sum(next_tags.values())
        for next_tag, count in next_tags.items():
            transitions[prev_tag][next_tag] = count / total_transitions

    return transitions

def calculate_likelihood_table(tagged_sentences):
    word_tag_frequency = defaultdict(lambda: defaultdict(int))
    word_frequency = defaultdict(int)

    # Count occurrences of word-tag pairs
    for sentence in tagged_sentences:
        for word, tag in sentence:
            word = word.lower()  # Convert word to lowercase
            word_tag_frequency[word][tag] += 1
            word_frequency[word] += 1

    # Convert counts to probabilities
    likelihood_table = defaultdict(dict)
    for word, tags in word_tag_frequency.items():
        for tag, count in tags.items():
            likelihood_table[word][tag] = count / word_frequency[word]

    return likelihood_table

def viterbi_algorithm(sentence, prior_probabilities, likelihood_table):
    num_states = len(prior_probabilities)
    num_words = len(sentence)

    # Setting up tables for storing probabilities and back-pointers.
    dp = defaultdict(lambda: defaultdict(float))
    backpointer = defaultdict(lambda: defaultdict(str))

    # Initialization step
    for tag in prior_probabilities:
        dp[tag][0] = prior_probabilities['<s>'].get(tag, 0) * likelihood_table[sentence[0]].get(tag, 0.0001)

    # Recursion step
    for t in range(1, num_words):
        for tag in prior_probabilities:
            max_prob, best_prev_tag = max(
                [(dp[prev_tag][t-1] * prior_probabilities[prev_tag].get(tag, 0) * likelihood_table[sentence[t]].get(tag, 0.0001), prev_tag) 
                for prev_tag in prior_probabilities]
            )
            dp[tag][t] = max_prob
            backpointer[tag][t] = best_prev_tag

    # Termination step: find best tag for the last word
    best_last_tag = max(dp, key=lambda tag: dp[tag][num_words-1])

    # Backtrack to find best tag sequence
    best_path = [best_last_tag]
    for t in range(num_words-1, 0, -1):
        best_last_tag = backpointer[best_last_tag][t]
        best_path.insert(0, best_last_tag)

    return best_path



def get_unique_words(tagged_sentences):
    return set(word for sentence in tagged_sentences for word, _ in sentence)
