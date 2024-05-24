# -------------------------------------IMPORT------------------------------------- #
import random
from random import randint
import os

# -------------------------------------UTILIDADES------------------------------------- #
# Display do menu
def menu():
    Menu = input('[P]Perfil - [E]Monstro Atual - [B]Batalhar - [M]Todos os Monstros - [C]Cemitério - [S]Sair do game: ')
    return Menu.lower()

# Borda para cabeçalho
def borda(frase):
    tamanho = len(frase)
    if tamanho:
        print('+', '-'*tamanho,'+')
        print('|', frase,'|')
        print('+', '-'*tamanho,'+')

# Pedra - papel - tesoura - para a batalha
def pedra_papel_tesoura():
    escolhas = ['pedra', 'papel', 'tesoura']
    return random.choice(escolhas)

# Determina quem vence cada rounde de batalha
def determinar_vencedor(escolha_Player, escolha_monstro):
    if escolha_Player == escolha_monstro:
        return 'empate'
    elif (escolha_Player == 'pedra' and escolha_monstro == 'tesoura') or \
         (escolha_Player == 'papel' and escolha_monstro == 'pedra') or \
         (escolha_Player == 'tesoura' and escolha_monstro == 'papel'):
        return 'player'
    else:
        return 'monstro'

# -------------------------------------Player------------------------------------- #
# Status do Player
def dano_player():
    numero_sorteado = randint(25, 150)
    return numero_sorteado

# Player
Pontos_Player = 20
Player = {
        'Nome': 'Nome_Player',
        'Level': 1,
        'Dano': dano_player(),
        'Hp': 350,
        'Hp_Max': 350,
        'Exp': 0,
        'Exp_Max': 20,
        'Pontos': Pontos_Player,
        'Loot': 0,
    }

# Perfil
def perfil():
    borda('PERFIL')
    info_player()
    print()

# Informaçao do Player
def info_player():
    print(f'🦸 Nome: {Player['Nome']}\n🔷 Level: {Player['Level']}\n❤️  Hp: {Player['Hp']}/{Player['Hp_Max']}\n🗡️  Dano: {Player['Dano']}\n💠 Exp: {Player['Exp']}/{Player['Exp_Max']}\n🔶 Pontos: {Player['Pontos']}\n💰 Dinheiro: {Player["Loot"]}')
    return info_player

# Ataque do player
def ataque_player(player,m):
    print(f"{Player['Nome']} esta atacando {m['Nome']}!")
    m['Hp'] -= Player['Dano']  # Reduzir a saúde do mob em 10
    if m['Hp'] <= 0:
        m['Hp'] = 0
        print(f"{m['Nome']} morreu!".upper())
        return True
    return False

# Adiciona dano
def adicionar_dano(n):
    if n >= 0:
        Player['Dano'] += n * 2
        Player['Pontos'] -= n
    if Player['Pontos'] < 0:
        Player['Pontos'] = 0
    return n

# Adiciona Hp
def adicionar_hp(n):
    if n >= 0:
        Player['Hp_Max'] += n * 5
        Player['Pontos'] -= n
    if Player['Pontos'] < 0:
        Player['Pontos'] = 0
    return n

# Upa o lvl do player
def lvl_up():
    if Player['Exp'] >= Player['Exp_Max']:
        Player['Level'] += 1
        Player['Exp'] = 0
        Player['Pontos'] += 20
        Player['Exp_Max'] = Player['Exp_Max'] * 2

# Menu do perfil do player
def menu_perfil(n):
    if n == 'p':
        if Player['Pontos'] >= 0:
            os.system('cls')
            Menu_pontos = input(f'Qual status você quer adicionar pontos?\n[1]🗡️  Dano: {Player["Dano"]}\n[2]❤️  Hp: {Player["Hp"]}: ')
            if Menu_pontos == '1': 
                os.system('cls')
                print(f'Você tem 🔶 Pontos: {Player['Pontos']}')       
                add_dano = int(input('Digite quantos pontos você quer adicionar em 🗡️  Dano?\n: '))
                if add_dano <= Player['Pontos']:
                    adicionar_dano(add_dano)
                    os.system('cls')
                    print(f'Você adicionou {add_dano} de dano.')
                    info_player()
                else:
                    print(f'Voce não tem {add_dano} de pontos.')
            elif Menu_pontos == '2':        
                os.system('cls')
                print(f'Você tem 🔶 Pontos: {Player['Pontos']}')       
                add_hp = int(input('Digite quantos pontos você quer adicionar em ❤️  Hp? (Cada ponto adiciona 5 de Hp.)\n: '))
                if add_hp <= Player['Pontos']:
                    adicionar_hp(add_hp)
                    os.system('cls')
                    print(f'Você adicionou {add_hp} de Hp.')
                    info_player()
                else:
                    print(f'Voce não tem {add_hp} de pontos.')
    elif Menu_perfil == 'c' or Menu_perfil == 'C':
        os.system('cls')
        if Player['Hp'] < Player['Hp_Max']:
            Player['Hp'] = Player['Hp_Max']
        else:
                print('Seu Hp já esta cheio.')  
        if Player['Loot'] >= 150:
            print('Você comprou uma cura! 🩹')
            Player['Loot'] -= 150
            info_player()
        else:
            print()
            print('Você não tem dinheiro suficiente.')
            print()
            
        if Player['Nome'] == 'Player Morto! ☠️':
            Player['Nome'] = 'Nome_player'
    return menu_perfil



# -------------------------------------MONSTRO------------------------------------- #
# Status do monstro
def dano_mob():
    numero_sorteado = randint(25,100)
    return numero_sorteado

def hp_mob():
    numero_sorteado = randint(140, 300)
    return numero_sorteado

def loot():
    numero_sorteado = randint(1, 300)
    return numero_sorteado

# Escolhe um nome para o monstro
def escolhe_nome_mob():
    nomes = ["Goblin", "Troll", "Orc", "Dragão", "Esqueleto"]
    return random.choice(nomes)

# Gera (n) monstros
def gerador_de_monstros(n):
    for x in range(n):
        novo_monstro = cria_monstro(x + 1)
        Monstros.append(novo_monstro)
        
# Escolhe aleatoriamente entre 1 - 10 monstros para criar
def escolhe_qtd_monstros():
    numero_sorteado = randint(2, 10)
    return numero_sorteado

# Escolhe aleatoriamente entre 1 - 10 monstros para criar

def exp_monstro():
    cap_max_exp = Player['Exp_Max']
    numero_sorteado = randint(20, cap_max_exp)
    return numero_sorteado

# Informaçoes do monstro
def info_monstro(Monstro):
    print(f'🧌  Nome: {Monstro['Nome']}\n❤️  Hp: {Monstro['Hp']}/{Monstro['Hp_max']} \n🗡️  Dano: {Monstro['Dano']}')
    print()
    return info_monstro


Monstros = []
Cemiterio = []
def cria_monstro(n):
    Hp = hp_mob()
    exp = exp_monstro()
    Monstro = {
        'Nome': escolhe_nome_mob(),
        'Dano': dano_mob(),
        'Hp': Hp,
        'Hp_max': Hp,
        'Exp': exp,
        'Loot': loot(),
    }
    return Monstro

# Ataque do monstro
def ataque_monstro(m):
    print(f"{m['Nome']} esta atacando {Player['Nome']}!")
    Player['Hp'] -= m['Dano']  # Reduzir a saúde do mob em 10
    if Player['Hp'] <= 0:
        Player['Hp'] = 0
        print(f"{Player['Nome']} morreu!".upper())
        return True
    return False

# Cria e seleciona o proximo monstro
def proximo_mob():
    if Monstros == []:
        gerador_de_monstros(1)
    else:
        Monstros[0]
        return gerador_de_monstros
# -------------------------------------BATALHA------------------------------------- #
# Informaçao da batalha
def info_batalha(m):
    info_player()
    print('.:VS:.')
    info_monstro(m)
    
# Inicia a batalha
def batalha(m):
    while Player['Hp'] > 0 and m['Hp'] > 0:
        info_batalha(m)
        escolha_player = input("Escolha 🪨  pedra, 📄 papel ou ✂️  tesoura: ").strip().lower()
        if escolha_player not in ['pedra', 'papel', 'tesoura']:
            print('Escolha invalida.')
            continue
        os.system('cls')
        escolha_monstro = pedra_papel_tesoura()
        print(f'O {Player["Nome"]} escolheu: {escolha_player}\nO {m['Nome']} escolheu: {escolha_monstro}')
        print()
        
        resultado = determinar_vencedor(escolha_player, escolha_monstro)
        
        if resultado == 'player':
            ataque_player(Player, m)
            print(f"Você acertou {Player['Dano']} de dano no {m['Nome']}".upper())
            print()
        elif resultado == 'monstro':
            ataque_monstro(m)
            print(f"{m['Nome']} acertou {m['Dano']} no {Player['Nome']}".upper())
            print()
        else:
            print("Empate, ninguém perdeu vida.".upper())
            print()
        
        if m['Hp'] <= 0 or Player['Hp'] <= 0:
            if m['Hp'] <= 0:
                Player['Loot'] += Monstros[0]['Loot']
                Player['Exp'] += Monstros[0]['Exp']
                print(f'{Player['Nome']} ganhou {Monstros[0]['Exp']} de experiencia e {Monstros[0]['Loot']} de dinheiro.')
                monstro_morto = Monstros.pop(0)
                Cemiterio.append(monstro_morto)
                novo_nome = {'Nome': 'Monstro Morto! ☠️'}
                m.update(novo_nome)

            if Player['Hp'] <= 0:
                novo_nome = {'Nome': 'Player Morto! ☠️'}
                Player.update(novo_nome)
                os.system('cls')
                print('Game Over 😭')
                break
        lvl_up()                       






# -------------------------------------RODAR O JOGO------------------------------------- #
gerador_de_monstros(1)
# gerador_de_monstros(escolhe_qtd_monstros())
Monstros[0]
while True:
    Menu = menu()
    os.system('cls')
    if Menu == 'p':
        perfil()
        Menu_perfil = input(f'[P]Pontos: {Player["Pontos"]} [C]Curar (💰 150): ')
        menu_perfil(Menu_perfil.lower())
        # os.system('cls')
    elif Menu == 'e':
        borda('MONSTRO ATUAL')
        info_monstro(Monstros[0])
        
    elif Menu == 'b':
        borda('BATALHAR')
        info_batalha(Monstros[0])
        Menu_batalha = input('[B]Batalhar: ')
        if Menu_batalha == 'b':
            os.system('cls')
            batalha(Monstros[0])
            borda('PROXIMA BATALHA')
            proximo_mob()
            info_batalha(Monstros[0])
        else:
            os.system('cls')
        
    elif Menu == 'm':
        borda('TODOS OS MONSTROS')
        for m in Monstros:
            info_monstro(m)
        
    elif Menu == 'c':
        borda('CEMITÉRIO')
        for m in Cemiterio:
            info_monstro(m)
        if Cemiterio == []:
            print('Não há monstros mortos.')
        
    elif Menu == 's':
        print('Você saiu do game!')
        break
    else:
        print('Escolha invalida.')
