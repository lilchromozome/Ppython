# Type your code here. 
text = input()
word1 = input()
word2 = input()
f = open(text)
content = f.readlines()

out = []
for word in content:
    if word >= word1 or word <= word2:
        out.append(word)
print(out)