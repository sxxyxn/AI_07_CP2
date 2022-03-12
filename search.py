# -*- coding: utf-8 -*-

import string
from collections import defaultdict
import random

f = open("__data__.txt", 'r', encoding='UTF8')
lines = f.readlines()

match_key = "1\t"
match_key2 = "2\t"
setences = defaultdict(list)

for i in range(len(lines)):
  if lines[i].startswith(match_key):
    line1 = lines[i].replace('1\t','')
    line1 = line1.replace("\n", "")
    line1 = line1.replace('컴패니언','보이스 봇')
    line1 = line1.translate(str.maketrans('', '', string.punctuation))
  else:
    line2 = lines[i].replace('2\t','')
    line2 = line2.replace("\n", "")
    line2 = line2.replace('컴패니언', '보이스 봇')
    setences[line1].append(line2)

f.close()

def search_engine(title):
  if title in setences:
    return random.choice(setences[title])
  else:
    return "잘 못알아 들었어요."


# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np

# stop_words = " "
# tfidf = TfidfVectorizer(stop_words=stop_words.split(' '))

# matrix = tfidf.fit_transform(setences)


# def search_engine(title):
#     setences.append(title)
#     matrix = tfidf.fit_transform(setences)

#     from sklearn.metrics.pairwise import linear_kernel
#     cosine_sim = linear_kernel(matrix, matrix)

#     indices = {v: k for k, v in enumerate(setences)}

#     idx = indices[title]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:6]

#     sentence_indices = [i[0] for i in sim_scores]
#     setences.remove(title)
#     return [setences[sentence_indices[1]],setences[sentence_indices[2]]]