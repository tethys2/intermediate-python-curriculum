scores = {"Ava" : 95, "Ben" : 88, "Kai": 73}

for name in scores:
    print(name, "scored", scores[name])

print(list(scores.keys()))
print(list(scores.values()))
print(list(scores.items()))

for name, score in scores.items():
    if score < 90 and score >= 85:
        print(name, "got a B")