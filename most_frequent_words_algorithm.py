#most frequent words algorithm
import sys

#count occurence of specific pattern and return number of occurences
def PatternCount(txt, pattern):
    count = 0

    for i in range(0,len(txt)- len(pattern)):
        if txt[i:i + len(pattern)] == pattern:
            count += 1

    return count

#find the most frequent k-mere in a given string
def MostFrequentWords(txt, k):
    frequentPatterns = []
    count = []

    for i in range(0,len(txt) - k):
        pattern = txt[i:i+k]
        count.append(PatternCount(txt, pattern))
    
    for i in range(0,len(count)):
        if count[i] == max(count):
            frequentPatterns.append(txt[i:i + k])
    
    frequentPatternsSet = list(set(frequentPatterns))
    print(frequentPatternsSet)


if __name__ == '__main__':
    k = int(sys.argv[1])
    txt = str(sys.argv[2])

    MostFrequentWords(txt, k)