#!/usr/bin/env python
words=['cat','window','supercalifragilisticexpialidocious'];
for w in words:
    print w, len(w);
for w in words[:]:
    if len(w)>6:
        words.insert(1,w);
print words;