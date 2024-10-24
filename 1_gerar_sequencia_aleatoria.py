import random

def gerar_sequencia_genetica(comprimento):
    bases = ['A', 'T', 'C', 'G']
    #sequencia = ''.join(random.choice(bases) for _ in range(comprimento))
    sequencia = ''
    for _ in range(comprimento):
      sequencia += random.choice(bases)
    return sequencia

# Exemplo de uso
comprimento_desejado = 10000  # Defina o comprimento desejado
sequencia_genetica = gerar_sequencia_genetica(comprimento_desejado)

print(sequencia_genetica)
