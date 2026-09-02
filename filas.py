# O que é uma QUEUE?
# Uma QUEUE (fila) é uma estrutura de dados que segue o princípio FIFO (First In, First Out)
# Isso significa que o primeiro elemento a ser adicionado à fila será o primeiro a ser removido. As filas são usadas em várias aplicações, como gerenciamento de tarefas, impressão de documentos, e processamento de dados em sistemas operacionais.

# Uma queue se corretamente implementada, ela terá uma referência para o primeiro elemento (head) e para o último elemento (tail) da fila. 
# Por que? pq quando eu quiser adicionar um elemento novo na queue, e ter que percorrer a queue toda e adicionar o novo elemento, eu posso pegar o elemento do tail e adicionar mais um elemento após ele.

# O que é uma Dequeue?
# Uma Dequeue (Double-Ended Queue) é uma estrutura de dados que permite a inserir e remover elementos tanto do início quanto do final da fila. 
# Isso significa que você pode adicionar ou remover elementos de ambos os lados da fila, tornando-a mais flexível do que uma fila tradicional.

from collections import deque

def docs_printer(doc1, doc2, doc3):
    # Usando deque da biblioteca padrão (collections)
    q = deque()
    
    print("Adicionando documentos à fila de impressão...")
    q.append(doc1)      # Equivale ao enqueue
    q.append(doc2)
    q.append(doc3)
    
    print("Imprimindo documentos...")
    # Em Python, uma coleção vazia avalia para False
    while q:
        print(f"Imprimindo: {q.popleft()}")  # Equivale ao dequeue
        
    if not q:
        print("Todos os documentos foram impressos.")

docs_printer("Documento 1", "Documento 2", "Documento 3")


