import json
from random import choice

with open("citacoes.json", "r", encoding="utf-8") as ficheiro:
    citacoes = json.load(ficheiro)

def mostrar_menu():    
    print("=" * 35)
    print(" Biblioteca Fernando Pessoa")
    print("=" * 35)
    print()
    print("1 - Nova citação")
    print("2 - Ver Favoritos")
    print("3 - Sair")
    print()

    escolha = input("Escolha: ")
    return escolha

def obter_citacao_aleatoria(citacoes):

    citacao = choice(citacoes)
    return citacao

def mostrar_citacao(citacao):
    print()
    print("-" * 50)
    print()

    print(citacao["texto"])
    print()
    print(f"— {citacao['heteronimo']}")
    print(f"«{citacao['obra']}»")

    print()
    print("-" * 50)
    print()

def carregar_favoritos():
    with open("favoritos.json", "r", encoding="utf-8") as ficheiro:
        favoritos = json.load(ficheiro)
    return favoritos


def adicionar_favorito(citacao):
    favoritos = carregar_favoritos()

    favoritos.append(citacao)

    with open("favoritos.json", "w", encoding="utf-8") as ficheiro:
        json.dump(favoritos, ficheiro, ensure_ascii=False, indent=4)

def mostrar_favoritos(favoritos):
    for favorito in favoritos:
        print(favorito["texto"])
        print()
        print(favorito["obra"])
        print(favorito["heteronimo"])

def navegar_favoritos(favoritos):
    indice = 0

    while True:
        mostrar_citacao(favoritos[indice])
        print("1 - Citação anterior")
        print("2 - Próxima citação")
        print("3 - Voltar ao menu")
        escolha = input("Escolha: ")
        if escolha == "1":
            if indice > 0:
                indice -= 1
        elif escolha == "2":
            if indice < len(favoritos) - 1:
                indice += 1
        elif escolha == "3":
            break
        else:
            print("Escolha inválida")

while True:

    # Mostrar o menu e guardar a opção escolhida
    escolha = mostrar_menu()
    if escolha == "1":
        citacao = obter_citacao_aleatoria(citacoes)
        mostrar_citacao(citacao)
        print("1 - Adicionar aos favoritos")
        print()
        print("2 - Voltar ao menu")
        escolha_favorito = input("Escolha: ")
        if escolha_favorito == "1":
            adicionar_favorito(citacao)
            print("Citação adicionada aos favoritos")
        elif escolha_favorito == "2":
            continue
        else:
            print("Opção inválida")
    elif escolha == "2":
        favoritos = carregar_favoritos()
        mostrar_favoritos(favoritos)
    elif escolha == "3":
        print("\nAté breve!\n")
        break
    else:
        print("\nOpção inválida.\n")
