# Text summarization

Self study lessons to summarize portuguese texts. The goal is create an algoritmic to summarize
a collection of related pull requests to create an small and clear release changelogs for developers.

## How to run?

Create a virtual python environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements.

```bash
pip3 install -r requirements.txt
```

Install portuguese model for Spacy.

```bash
python3 -m spacy download pt_core_news_sm
```

Run:

```bash
python3 src/main.py
```

## Summarization strategies
