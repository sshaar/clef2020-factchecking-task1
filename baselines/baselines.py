import pdb
import pandas as pd
import random
import numpy as np
import os
from os import listdir
from os.path import join, dirname

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

import sys
sys.path.append('.')

from scorer.main import evaluate
from format_checker.main import check_format

import requests, time
from functools import reduce

random.seed(0)
ROOT_DIR = dirname(dirname(__file__))

# topic_id tweet_id score run_id
def run_random_baseline(data_fpath):
    results_fpath = join(ROOT_DIR, 'baselines/data/task1_random_baseline_%s'%(os.path.basename(data_fpath)))
    gold_df = pd.read_csv(data_fpath, sep='\t')
    with open(results_fpath, "w") as results_file:
        for i, line in gold_df.iterrows():
            results_file.write('{}\t{}\t{}\t{}\n'.format(line['topic_id'], line['tweet_id'], 
                random.random(), "random"))


def run_ngram_baseline(train_fpath, test_fpath):
    train_df = pd.read_csv(train_fpath, sep='\t')
    test_df = pd.read_csv(test_fpath, sep='\t')

    pipeline = Pipeline([
        ('ngrams', TfidfVectorizer(ngram_range=(1, 1))),
        ('clf', SVC(C=1, gamma=0.75, kernel='rbf', random_state=0))
    ])
    pipeline.fit(train_df['tweet_text'], train_df['claim_worthiness'])

    results_fpath = join(ROOT_DIR, 'baselines/data/task1_ngram_baseline_%s'%(os.path.basename(test_fpath)))
    with open(results_fpath, "w") as results_file:
        predicted_distance = pipeline.decision_function(test_df['tweet_text'])
        for i, line in test_df.iterrows():
            dist = predicted_distance[i]
            results_file.write("{}\t{}\t{}\t{}\n".format(line['topic_id'], line['tweet_id'], 
                dist, "ngram"))


def run_baselines():
    train_fpath = join(ROOT_DIR, 'data/training.tsv')
    test_fpath = join(ROOT_DIR, 'data/dev.tsv')


    run_random_baseline(test_fpath)
    random_baseline_fpath = join(ROOT_DIR, 'baselines/data/task1_random_baseline_%s'%(os.path.basename(test_fpath)))
    if check_format(random_baseline_fpath):
        thresholds, precisions, avg_precision, reciprocal_rank, num_relevant = evaluate(test_fpath, random_baseline_fpath)
    print("Random Baseline AVGP:", avg_precision)

    run_ngram_baseline(train_fpath, test_fpath)
    ngram_baseline_fpath = join(ROOT_DIR, 'baselines/data/task1_ngram_baseline_%s'%(os.path.basename(test_fpath)))
    if check_format(ngram_baseline_fpath):
        thresholds, precisions, avg_precision, reciprocal_rank, num_relevant = evaluate(test_fpath, ngram_baseline_fpath)
    print("Ngram Baseline AVGP:", avg_precision)


if __name__ == '__main__':
    run_baselines()
