#!/bin/bash -tt
import urllib2
from collections import Counter
c = Counter()
content = urllib2.urlopen("target-website").read()
c.update(content.split())
c.most_common(50)

for k in c.keys():
    if "<" in k: del c[k]; continue
    if ">" in k: del c[k]; continue
    if "=" in k: del c[k]; continue
    
c.most_common(50)
