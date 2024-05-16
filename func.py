from data import *


#инфо игрока
def info_player():
    print(f'Игрок - {player["name"]}')
    print(f'Здоровье - {player["HP"]}')
    print(f'Сила - {player["strong"]}')
    print(f'Броня - {player["defense"]}')
    print(f'Деньги - {player["money"]}')

#тренировка
def training(training_type):
    pass

def fight(cm):
    enemy = enimies[cm]
    while player["HP"]>0 and enemy["HP"]>0:
        player["HP"] -= enemy['attack']
        enemy['HP'] -= player['attack']
        
        print(f'здоровье игрока ={player["HP"]}, Враг нвнёс: {enemy["attack"]} урона')
        print(f'Здоровье врага = {enemy["HP"]}')

        print()
        sleep(1.5)




