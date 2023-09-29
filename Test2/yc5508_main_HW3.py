import yc5508_trainHMM_HW3 as trainHMM

def read_training_file(file_path):
    with open(file_path, 'r') as file:
        sentence = []
        for line in file:
            if line.strip() !="":
                token, tag = line.strip().split("\t")
                sentence.append((token, tag))
    return sentence

def read_testing_file(file_path):
    with open(file_path, 'r') as file:
        sentences = []
        sentence = []
        for line in file:
            if line.strip() == "":
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            else:
                token = line.strip()
                sentence.append(token)
        if sentence:
            sentences.append(sentence)
    return sentences

def main():
    training_filepath = 'WSJ_02-21.pos'  # Replace 
    texting_filepath = 'WSJ_24.words'  # Replace 
    training_corpus = read_training_file(training_filepath)
    testing_data = read_testing_file(texting_filepath)

    # Step 3: Calculate Prior Probabilities
    prior_probabilities = trainHMM.calculate_prior_probabilities(training_corpus)
    
    # Step 4: Create Likelihood Table
    likelihood_table = trainHMM.create_likelihood_table(training_corpus)
    
    # Step 5: List Words and Handle OOV
    unique_words = trainHMM.get_unique_words(training_corpus)
    
    
    # Here, run the Viterbi algorithm and other steps for the development corpus using the calculated probabilities and tables.
    # You will likely need to add a function to your training and model file for running Viterbi and call it here.
    # Then, compare the result with the true tags to calculate the accuracy on the development set.
    
    # When you are ready, repeat the process for the test corpus.
    
    # Write the output to the submission.pos file
    with open('submission.pos', 'w') as output_file:
        # Iterate over the sentences in your test corpus output and write each word and its predicted tag to the file.
        for sentence in tagged_sentences:
            for token, tag in sentence:
                output_file.write(f"{token}\t{tag}\n")
            output_file.write("\n")  
if __name__ == "__main__":
    main()
