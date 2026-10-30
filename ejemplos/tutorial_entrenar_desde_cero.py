"""Regresión lineal educativa sin bibliotecas externas: y = 2x + 1."""
import json
from pathlib import Path

TRAIN = [(0., 1.), (1., 3.), (2., 5.), (3., 7.)]
TEST = [(4., 9.), (5., 11.)]
CHECKPOINT = Path(__file__).with_name("checkpoint_tutorial.json")

def loss_and_grad(w, b, data):
    n = len(data)
    errors = [(w*x+b-y, x) for x,y in data]
    loss = sum(error**2 for error,_ in errors)/n
    dw = 2*sum(error*x for error,x in errors)/n
    db = 2*sum(error for error,_ in errors)/n
    return loss,dw,db

def train(steps=5000, lr=0.05):
    w,b=0.0,0.0
    for step in range(steps):
        loss,dw,db=loss_and_grad(w,b,TRAIN)
        w-=lr*dw
        b-=lr*db
        if step in (0,1,2,9,99,steps-1):
            print(f"paso={step+1} pérdida={loss:.6f} w={w:.6f} b={b:.6f}")
    return {'w':w,'b':b}

def predict(model,x):
    return model['w']*x+model['b']

if __name__ == '__main__':
    model=train()
    for x,y in TEST:
        print(f"prueba x={x} esperado={y} predicción={predict(model,x):.6f}")
    CHECKPOINT.write_text(json.dumps(model,indent=2),encoding='utf-8')
    restored=json.loads(CHECKPOINT.read_text(encoding='utf-8'))
    assert all(abs(predict(model,x)-predict(restored,x)) < 1e-12 for x,_ in TEST)
    assert abs(model['w']-2)<1e-3 and abs(model['b']-1)<1e-3
    print('checkpoint restaurado y comprobado:',CHECKPOINT)
