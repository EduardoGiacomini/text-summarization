import re
import nltk
import string
import heapq
from text_summarizer import TextSummarizerContract
from utils import ListUtils


class LuhnExtractiveTextSummarizer(TextSummarizerContract):
  def __init__(self) -> None:
    self.stopwords = nltk.corpus.stopwords.words('portuguese')
    self.top_n_words = 5
    self.distance = 2
    self.number_of_sentences = 3

  def summarize(self, text: str) -> str:
    sentences = self.__split_sentences(text)
    preprocessed_sentences = self.__preprocess_sentences(sentences)
    top_words = self.__get_top_words(preprocessed_sentences)
    sentences_score = self.__calculate_sentences_score(preprocessed_sentences, top_words)
    best_sentences = self.__get_best_sentences(sentences, sentences_score)
    summary = ' '.join(best_sentences)
    return summary
  
  def __split_sentences(self, text: str) -> list[str]:
    sentences = nltk.sent_tokenize(text)
    return sentences
  
  def __preprocess_sentences(self, sentences: [str]) -> list[str]:
    preprocessed_sentences = [self.__preprocess_text(sentence) for sentence in sentences]
    return preprocessed_sentences

  def __preprocess_text(self, text: str) -> str:
    text = text.lower()

    all_tokens = nltk.word_tokenize(text)
    tokens = list(filter(lambda token: (token not in self.stopwords and token not in string.punctuation), all_tokens))

    text = ' '.join(tokens)
    return text

  def __get_top_words(self, preprocessed_sentences: list[str]) -> list[str]:
    words = [word for sentence in preprocessed_sentences for word in nltk.word_tokenize(sentence)]
    words_frequency = nltk.FreqDist(words)
    top_words = [word[0] for word in words_frequency.most_common(self.top_n_words)]
    return top_words

  def __calculate_sentences_score(self, preprocessed_sentences: list[str], top_words: list[str]) -> list[dict[float, int]]:
    scores = []
    sentence_index = 0
    for preprocessed_sentence in preprocessed_sentences:
      word_indexes = self.__get_top_word_indexes_in_sentence(preprocessed_sentence, top_words)

      if ListUtils.is_empty(word_indexes):
        continue

      groups = self.__separate_sentence_top_word_indexes_in_groups(word_indexes)
      max_group_score = self.__calculate_sentence_group_score(groups)
      scores.append((max_group_score, sentence_index))
      sentence_index += 1
    return scores

  def __get_top_word_indexes_in_sentence(self, preprocessed_sentence: str, top_words: list[str]) -> list[int]:
    word_indexes = []
    sentence_words = nltk.word_tokenize(preprocessed_sentence)

    for top_word in top_words:
      index = ListUtils.index_of_or_none(sentence_words, top_word)
      if index != None:
        word_indexes.append(index)
    
    word_indexes.sort()
    return word_indexes
  
  def __separate_sentence_top_word_indexes_in_groups(self, word_indexes: list[int]) -> list[list[int]]:
    groups = []
    current_group = [word_indexes[0]]
    i = 1
    while i < len(word_indexes):
      left = word_indexes[i - 1]
      right = word_indexes[i]

      if right - left < self.distance:
        current_group.append(right)
      else:
        groups.append(current_group[:])
        current_group = [right]
      
      i += 1

    groups.append(current_group)
    return groups
  
  def __calculate_sentence_group_score(self, groups: list[list[int]]) -> float:
    max_group_score = 0
    for group in groups:
      important_words_in_group = len(group)

      last_group_index = group[-1]
      first_group_index = group[0]
      total_words_in_group = last_group_index + (first_group_index + 1)

      score = (1.0 * important_words_in_group ** 2) / total_words_in_group
      if score > max_group_score:
        max_group_score = score

    return max_group_score

  def __get_best_sentences(self, sentences: list[str], sentences_score: list[dict[float, int]]) -> list[str]:
    best_sentences = heapq.nlargest(self.number_of_sentences, sentences_score)
    best_sentences = [sentences[i] for (_score, i) in best_sentences]
    return best_sentences