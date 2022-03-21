[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/enccs/word-count-hpda/HEAD)
# Word count example

These programs will count words in a given text, plot a bar chart of the 10
most common words, and print out the 10 most common words which can be used to test [Zipf's
law](https://en.wikipedia.org/wiki/Zipf%27s_law).

- Inspired by and derived from https://hpc-carpentry.github.io/hpc-python/
  which is distributed under
  [Creative Commons Attribution license (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
- Documentation: https://word-count.readthedocs.io

## Example usage

All data files, 64 public domain books from [Project Gutenberg](https://www.gutenberg.org/)
reside under `data`. To compute the frequency distribution of words for one of the books:

```bash
# count words in two books
python source/wordcount.py data/pg10.txt > processed_data/pg10.dat
python source/wordcount.py data/pg65.txt > processed_data/pg65.dat

# (optionally) create plots
python source/plotcount.py processed_data/pg10.dat results/pg10.png
python source/plotcount.py processed_data/pg65.dat results/pg65.png

# print frequency of 10 most frequent words in both books to file
python source/zipf_test.py 10 pg10.dat pg65.dat > results.txt
```

This workflow is encoded in the `Snakefile` which can be used to run
through all data files in serial or parallel:
```bash
# run workflow 
snakemake -j 1

# clear all output
snakemake -j 1 --delete-all-output

# run in parallel on 4 processes
snakemake -j 4
```

