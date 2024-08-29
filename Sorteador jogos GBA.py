import random
import string
import json
import os
from biblioteca import biblioteca_gba  # Importa biblioteca_gba from biblioteca.py

# Arquivo JSON para armazenar as combinações geradas
state_file = 'generated_combinations.json'

# Carregar combinações previamente geradas no arquivo JSON
if os.path.exists(state_file):
    with open(state_file, 'r') as file:
        state = json.load(file)
    generated_combinations = set(state['generated_combinations'])
    all_generated_combinations = state['all_generated_combinations']
else:
    generated_combinations = set()
    all_generated_combinations = []

# Gera uma combinação aleatória de uma letra maiúscula e três números inteiros
def generate_random_combination():
    letter = random.choice(string.ascii_uppercase)
    numbers = ''.join(random.choices(string.digits, k=3))
    return letter + numbers

# Retorna o nome do jogo baseado na combinação aleatória gerada
def get_game_info(combination):
    return biblioteca_gba.get(combination, None)

# Gera uma combinação única e válida que não foi gerada anteriormente
def generate_unique_valid_combination():
    while True:
        random_combination = generate_random_combination()
        if random_combination not in generated_combinations and get_game_info(random_combination):
            generated_combinations.add(random_combination)
            all_generated_combinations.append(random_combination)
            save_state()  # Save state after generating a new combination
            return random_combination

# Salva o atual estado de combinações geradas no arquivo JSON
def save_state():
    state = {
        'generated_combinations': list(generated_combinations),
        'all_generated_combinations': all_generated_combinations
    }
    with open(state_file, 'w') as file:
        json.dump(state, file)

# Retorna uma lista de todas as combinações geradas
def get_all_generated_combinations():
    return all_generated_combinations

# Gera uma combinação única e válida
unique_combination = generate_unique_valid_combination()
information = get_game_info(unique_combination)

# Mostra a combinação gerada e o jogo correspondente
print(f"Combinação: {unique_combination}")
print(f"Jogo sorteado: {information}")

# Lista todas as combinações geradas
print("Lista de todas as combinações sorteadas:", get_all_generated_combinations())