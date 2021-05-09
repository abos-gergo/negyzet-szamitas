import math
import time
import os

def clear_console():
    os.system('cls')

def draw_line():
    print('----------------------------------------------------------')

def negyzet_kerulet():
    print('Négyzet kerületszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Terület')
    print('2. Oldal hossza')
    print('3. Átló hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()
    if opcio == 1:
        terulet : float = 0
        while terulet <= 0:
            terulet : float = float(input('Adja meg a négyzet területét! (cm2)'))
            if terulet <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = math.sqrt(terulet)
        kerulet : float = oldal * 4
        print(f'A négyzet kerülete: √({terulet}) * 4 = {kerulet} centiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        oldal : float = 0
        while oldal <= 0:
            oldal : float = float(input('Adja meg az oldal hosszát! (cm)'))
            if oldal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        terulet : float = oldal ** 2
        print(f'A négyzet területe: {oldal} ^ 2 = {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 3:
        diagonal : float = 0
        while diagonal <= 0:
            diagonal : float = float(input('Adja meg a négyzet átlójának hosszát! (cm)'))
            if diagonal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = math.sqrt((diagonal ** 2) / 2)
        terulet : float = oldal ** 2
        print(f'A négyzet területe: √(({diagonal} ^ 2) / 2) ^ 2 = {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def negyzet_terulet():
    print('Négyzet területszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Kerület')
    print('2. Oldal hossza')
    print('3. Átló hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()

    if opcio == 1:
        kerulet : float = 0
        while kerulet <= 0:
            kerulet : float = float(input('Adja meg a négyzet kerületét! (cm)'))
            if kerulet <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = kerulet / 4
        terulet : float = oldal ** 2
        print(f'A négyzet területe: ({kerulet} : 4) ^ 2 = {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        oldal : float = 0
        while oldal <= 0:
            oldal : float = float(input('Adja meg az oldal hosszát! (cm)'))
            if oldal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        terulet : float = oldal ** 2
        print(f'A négyzet területe: {oldal} ^ 2 = {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 3:
        diagonal : float = 0
        while diagonal <= 0:
            diagonal : float = float(input('Adja meg a négyzet átlójának hosszát! (cm)'))
            if diagonal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = math.sqrt((diagonal ** 2) / 2)
        terulet : float = oldal ** 2
        print(f'A négyzet területe: √(({diagonal} ^ 2) / 2) ^ 2 = {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def main():
    print("Program a négyzet kerületének és területének kiszámolására.")
    draw_line()
    while True:
        print('Mit szeretne tenni?')
        print('1. Kerület kiszámolása')
        print('2. Terület kiszámolása')
        print('3. Kilépés a programból')
        opcio : int = int(input('Adja meg az opció számát: '))
        draw_line()
        if opcio == 1:
            negyzet_kerulet()
        elif opcio == 2:
            negyzet_terulet()
        elif opcio == 3:
            print('Kilépés a programból...')
            quit()

if __name__ == "__main__":
    main()