import re
import csv
from collections import Counter
with open("/Users/macbook/Desktop/klignon.tab","r") as f:
# QUESTION 1  Afiicer la liste des 3 noms de poneys les plus fréquents  
    MELONGE = []
    for t in f:
        t = t.split('\t')[2]
        MELONGE.append(t)
    
print('\n'.join(MELONGE))