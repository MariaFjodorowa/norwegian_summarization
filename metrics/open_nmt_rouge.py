"""
Usage:
  open_nmt_rouge.py <goldpath> <predpath> <outpath>

Options:
  goldpath  ожидаемые саммари
  predpath  предсказанные саммари
  outpath  куда сохранить саммари с rouge
"""

from docopt import docopt
from tqdm import tqdm
from rouge import Rouge
from collections import defaultdict
import os

def unbpe(text):
    tokens = text.split()
    words = []
    for token in tokens:
        if not token.startswith("▁") and words:
            words[-1] += token
        else:
            words.append(token)
    if not words:
        words = ["▁"]
    return " ".join(words)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    predpath, goldpath = arguments['<predpath>'], arguments['<goldpath>']

    scores = {"rouge-1": defaultdict(list),
              "rouge-2": defaultdict(list),
              "rouge-l": defaultdict(list)}
    with open(predpath, 'r', encoding='utf-8') as predictions:
        predicted = predictions.readlines()

    with open(arguments['<goldpath>'], 'r', encoding='utf-8') as gold:
        gold_sum = gold.readlines()
    rouge = Rouge()
    outpath = arguments['<outpath>']
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    for i, (summary, abstract) in enumerate(tqdm(zip(predicted, gold_sum))):
        #summary = unbpe(summary)
        #abstract = unbpe(abstract)
        try:
            rouge_score = rouge.get_scores(summary, abstract)
        except Exception as e:
            print(i, e)
            continue
        for metric, score in rouge_score[0].items():
            for key, value in score.items():
                scores[metric][key].append(value)
        with open(os.path.join(outpath, "{0}.txt".format(i)), 'w', encoding='utf-8') as outfile:
            outfile.write(summary + ' ' + str(rouge_score) + '\n')
    line = '\n|'+outpath+'|'
    with open('../results.md', 'a', encoding='utf-8') as results:
        for metric, score in scores.items():
            print(metric)
            for k, v in score.items():
                v = str(round((sum(v) / len(v)), 4))
                print(k + ' ' + v)
                line += (v + '|')
        results.write(line)
