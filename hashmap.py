#HashMap - Augusto galego
# Um hashmap é uma estrutura de dados que armazena pares de chave-valor, permitindo acesso rápido aos valores com base em suas chaves. Abaixo está uma implementação simples de um HashMap em Python.

idades = {} #hashmap em python são representados por dicts

idades["João"] = 25
idades["Maria"] = 30
print(idades) # {'João': 25, 'Maria': 30} Saída, porque? por que instanciamos idades como um dicionario vazion, depois adicionamos valores usando chave: valor, como na linha 6 (joão:25)


class MeuHashMap:
    def __init__(self, capacidade=8):
        self.buckets = [[] for _ in range(capacidade)]
        self.quantidade = 0

    def put(self, chave, valor):
        indice = hash(chave) % len(self.buckets)
        bucket = self.buckets[indice]

        # TODO: se a chave já está no bucket, atualize seu valor.
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)
                return
        bucket.append((chave, valor))
        self.quantidade += 1
        # TODO: caso contrário, adicione o par e aumente quantidade.

    def get(self, chave):
        indice = hash(chave) % len(self.buckets)
        bucket = self.buckets[indice]

        # TODO: procure a chave no bucket e devolva seu valor.
        for k, v in bucket:
            if k == chave:
                return v # retorna o valor baseado na key
        # TODO: se não existir, lance KeyError(chave).
        raise KeyError(chave)

    def load_factor(self):
        # TODO: devolva quantidade / capacidade.
        lf = self.quantidade / len(self.buckets)
        if lf:
            return lf
        raise NotImplementedError


meu_hashmap = MeuHashMap()
meu_hashmap.put("João", 25)
print(meu_hashmap.buckets)  # Exibe os buckets do hashmap
meu_hashmap.put("João", 30)
print(meu_hashmap.buckets)  # Exibe os buckets do hashmap após atualizar o valor