word = "washington"

freq = {}
for ch in word:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print(freq)

word2 = "committee"
freq2 = {}
for ch in word2:
    freq2[ch] = freq2.get(ch, 0) + 1
print(freq2)