import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
from text_summarizer import TextSummarizerContract


class SpacyExtractiveTextSummarizer(TextSummarizerContract):
  def __init__(self) -> None:
    self.nlp = spacy.load('pt_core_news_sm')
    self.pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    self.stop_words = list(STOP_WORDS)
    self.sentences = 2

  def summarize(self, text: str) -> str:
    doc = self.nlp(text)

    keywords = []
    for token in doc:
      if token.text in self.stop_words or token.text in punctuation:
        continue
      if token.pos_ in self.pos_tag:
        keywords.append(token.text)

    word_frequency = Counter(keywords)

    max_frequency = word_frequency.most_common(1)[0][1]
    for word in word_frequency.keys():
      word_frequency[word] = word_frequency[word] / max_frequency

    sentence_strengths = dict()
    for sentence in doc.sents:
      for word in sentence:
        if word.text in word_frequency.keys():
          if sentence in sentence_strengths.keys():
            sentence_strengths[sentence] += word_frequency[word.text]
          else:
            sentence_strengths[sentence] = word_frequency[word.text]

    summarized_sentences = nlargest(n=self.sentences, iterable=sentence_strengths, key=sentence_strengths.get)
    sentences = [sentence.text for sentence in summarized_sentences]
    summary = " ".join(sentences)

    return summary
