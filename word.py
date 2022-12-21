n = int(input().strip())
counter = {}
words = []
for i in range(n):
  word = input().strip()
  if word in counter:
    counter[word] += 1
  else:
    counter[word] = 1
    words.append(word)
    
print (len(words))
print (' '.join([str(counter[word]) for word in words]))
