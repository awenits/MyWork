from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # splitting the strings into unique lines
    lines_a = set(a.split("\n"))
    lines_b = set(b.split("\n"))
    # list of common lines in both a & b
    similarLines = []
    # appending the common lines in similarLines
    for line in lines_a:
        if line in lines_b:
            similarLines.append(line)
    # returning list of similar Lines
    return similarLines


def sentences(a, b):
    """Return sentences in both a and b"""
    # splitting the strings into unique sentences
    sentences_a = set(sent_tokenize(a))
    sentences_b = set(sent_tokenize(b))
    # for storing common sentences in both a & b
    similarSentences = []
    # appending the common sentences in similarLines
    for sentence in sentences_a:
        if sentence in sentences_b:
            similarSentences.append(sentence)
    # returning list of similar Sentences
    return similarSentences


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    # unique substrings of length n
    substrings_a = helper(a, n)
    substrings_b = helper(b, n)
    # for storing common substrings in both a and b
    similarSubstrings = []
    # appending the common sentences in similarLines
    for substring in substrings_a:
        if substring in substrings_b:
            similarSubstrings.append(substring)
    # returning similarSubstrings
    return similarSubstrings


def helper(stri, n):
    """Return unique substrings of length n in stri"""
    substri_n = []
    los = int(len(stri))
    for i in range(los):
        if i <= los - n:
            substri_n.append(stri[i: i + n])
    return set(substri_n)