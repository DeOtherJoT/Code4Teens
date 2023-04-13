word1 = 'car '
word2 = 'exceeded '
text1 = 'speed limit'
word3 = 'the'

print("{}{}{} {}".format(word1, word2, word3, text1))

print("%s%s%s %s" % (word1, word2, word3, text1))

print(f"{word1}{word2}{word3} {text1}")

print(" ".join([word1.strip(), word2.strip(), word3.strip(), text1]))

print(word1 + word2 + word3, text1)