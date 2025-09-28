# 🎮 Sorteador de Jogos GBA

O **Sorteador de Jogos GBA** é um programa em Python que gera combinações aleatórias de códigos de jogos de **Game Boy Advance (GBA)** e retorna o nome do jogo correspondente. Cada combinação é única, evitando repetições e garantindo sorteios válidos.

---

## ✨ Funcionalidades

- Geração de combinações aleatórias no formato: **uma letra maiúscula + três números** (ex.: `A001`, `X006`).  
- Consulta do nome do jogo baseado na combinação sorteada.  
- Evita duplicação de combinações já sorteadas.  
- Armazena todas as combinações geradas em um arquivo JSON (`generated_combinations.json`).  
- Possibilidade de listar todas as combinações já sorteadas.

---

## 🗂 Estrutura do Projeto

Sorteador-Jogos-GBA/
│
├─ Sorteador jogos GBA.py # Script principal
├─ biblioteca.py # Dicionário com códigos e nomes dos jogos
├─ generated_combinations.json # Histórico das combinações já sorteadas

---

## ⚡ Como usar

1. Certifique-se de ter **Python 3** instalado.  
2. Clone ou baixe o repositório.  
3. Execute o script principal:

```bash
python "Sorteador jogos GBA.py"

Combinação: X006
Jogo sorteado: xXx (USA, Europe)
Lista de todas as combinações sorteadas: ['D042', 'X006', 'E001', 'W007']

Cada execução gera uma nova combinação única.

🛠 Tecnologias utilizadas

Python 3
JSON (para salvar o histórico de combinações)

⚠️ Observações

O arquivo generated_combinations.json é atualizado automaticamente a cada sorteio.

Novos códigos e jogos podem ser adicionados ao dicionário biblioteca_gba dentro do arquivo biblioteca.py.

Garante que nenhuma combinação seja repetida durante o sorteio.
