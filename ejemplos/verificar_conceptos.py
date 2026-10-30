"""Comprobaciones matemáticas de la guía."""
from math import exp,sqrt,isclose

def run():
    assert 3*4+4 + 4*2+2 == 26
    w=0
    expected=[.4,.72,.976]
    for target in expected:
        grad=2*(w-2)
        w-=.1*grad
        assert isclose(w,target,abs_tol=1e-12)
    vals=[exp(2),exp(1),exp(0)]
    probs=[v/sum(vals) for v in vals]
    assert isclose(sum(probs),1)
    assert isclose(probs[0],.6652409558,abs_tol=1e-8)
    s=exp(1/sqrt(2))/(exp(1/sqrt(2))+1)
    assert isclose(s,.66976,abs_tol=.001)
    assert isclose(s*10+(1-s)*20,13.3024,abs_tol=.02)
    print('Cálculos principales: correctos')

if __name__ == '__main__': run()
