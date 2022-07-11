#!/bin/bash

python -m textblob.download_corpora

python -c "import nltk; nltk.download('stopwords')"