labelset = set()
wordset = set()
with open('target.txt', 'r') as target:
    for content in target.readlines():
        for i in content.split(' '):
            i = i.strip()
            if i != '':
                labelset.add(i)
with open('source.txt', 'r') as source:
    for content in source.readlines():
        for i in content.split(' '):
            i = i.strip()
            if i != '':
                wordset.add(i)
with open('target_vocab.txt', 'w') as target_vocab:
    for label in labelset:
        target_vocab.write(label+'\n')
    target_vocab.close()

with open('source_vocab.txt', 'w') as source_vocab:
    for word in wordset:
        source_vocab.write(word+'\n')
    source_vocab.close()
