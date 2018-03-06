import datetime
import time
import os


new_dic = {0: {1: ' 0000 ', 2: '00  00', 3: '00  00', 4: '00  00', 5: ' 0000 '},
           1: {1: '1111  ', 2: '  11  ', 3: '  11  ', 4: '  11  ', 5: '111111'},
           2: {1: ' 2222 ', 2: '22  22', 3: '   22 ', 4: '  22  ', 5: '222222'},
           3: {1: ' 3333 ', 2: '33  33', 3: '   333', 4: '33  33', 5: ' 3333 '},
           4: {1: '44  44', 2: '44  44', 3: '444444', 4: '    44', 5: '    44'},
           5: {1: '555555', 2: '55    ', 3: '55555 ', 4: '    55', 5: '55555 '},
           6: {1: ' 6666 ', 2: '66    ', 3: '66666 ', 4: '66  66', 5: ' 6666 '},
           7: {1: '777777', 2: '   77 ', 3: '  77  ', 4: ' 77   ', 5: '77    '},
           8: {1: ' 8888 ', 2: '88  88', 3: ' 8888 ', 4: '88  88', 5: ' 8888 '},
           9: {1: ' 9999 ', 2: '99  99', 3: ' 99999', 4: '    99', 5: ' 9999 '},
           10: {1: '   *  ', 2: '  * * ', 3: '   *  ', 4: '  * * ', 5: '   *  '},
           }


def hours(num1, num2, num3, num4, num5, num6):                                                                    #dot
    print(new_dic[num3][1], new_dic[num1][1], new_dic[10][1], new_dic[num4][1], new_dic[num2][1], new_dic[10][1], new_dic[num5][1], new_dic[num6][1])
    print(new_dic[num3][2], new_dic[num1][2], new_dic[10][2], new_dic[num4][2], new_dic[num2][2], new_dic[10][2], new_dic[num5][2], new_dic[num6][2])
    print(new_dic[num3][3], new_dic[num1][3], new_dic[10][3], new_dic[num4][3], new_dic[num2][3], new_dic[10][3], new_dic[num5][3], new_dic[num6][3])
    print(new_dic[num3][4], new_dic[num1][4], new_dic[10][4], new_dic[num4][4], new_dic[num2][4], new_dic[10][4], new_dic[num5][4], new_dic[num6][4])
    print(new_dic[num3][5], new_dic[num1][5], new_dic[10][5], new_dic[num4][5], new_dic[num2][5], new_dic[10][5], new_dic[num5][5], new_dic[num6][5])


while True:
    current_time = datetime.datetime.today()
    hour = current_time.strftime("%H")
    mint = current_time.strftime("%M")
    sec = (current_time.strftime("%S"))

    time.sleep(1)
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0

    if len(hour) == 2:
        num3 = int(hour[0])
        num1 = int(hour[1])
    else:
        num1 = int(hour)

    if len(mint) == 2:
        num4 = int(mint[0])
        num2 = int(mint[1])
    else:
        num2 = mint

    if len(sec) == 2:
        num5 = int(sec[0])
        num6 = int(sec[1])
    else:
        num6 = int(sec)
    os.system('cls' if os.name == 'nt' else 'clear')
    hours(num1, num2, num3, num4, num5, num6)


Print('Goodbye!')