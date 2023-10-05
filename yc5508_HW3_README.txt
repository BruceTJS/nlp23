
yc5508_HW3_README.txt


Introduction:

This README provides instructions on how to run the Part-of-Speech (POS) tagging system. The tagger is based on the Hidden Markov Model (HMM) and uses the Viterbi algorithm for predictions. The Penn Treebank tagging scheme has been adopted for this task.


Files Included:

yc5508_train_HW3.py: Contains functions to calculate likelihood tables and prior probabilities.
yc5508_main_HW3.py: Main file to run the system, which imports and uses functions from yc5508_train_HW3.py.

How to Run the System:

Navigate to the directory containing the Python files.

Use the following command to run the tagger:

python3 yc5508_train_HW3.py training_filename testing_filename output_filename

Replace your_training_module_name with the name of the module (or file) containing your training functions.

The results will be written to path_to_output_file in the format word\ttag.

Handling Out Of Vocabulary (OOV) Items:

For words that were not seen in the training data (OOV words), a strategy has been implemented to handle them:

A constant probability is given to OOV words to handle the zero probability issue in the Viterbi algorithm. This ensures that even if the word is not recognized, the sentence can still be tagged.
This method was chosen for its simplicity and effectiveness. It's a common strategy to address OOV items, especially in the absence of a richer feature set or morphological clues.
