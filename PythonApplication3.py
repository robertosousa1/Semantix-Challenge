import operator
arquivo = open("edges.dat", "r")
grafo = {}

for linha in arquivo:
    primeiraColuna, segudaColuna = linha.split()
    if primeiraColuna not in grafo:
        grafo[primeiraColuna] = {}
        grafo[primeiraColuna][segudaColuna] = {}
    else:
        grafo[primeiraColuna][segudaColuna] = {}

    if segudaColuna not in grafo:
        grafo[segudaColuna] = {}
        grafo[segudaColuna][primeiraColuna] = {}
    else:
        grafo[segudaColuna][primeiraColuna] = {}

def proximidade(grafo, u=None):
    distanciamento = {}
    vertice = []
    i = 0
    for aux, valor in grafo.items():
        vertice.append(aux)
    
    for n in vertice:
        caminhoCurto = caminhoCurtoCorreto(grafo,n)
        caminhoInteiro = sum(caminhoCurto.values())
        if caminhoInteiro > 0.0 and len(grafo) > 1:
            distanciamento[n] = (len(caminhoCurto)-1.0) / caminhoInteiro
            s = (len(caminhoCurto)-1.0) / ( len(grafo) - 1 )
            distanciamento[n] *= s
        else:
            distanciamento[n] = 0.0
    if u is not None:
        return distanciamento[u]
    else:
        return distanciamento

def caminhoCurtoCorreto(graph,source):
    percorrido={}                  
    ponto=0               
    proximoPonto={source:1}  
    while proximoPonto:
        atualPonto=proximoPonto  
        proximoPonto={}         
        for v in atualPonto:
            if v not in percorrido:
                percorrido[v]=ponto 
                proximoPonto.update(graph[v]) 
        ponto=ponto+1
    return percorrido  

valorFinal = proximidade(grafo)
ordem = sorted(valorFinal.items(),key=operator.itemgetter(-1))
for i in ordem:
    print(i)
exit()