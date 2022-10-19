# Ambiguity Sentence Identifier
import spacy

nlp = spacy.load("en_core_web_sm")
print('INFO: spaCy initialized successfully.')


def get_quantifier(sentence, quantifiers):
    doc = nlp(sentence)
    dep = ['det', 'poss', 'advmod', 'nmod', 'nsubj', 'nsubjpass', 'ROOT']
    for token in doc:
        for quantifier in quantifiers:
            if (quantifier in token.text.lower()) and (token.dep_ in dep):
                if token.text != 'know':
                    return token
    return None


def assoc_negation_exists(sentence, q_root):
    doc = nlp(sentence)
    for token in doc:
        if token.dep_ == 'neg':
            if (token.head.text == q_root.text and token.head.i == q_root.i) or (
                    token.head.head.text == q_root.text and token.head.head.i == q_root.i):
                return True
    return False


def get_q_root(quantifier):
    case_1 = ['nsubj', 'nsubjpass']
    case_2 = ['det', 'poss', 'advmod', 'nmod']
    dep = quantifier.dep_

    q_head = quantifier.head
    if dep in case_1:
        if q_head.dep_ == 'nsubj' or q_head.dep_ == 'auxpass':
            return q_head.head
        else:
            return q_head
    elif dep in case_2:
        return q_head.head


def reversed_traversal(sentence, quantifiers):
    doc = nlp(sentence)
    negation = None
    for token in doc:
        if token.dep_ == 'neg' or token.dep_ == 'preconj':
            negation = token
    if negation == None:
        return False

    ancestor = negation
    while ancestor != ancestor.head:
        ancestor = ancestor.head

    for quantifier in quantifiers:

        if ancestor.dep_ == 'ROOT' and quantifier in ancestor.text:
            return True
        for token in doc:
            if token.head == ancestor and quantifier in token.text and token.i < ancestor.i:
                return True

    return False


def is_quantifier_negation(sentence, quantifiers):
    quantifier = get_quantifier(sentence, quantifiers)
    if quantifier is None:
        return False
    if reversed_traversal(sentence, quantifiers):
        return True
    q_root = get_q_root(quantifier)
    if assoc_negation_exists(sentence, q_root):
        return True

    return False

def find_quantifier_negation(sentences, quantifiers):
    print('INFO: Beginning search for quantifier + negation statements.')
    ret = []
    i = 0
    indices = []
    for sentence in sentences:
        if is_quantifier_negation(sentence, quantifiers):
            ret.append(sentence)
            indices.append(i)
        i = i+1
    print('INFO: Search completed with ' + str(len(ret)) + ' potential quantifier + negations.')
    print("\n")
    return ret, indices

def get_context(sentences, indices):
    ret = []
    for index in indices:
        start = index - 3
        end = index + 2
        if start <= 0:
            start = 0
        elif end > len(sentences):
            end = len(sentences)
        for i in range(start, end):
            ret.append(sentences[i])
        ret.append('**********')
    return ret

def read_csv(csv):
    print('INFO: Reading ' + csv + '.')
    sentences = []
    with open(csv, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            sentences.append(row[0])
    print('INFO: Successfully imported ' + str(len(sentences)) + ' sentences from ' + csv + '.')
    return sentences

def read_txt(txt):
    print('INFO: Reading ' + txt + '.')
    read_obj = open(txt, 'r')
    lines = read_obj.read().splitlines()
    sentences = []
    for line in lines:
        if line != '':
            sentences.append(line)

    print('INFO: Successfully imported ' + str(len(sentences)) + ' sentences from ' + txt + '.')

    return sentences

if __name__ == '__main__':
    pass
