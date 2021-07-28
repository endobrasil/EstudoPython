#conjuntos
conjunto={1,2,3,4,5}
conjunto2={5,6,7,8}
print(type(conjunto))
print(conjunto)
conjunto.add(6)
print(conjunto)

conjunto_uniao=conjunto.union(conjunto2)
conjunto_interseccao=conjunto.intersection(conjunto2)
conjunto_diferenca=conjunto.difference(conjunto2)
conjunto_diferenca2=conjunto2.difference(conjunto)
conjunto_diferenca_simetrica=conjunto.symmetric_difference(conjunto2)
print(conjunto_uniao)
print(conjunto_interseccao)
print(conjunto_diferenca)
print(conjunto_diferenca2)
print(conjunto_diferenca_simetrica)