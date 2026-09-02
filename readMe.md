# Diario de Estudos - Python

Repositorio para registro de topicos estudados, anotacoes teoricas e aprendizados praticos.

---

## Progresso dos Topicos

<!-- 
COMPONENTE: CHECKLIST
- [ ] **[NOME DO TOPICO]** (YYYY-MM-DD) - `caminho/do/script.py`
-->

- [x] **Queues e Deques** (2026-09-01) - `desafio1.py`

---

## Topicos Estudados

### Queues e Deques

#### 1. O que e uma Queue?
Estrutura de dados que segue o principio **FIFO** (First In, First Out). O primeiro elemento a entrar e o primeiro a sair.

**Aplicacoes:**
- Filas de impressao.
- Processamento de tarefas em segundo plano.

**Head e Tail:**
Uma fila eficiente mantem referencias para o inicio (`head`) e o fim (`tail`). Isso permite adicionar novos elementos diretamente apos o `tail` com complexidade $O(1)$, sem precisar percorrer a estrutura toda.

#### 2. O que e uma Deque?
Fila de extremidade dupla (Double-Ended Queue). Permite inserir e remover elementos de ambas as pontas (inicio e fim) com complexidade $O(1)$.

#### 3. Erros Comuns e Boas Praticas
- **Shadowing de modulos:** Nao nomeie o arquivo como `queue.py`, pois isso bloqueia a importacao do modulo padrao do Python (`ImportError: cannot import name 'Queue' from 'queue'`).
- **Uso padrao em Python:** Utilize `from collections import deque`.
- **Metodos do `deque`:** `.append()` para enfileirar e `.popleft()` para desenfileirar.

---

<!-- 
====================================================================
COMPONENTE PARA NOVO TOPICO (Copie e cole abaixo para novos estudos)
====================================================================

### [NOME DO NOVO TOPICO]

#### 1. Conceito Principal
Descricao do conceito...

#### 2. Aplicacoes
- Aplicacao 1
- Aplicacao 2

#### 3. Erros Comuns e Boas Praticas
- Anotacoes importantes...

---
-->
