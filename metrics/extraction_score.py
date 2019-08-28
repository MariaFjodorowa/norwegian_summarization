"""
Usage:
  extraction_score.py <src> <predpath>

Options:
  src  ожидаемые саммари
  predpath  предсказанные саммари

"""
from math import exp, e
from docopt import docopt
from difflib import SequenceMatcher
from tqdm import tqdm

LONG_SEQ_THRESHOLD = 16



def count_extraction_score(testarticle, testsummary):
    matcher = SequenceMatcher(None, testarticle, testsummary)
    matching = matcher.get_matching_blocks()
    P_ACS_s = []
    for match in matching:
        s = match.size
        if s > LONG_SEQ_THRESHOLD:
            s = s / len(testsummary)
            P_ACS_s.append(s*(exp(s-1)-(1-s)/e))
    return round(sum(P_ACS_s), 3)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    with open(arguments['<src>'], 'r', encoding='utf-8') as src:
        source = src.readlines()
    with open(arguments['<predpath>'], 'r', encoding='utf-8') as predpath:
        predicted = predpath.readlines()
    scores = []
    count_extr = 0
    for i, (src, pred) in enumerate(tqdm(zip(source, predicted))):
        score = count_extraction_score(src.strip(), pred.strip())
        scores.append(score)
    print("Average extraction_score: {0}".format(sum(scores) / len(scores), 3))
