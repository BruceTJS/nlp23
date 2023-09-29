def read_training_file(file_path):
    with open(file_path, 'r') as file:
        sentences = []
        sentence = []
        for line in file:
            if line.strip() == "":
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            else:
                token, tag = line.strip().split("\t")
                sentence.append((token, tag))
        if sentence:
            sentences.append(sentence)
    return sentences[0]
def read(file_path):
    with open(file_path, 'r') as file:
        sentence = []
        for line in file:
            if line.strip() !="":
                token, tag = line.strip().split("\t")
                sentence.append((token, tag))
    return sentence
def reade(file_path):
    with open(file_path, 'r') as file:
        sentence = []
        for line in file:
            if line.strip() != "":
                l=line.strip()
                sentence.append(l.replace('\t',''))
    return sentence
s=read("TS.txt")

se=reade("TS.txt")
#s=read_training_file("TS.txt")
print(s)
print('------------------------------------------------')
print(se)