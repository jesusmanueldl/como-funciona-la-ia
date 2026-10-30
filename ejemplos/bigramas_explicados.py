"""Modelo estadístico de bigramas de caracteres con suavizado sencillo."""
from collections import Counter,defaultdict
import random

CORPUS = ['casa','cama','casa','capa']
counts=defaultdict(Counter)
for word in CORPUS:
    text='^'+word+'$'
    for a,b in zip(text,text[1:]):
        counts[a][b]+=1

def probabilities(previous):
    row=counts[previous]
    alphabet=sorted({c for line in CORPUS for c in line} | {'$'})
    k=len(alphabet)
    total=sum(row.values()) + k
    return {c:(row[c]+1)/total for c in alphabet}

if __name__=='__main__':
    for symbol in ['^','c','a']:
        print('contexto',symbol,'conteos',dict(counts[symbol]),'probabilidades',probabilities(symbol))
    rng=random.Random(42)
    text=''
    previous='^'
    for _ in range(25):
        ps=probabilities(previous)
        nxt=rng.choices(list(ps),weights=list(ps.values()),k=1)[0]
        if nxt=='$': break
        text+=nxt
        previous=nxt
    print('generado:',text)
