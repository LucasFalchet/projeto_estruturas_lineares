# 📚 Estruturas de Dados em Python

Este repositório contém três pequenos projetos desenvolvidos em Python com o objetivo de praticar conceitos fundamentais de estruturas de dados: **lista, pilha e fila**.

---

## 🧠 Problema que os programas resolvem

Os programas simulam situações reais do dia a dia:

* **Desafio 01 – Votação:**
  Permite registrar votos para candidatos e calcular o vencedor de uma eleição simples.

* **Desafio 02 – Editor de Texto (Pilha):**
  Simula um editor de texto onde é possível digitar palavras e desfazer a última ação (como um "Ctrl + Z").

* **Desafio 03 – Fila de Atendimento:**
  Representa o funcionamento de uma fila em uma secretaria acadêmica, onde alunos entram e são atendidos por ordem de chegada.

---

## 🏗️ Estruturas utilizadas

Cada programa utiliza uma estrutura específica:

* **Lista (`list`)**

  * Usada em todos os projetos como base.

* **Pilha (LIFO - Last In, First Out)**

  * Implementada no editor de texto.
  * Métodos usados:

    * `append()` → adiciona elemento
    * `pop()` → remove o último elemento

* **Fila (FIFO - First In, First Out)**

  * Implementada na fila de atendimento.
  * Métodos usados:

    * `append()` → adiciona ao final
    * `pop(0)` → remove o primeiro elemento

---

## ▶️ Como executar o programa

### Pré-requisitos:

* Ter o **Python 3** instalado

### Passos:

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta:

```bash
cd seu-repositorio
```

3. Execute qualquer um dos arquivos:

```bash
python desafio_01_votacao.py
python desafio_02_editor_pilha.py
python desafio_03_fila_atendimento.py
```

---

## 💻 Exemplos de entrada e saída

### 🗳️ Votação

**Entrada:**

```
ana
bruno
ana
fim
```

**Saída:**

```
Resultado da votação:
Ana: 2 votos
Bruno: 1 votos
Carlos: 0 votos

O vencedor é: Ana.
```

---

### 📝 Editor de Texto (Pilha)

**Entrada:**

```
1 → Digitar palavra → "Olá"
1 → Digitar palavra → "mundo"
3 → Mostrar texto
```

**Saída:**

```
Texto atual: Olá mundo
```

---

### 🏫 Fila de Atendimento

**Entrada:**

```
1 → João
1 → Maria
3 → Mostrar fila
2 → Chamar próximo
```

**Saída:**

```
Fila atual:
1° - João
2° - Maria

Chamando aluno: João
```

---

## 📌 Observações

* Os programas utilizam `match-case` (Python 3.10+).
* O comando `cls` é usado para limpar o terminal (funciona no Windows).

---

## 🚀 Objetivo

Este projeto foi desenvolvido com foco educacional para reforçar conceitos de lógica de programação e estruturas de dados na prática.

---
# projeto_estruturas_lineares
