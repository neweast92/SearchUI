import numpy
from numpy import mean
from numpy import std
from numpy import dstack
from pandas import read_csv
from konlpy.tag import Okt
# from matplotlib import pyplot
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import Flatten
# from keras.layers import Dropout
# from keras.layers.convolutional import Conv1D
# from keras.layers.convolutional import MaxPooling1D
# from keras.layers.convolutional import AveragePooling1D
# from keras.utils import to_categorical
# import datetime as dt
# from sklearn.preprocessing import MinMaxScaler
import csv
import os
import gensim
from gensim.models import Word2Vec
import sys

class WordSearch:
    def __init__(self):
        # model 로드
        model = gensim.models.Word2Vec.load("category_model.model")

    def search_category(self, word):
        try:
            return model.wv.most_similar(word)
        except:
            return ''


# run the search
if __name__ == "__main__":
    cls = WordSearch()
    # cls.search_category(sys.argv)
    typed_str = ''
    while True:
        typed_str = input("Category : ")
        if typed_str == 'exit':
            False
        elif typed_str == '':
            continue
        cls.search_category(typed_str)
