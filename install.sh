#!/bin/bash

# Install all necessary packages
python -m pip install -r requirements.txt

# Uncompress the embedding models that are huge for Github
gunzip -c Embeddings/FastTextEmbeddings.txt.gz > Embeddings/FastTextEmbeddings.txt
cat Embeddings/glove.6B.100d.txt.gz.part-* | gunzip > Embeddings/glove.6B.100d.txt

# Run the notebook with the widgets extension
jupyter notebook
jupyter nbextension enable --py --sys-prefix widgetsnbextension

