from wordcount import load_word_counts
import sys


def top_n_words(counts, number_of_top_words=10):
    """
    Given a list of (word, count, percentage) tuples,
    return the top two word counts.
    """
    limited_counts = counts[0:number_of_top_words]
    count_data = [count for (_, count, _) in limited_counts]
    return count_data


if __name__ == '__main__':
    number_of_top_words = sys.argv[1]
    input_files = sys.argv[2:]
    header = "Book"
    for i in range(int(number_of_top_words)):
         header += ",word"+str(i+1)
    print(header)
    for input_file in input_files:
        counts = load_word_counts(input_file)
        top_words = top_n_words(counts, int(number_of_top_words))
        bookname = input_file[:-4].split("/")[-1]
        line = bookname
        for i in top_words:
            line += ","+str(i)
        print(line)
