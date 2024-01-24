from text_summarizer import TextSummarizer, LuhnExtractiveTextSummarizer, NltkExtractiveTextSummarizer, SpacyExtractiveTextSummarizer


def main():
  text = """
    O aprendizado de máquina (ML) é o estudo científico de algoritmos e modelos estatísticos que os
    sistemas de computador usam para melhorar progressivamente seu desempenho em uma tarefa
    específica. Algoritmos de aprendizado de máquina constroem um modelo matemático de dados de
    amostra, conhecidos como “dados de treinamento”, para fazer previsões ou decisões sem serem
    explicitamente programados para executar a tarefa. Algoritmos de aprendizado de máquina são
    utilizados nas aplicações de filtragem de e-mail, detecção de intrusos em redes e visão
    computacional, onde é inviável desenvolver um algoritmo de instruções específicas para a
    execução da tarefa. O aprendizado de máquina está intimamente relacionado à estatística
    computacional, que se concentra em fazer previsões usando computadores. O estudo da otimização
    matemática fornece métodos, teoria e domínios de aplicação ao campo do aprendizado de máquina.
    A mineração de dados é um campo de estudo do aprendizado de máquina e se concentra na análise
    exploratória de dados por meio do aprendizado não supervisionado. Na sua aplicação em problemas
    de negócios, o aprendizado de máquina também é conhecido como análise preditiva.
  """

  luhn_extractive_text_summarizer = TextSummarizer(LuhnExtractiveTextSummarizer())
  nltk_extractive_text_summarizer = TextSummarizer(NltkExtractiveTextSummarizer())
  spacy_extractive_text_summarizer = TextSummarizer(SpacyExtractiveTextSummarizer())

  luhn_extractive_summary = luhn_extractive_text_summarizer.summarize(text)
  nltk_extractive_summary = nltk_extractive_text_summarizer.summarize(text)
  spacy_extractive_summary = spacy_extractive_text_summarizer.summarize(text)
  
  print("🤖 Luhn summarized text:\n", luhn_extractive_summary)
  print("🤖 NLTK summarized text:\n", nltk_extractive_summary)
  print("🤖 Spacy summarized text:\n", spacy_extractive_summary)


if __name__ == '__main__':
  main()
