import abc


class TextSummarizerContract:
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def summarize(self, text: str) -> str:
    pass


class TextSummarizer:
  def __init__(self, summarizer_strategy: TextSummarizerContract) -> None:
    self.__strategy= summarizer_strategy

  def summarize(self, text: str) -> str:
    return self.__strategy.summarize(text)
