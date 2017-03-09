def playing(PlayOff, commands):
    import random
    
    random.shuffle(commands)
    rand = commands[:]
    for a in range(0, len(rand)):
        if a%2 == 0:
            game = [random.randint(0,5), random.randint(0,5), rand[a+1]]
            PlayOff[rand[a]].append(game)
            if game[0] > game[1]:
                del (commands[commands.index(rand[a+1])])
            elif game[0] < game[1]:
                del (commands[commands.index(rand[a])])
            else:
                while game[0] == game[1]:
                    game[0] = game[0]+random.randint(0,1)
                    game[1] = game[1]+random.randint(0,1)
                if game[0] > game[1]:
                    del (commands[commands.index(rand[a+1])])
                else:
                    del (commands[commands.index(rand[a])])
            game1 = [game[1], game[0], rand[a]]
            PlayOff[rand[a+1]].append(game1)

def main():

    file = open('commands.txt')
    PlayOff = dict()
    for line in file:
        PlayOff[line[:-1]] = [] #Удаляем символ перехода строки
   # print(PlayOff)
    Current = list(PlayOff.keys()) #Выписываем текущие команды
   # print(Current)
    
    playing(PlayOff, Current)
    playing(PlayOff, Current)
    playing(PlayOff, Current)

    print("-----------------ЧЕМПИОНАТ ПРОВЕДЕН-------------------")
    print("Результаты какой команды вы хотите посмотреть? \nЧтобы выйти, наберите 'end' ...\n")
    command = input()
    while command != "end":
        
        while not PlayOff.get(command):
            print("такой команды нет, введите снова")
            command = input("Результаты какой команды вы хотите посмотреть? ")
        for a in range(0, len(PlayOff[command])):
            if a == 0:
                fin = "четвертьфинал"
            if a == 1:
                fin = "полуфинал"
            if a == 2:
                fin = "финал"
            if PlayOff[command][a][0] > PlayOff[command][a][1]:
                print("{}: {}:{}, победа над командой {}!!! :D ".format(fin,PlayOff[command][a][0], PlayOff[command][a][1], PlayOff[command][a][2]))
            else:
                print("{}: {}:{}, поражение команде {}! ;( ".format(fin,PlayOff[command][a][0], PlayOff[command][a][1], PlayOff[command][a][2]))
        print("\nРезультаты какой команды вы хотите посмотреть? \nЧтобы выйти, наберите 'end' ...\n")
        command = input()
            
main()
