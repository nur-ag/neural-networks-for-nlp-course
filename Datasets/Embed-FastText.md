Assuming a FastText installation, using a pretrained model such as `../crawl-300d-2M-subword.bin`,
the process of generating word embeddings for a vocabulary `vocab.txt` with a token per line is
to simply run:

    ```fasttext print-word-vectors ../crawl-300d-2M-subword.bin < vocab.txt```

This is the method used to generate 'FastTextEmbeddings.txt' in the `Embeddings` folder.
