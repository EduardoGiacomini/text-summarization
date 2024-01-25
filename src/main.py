from text_summarizer import TextSummarizer, LuhnExtractiveTextSummarizer, NltkExtractiveTextSummarizer, SpacyExtractiveTextSummarizer


def main():
  text = """
A progressão de carga é uma estratégia comum em periodizações de treinamento de força que visa aumentar gradativamente a intensidade do treino. A ideia por trás da progressão de carga é que, para continuar estimulando o crescimento muscular e força, é necessário fornecer uma sobrecarga progressiva nos músculos. A sobrecarga progressiva pode ser alcançada aumentando a quantidade de peso levantado, o número de séries e repetições.
Estudos sugerem que a progressão de carga é um fator importante para o desenvolvimento da força e hipertrofia muscular, especialmente para os iniciantes na musculação. Além disso, a progressão de carga é uma estratégia segura e eficaz para prevenir lesões e melhorar a qualidade de vida em idosos (1)(2).
Se você deseja melhorar a força e resistência muscular dos membros inferiores, uma excelente opção de exercício é o agachamento. O agachamento é um exercício composto que trabalha vários grupos musculares dos membros inferiores, incluindo quadríceps, glúteos, isquiotibiais e panturrilhas. Além disso, é um exercício funcional que pode ajudar a melhorar a sua capacidade de fazer movimentos diários com menos dificuldade, como subir escadas ou carregar as compras, o filho e até mesmo arrumar a casa arrastando os objetos pesados.
É importante enfatizar que a progressão de carga deve ser gradual para ser segura. Se você aumentar a carga rápido demais, corre o risco de lesões, pois os tendões têm um tempo diferente dos músculos para se adaptar ao treino e o aumento de carga. É por isso que é importante trabalhar com um treinador ou personal trainer para prescrever ou planejar um programa de treinamento adequado.
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
