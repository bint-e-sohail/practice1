sentence = "the cat and the hat and the bat"

# Split into list
words = sentence.split()

# 2. Count= make dict to count 
counts = {}
#if word's new,start at 1 .if exist add 1 and save new cout in dict
for word in words:
    counts[word] = counts.get(word, 0) + 1

# 3. Print the dict
print(counts)
#find keys vaule and compare
most_common = max(counts, key=counts.get)

# 4. Print most common word and its count
print(most_common, counts[most_common])