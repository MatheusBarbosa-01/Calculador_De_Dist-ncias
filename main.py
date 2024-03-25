#Trabalho de Algorítimo, tema 08
import os, time, math, msvcrt

def main():
    
    def menu():
        os.system('cls')
        print('''

    ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░  ██████╗░███████╗
    ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
    ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝  ██║░░██║█████╗░░
    ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗  ██║░░██║██╔══╝░░
    ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║  ██████╔╝███████╗
    ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝

    ██████╗░██╗░██████╗████████╗░█████╗░███╗░░██╗░█████╗░██╗░█████╗░░██████╗
    ██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██║██╔══██╗██╔════╝
    ██║░░██║██║╚█████╗░░░░██║░░░███████║██╔██╗██║██║░░╚═╝██║███████║╚█████╗░
    ██║░░██║██║░╚═══██╗░░░██║░░░██╔══██║██║╚████║██║░░██╗██║██╔══██║░╚═══██╗
    ██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░╚███║╚█████╔╝██║██║░░██║██████╔╝
    ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░
    ''')
        print('Bem-vindo!')
        print('\n- Digite 1 para calcular a distância no plano Bidimensional.')
        print('- Digite 2 para calcular a distância no plano Tridimensional.')
        print('- Digite 3 para encerrar o programa.')
        answer = int(input('\nDigite aqui sua decisão: '))
        
        if answer == 1:
            os.system('cls')
            bidimensional()
        elif answer == 2:
            os.system('cls')
            tridimensional()
        elif answer == 3:
            print('Até mais...')
            time.sleep(3)
            os.system('cls')
        else:
            os.system('cls')
            print('Opção inválida! Aguarde para retornar ao menu principal.')
            time.sleep(3)
            menu()

    def distancia_2d(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def distancia_3d(x1, y1, z1, x2, y2, z2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    def read_key():
        return msvcrt.getch()

    def bidimensional():
        print('*******************')
        print('Plano Bidimensional')
        print('*******************\n')
        x1, y1 = map(float, input('Digite as coordenadas do ponto A (x1 , y1) separadamente e sem vírgula: ').split())
        x2, y2 = map(float, input('Digite as coordenadas do ponto B (x2 , y2) separadamente e sem vírgula: ').split())
        distanciaResult = distancia_2d(x1, y1, x2, y2)
        print('\nA distância entre os pontos A e B no plano 2D é:', distanciaResult)
        print('Aperte qualquer tecla para retornar ao menu: ')
        key = read_key()
        os.system('cls')
        print('Retornando...')
        time.sleep(3)
        menu()
        
    def tridimensional():
        print('********************')
        print('Plano Tridimensional')
        print('********************\n')
        x1, y1, z1 = map(float, input('Digite as coordenadas do ponto A (x1 , y1 , z1) separadamente e sem vírgula: ').split())
        x2, y2, z2 = map(float, input('Digite as coordenadas do ponto B (x2 , y2 , z2) separadamente e sem vírgula: ').split())
        distanciaResult = distancia_3d(x1, y1, z1, x2, y2, z2)
        print('\nA distância entre os pontos A e B no espaço 3D é:', distanciaResult)
        print('Aperte qualquer tecla para retornar ao menu: ')
        key = read_key()
        os.system('cls')
        print('Retornando...')
        time.sleep(3)
        menu()
        
    menu()

if __name__ == "__main__":
    main()