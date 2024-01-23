import re
import nltk
import string
import heapq
from text_summarizer import TextSummarizerContract


class NltkExtractiveTextSummarizer(TextSummarizerContract):
  def __init__(self) -> None:
    self.sentences = 2
    self.stopwords = nltk.corpus.stopwords.words('portuguese')

  def summarize(self, text: str) -> str:
    processed_text = self.__preprocess_text(text)
    word_frequency = self.__calculate_word_frequency(processed_text)
    sentences_score = self.__set_sentence_weights(text, word_frequency)
    best_sentences = self.__get_best_sentences(sentences_score)
    summary = self.__generate_summary(best_sentences)
    return summary
  
  def __preprocess_text(self, text: str) -> str:
    text = text.lower()

    all_tokens = nltk.word_tokenize(text)
    tokens = list(filter(lambda token: (token not in self.stopwords and token not in string.punctuation), all_tokens))

    text = ' '.join(tokens)
    return text
  
  def __calculate_word_frequency(self, text: str) -> dict:
    word_frequency = nltk.FreqDist(nltk.word_tokenize(text))
    highest_frequency = max(word_frequency.values())

    for word in word_frequency.keys():
      word_frequency[word] = word_frequency[word] / highest_frequency

    return word_frequency

  def __set_sentence_weights(self, text: str, word_frequency: dict) -> dict:
    sentences = nltk.sent_tokenize(text)

    sentences_score = dict()
    for sentence in sentences:
      for word in nltk.word_tokenize(sentence.lower()):
        if sentence not in sentences_score.keys():
          sentences_score[sentence] = word_frequency[word]
        else:
          sentences_score[sentence] += word_frequency[word]

    return sentences_score
  
  def __get_best_sentences(self, sentences_score: dict) -> list[str]:
    best_sentences = heapq.nlargest(self.sentences, sentences_score, key=sentences_score.get)
    return best_sentences
  
  def __generate_summary(self, best_sentences: list[str]) -> str:
    summary = ' '.join(best_sentences)
    return summary
