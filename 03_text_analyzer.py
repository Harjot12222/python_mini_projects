para = input("Please enter the paragraph to analyze: ")

# Split into words and sentences
words = para.split()
sentences = [s for s in para.split('.') if s.strip()]  # filter out empty strings

# Count characters (excluding spaces)
characters = len(para.replace(" ", ""))

print("Characters (no spaces):", characters)
print("Words:", len(words))
print("Sentences:", len(sentences))

# Word frequency
freq = {}
for word in words:
    word = word.lower().strip(",.!?")  # normalize words
    freq[word] = freq.get(word, 0) + 1

print("Word frequencies:", freq)

# Most common word
if freq:
    most_common = max(freq, key=freq.get)
    print("Most common word:", most_common)

# Average word length
if words:
    avg = sum(len(word) for word in words) / len(words)
    print("Average word length:", avg)
