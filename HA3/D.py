import sys

words = sys.stdin.read().rsplit()
my_set = set()

for i in range(len(words)):
    if not(words[i] in my_set):
        my_set.add(words[i])

print(len(my_set))