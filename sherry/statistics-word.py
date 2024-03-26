# 统计文本中单词出现顺序

text = "This is a sample text for word frequency analysis."
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)