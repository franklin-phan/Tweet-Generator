import sys

def read_file(file_name):
    #Read in file
    with open(file_name, 'r') as f:
        words = f.read().split()

    #Strip words of special characters
    for word in words:
        word = word.strip(".@'/").upper()

    return words

#dictionary
def histogram_dictonary(words):
    histogram = dict()

    #Look up and increment word
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

def unique_words(histogram):
    return len(histogram)

#for word in word
#   


if __name__ == "__main__":
    file_name = ('histo.txt')
    words = read_file(file_name)

    #Histogram using dict
    print(f"Dictionary: {histogram_dictonary(words)}")
    #hello
    