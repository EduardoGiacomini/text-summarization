import re
import nltk
import string
import heapq
from text_summarizer import TextSummarizerContract


class LuhnExtractiveTextSummarizer(TextSummarizerContract):
  def __init__(self) -> None:
    self.stopwords = nltk.corpus.stopwords.words('portuguese')
    self.top_n_words = 5

  def summarize(self, text: str) -> str:
    self.__summarize(text)
    return text

  def __preprocess_text(self, text: str) -> str:
    text = text.lower()

    all_tokens = nltk.word_tokenize(text)
    tokens = list(filter(lambda token: (token not in self.stopwords and token not in string.punctuation), all_tokens))

    text = ' '.join(tokens)
    return text

  def __summarize(self, text: str) -> str:
    sentences = nltk.sent_tokenize(text)
    preprocessed_sentences = [self.__preprocess_text(sentence) for sentence in sentences]
    words = [word for sentence in preprocessed_sentences for word in nltk.word_tokenize(sentence)]
    words_frequency = nltk.FreqDist(words)
    top_words = [word[0] for word in words_frequency.most_common(self.top_n_words)]

    print(top_words)
