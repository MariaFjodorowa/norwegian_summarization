"""
Usage:
  textrank.py <path> <outpath>

Options:
  path     csv с текстами и саммари
  outpath  куда сохранить полученные саммари
"""

from summa.summarizer import summarize  # https://github.com/summanlp/textrank
import csv
from docopt import docopt
from tqdm import tqdm
from rouge import Rouge
import os
from collections import defaultdict
csv.field_size_limit(100000000)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    outpath = arguments['<outpath>']
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    scores = {"rouge-1": defaultdict(list),
              "rouge-2": defaultdict(list),
              "rouge-l": defaultdict(list)}
    with open(arguments['<path>'], 'r', encoding='utf-8') as csvfile:
        rouge = Rouge()
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(tqdm(csvreader)):
            abstract, article = row[1], row[2]
            summary = summarize(article, language='norwegian')
            if summary:
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
    for metric, score in scores.items():
        print(metric)
        for k, v in score.items():
            print(k + ' ' + str(round((sum(v) / len(v)),3)))
