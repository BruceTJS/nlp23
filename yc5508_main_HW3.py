import sys
import yc5508_Train_HW3 as hm

def read_corpus(file_path):
    with open(file_path, 'r') as f:
        tagged_sentences = []
        sentence = []
        for line in f.readlines():
            line = line.strip()
            if not line:  # skip empty lines
                continue
            
            word, tag = line.split('\t')
            
            # If the line represents the end of a sentence, 
            # add the current sentence to tagged_sentences and start a new sentence
            if word == '.' and tag == '.':
                if sentence:  # if the sentence is not empty
                    tagged_sentences.append(sentence)
                sentence = []  # start a new sentence
            else:
                sentence.append((word, tag))  # add the word, tag tuple to the current sentence
                
        # Don't forget to add the last sentence if it's not empty
        if sentence:
            tagged_sentences.append(sentence)
            
    return tagged_sentences


def read_test_file(file_path):
    """Reads the testing file and returns a list of sentences, where each sentence is a list of words."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    sentences = []
    sentence = []
    
    for line in lines:
        stripped_line = line.strip()
        
        # If the line is empty, it's the end of a sentence
        if not stripped_line:
            if sentence:  # if there's content in the current sentence, append it to sentences
                sentences.append(sentence)
                sentence = []
            continue
        
        # Extract the word (ignoring tags since they're absent in test files)
        word = stripped_line
        sentence.append(word)
    
    # Append the last sentence if there's any remaining content
    if sentence:
        sentences.append(sentence)
        
    return sentences



def write_output_file(testing_sentences, prior_probabilities, likelihood_table, file_path):
    with open(file_path, 'w') as f:
        for sentence in testing_sentences:
            predicted_tags = hm.viterbi_algorithm(sentence, prior_probabilities, likelihood_table)
            for word, tag in zip(sentence, predicted_tags):
                f.write(f"{word}\t{tag}\n")
            f.write("\n")  # separate sentences by a newline


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 main_NETID_HW3.py <training_filename> <testing_filename> <output_filename>")
        return

    training_file_name = sys.argv[1]
    testing_file_name = sys.argv[2]
    output_file_name = sys.argv[3]

    # Read the training data
    training_data = read_corpus(training_file_name)

    # Generate the prior probabilities and likelihood tables
    prior_probabilities = hm.calculate_prior_probabilities(training_data)
    likelihood_table = hm.calculate_likelihood_table(training_data)

    # Read the testing data
    testing_sentences = read_test_file(testing_file_name)

    # Process each sentence with the Viterbi algorithm

    # Write the output to a file
    write_output_file(testing_sentences, prior_probabilities, likelihood_table, output_file_name)

if __name__ == "__main__":
    main()

