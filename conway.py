import os
import time
dead = []
alive = []
newline = []
while True:
    inpu4 = input("[o]pen-a-file / [n]ew (defalt=n)\n")
    inpu4 = inpu4.split(" ")
    if inpu4[0] == "o":
        if len(inpu4) > 1:
            if os.path.exists(inpu4[1]):
                file1 = open(inpu4[1], mode="r")
                file1 = file1.read()
                file1 = file1.split("\n")
                lines = len(file1) - 1
                index6 = 1
                for line in file1:
                    if line:
                        for i in line:
                            if i == "0":
                                dead.append(index6)
                            elif i == "1":
                                alive.append(index6)
                            index6 += 1
                        newline.append(index6)
                        index6 += 1
                    else:
                        break
                print(alive, dead, newline)
                break
            else:
                print(f'文件“{inpu4[1]}”不存在')
        else:
            print("请指定文件名")
    else:
        while True:
            try:
                lines = int(input('请输入输入行数：'))
                break
            except:
                print("请输入大于0的整数")
        index1 = 1
        inpu2 = []
        print('请输入初始状态：')
        while index1 <= lines:
            inpu1 = [i for i in input()]
            inpu2.append(inpu1)            #example: inpu2=[["0","0","0"],["1","1","1"],["0","0","0",]]
            index1 += 1
        currentline = 0
        index2 = 1
        for i in inpu2:
            for i in inpu2[currentline]:
                if i == "1":
                    alive.append(index2)    #alive=[5,6,7]
                elif i == "0":
                    dead.append(index2)    #dead=[1,2,3,9,10,11]
                index2 += 1
            currentline += 1
            newline.append(index2)
            index2 += 1
        break
print("输入'q'以退出")
index7 = 1
while True:
    dead1 = []
    alive1 = []
    adY1 = 0
    adY2 = 0
    adX1 = 0
    adX2 = 0
    for i in alive:
        if i > newline[lines - 2]:
            adY1 += 1
        if i < newline[0]:
            adY2 += 1
        if i in [i-1 for i in newline]:
            adX1 += 1
        if i in [i-newline[0]+1 for i in newline]:
            adX2 += 1
    #下
    if adY1 > 0:
        for i in range(newline[0]):
            dead.append(newline[lines - 1]+i + 1)
        newline.append(newline[lines-1] + newline[0])
        lines += 1
    
    #上
    if adY2 > 0:
        alive = [i+newline[0] for i in alive]
        dead = [i+newline[0] for i in dead]
        for i in range(1, newline[0]):
            dead.append(i)
        newline.append(newline[lines-1] + newline[0])
        lines += 1
    
    #右
    if adX1 > 0:
        alive2 = []
        alive4 = []
        for index4 in range(lines):
            alive3 = []
            for i in alive:
                if index4 == 0 and i<newline[0]:
                    alive3.append(i)
                if index4 > 0:
                    if i >= newline[index4-1] and i <= newline[index4]:
                        alive3.append(i)
            for a in alive3:
                alive4.append(a + index4)
        alive = alive4

        dead2 = []
        dead4 = []
        for index5 in range(lines):
            dead3 = []
            for i in dead:
                if index5 == 0 and i<newline[0]:
                    dead3.append(i)
                if index5 > 0:
                    if i >= newline[index5-1] and i <= newline[index5]:
                        dead3.append(i)
            dead3.append(newline[index5])
            for a in dead3:
                dead4.append(a + index5)
        dead = dead4
        
        newline1 = [i*(newline[0]+1) for i in range(1, len(newline)+1)]
        newline = newline1
    
    #左
    if adX2 > 0:
        alive2 = []
        alive4 = []
        for index4 in range(lines):
            alive3 = []
            for i in alive:
                if index4 == 0 and i<newline[0]:
                    alive3.append(i)
                if index4 > 0:
                    if i >= newline[index4-1] and i <= newline[index4]:
                        alive3.append(i)
            for a in alive3:
                alive4.append(a + index4 + 1)
        alive = alive4

        dead2 = []
        dead4 = []
        for index5 in range(lines):
            dead3 = []
            for i in dead:
                if index5 == 0 and i<newline[0]:
                    dead3.append(i)
                if index5 > 0:
                    if i >= newline[index5-1] and i <= newline[index5]:
                        dead3.append(i)
            dead3.append(newline[index5]-newline[0])
            for a in dead3:
                dead4.append(a + index5 + 1)
        dead = dead4
        
        newline1 = [i*(newline[0]+1) for i in range(1, len(newline)+1)]
        newline = newline1
    

    nearestblocks = [-newline[0], -newline[0]+1, -newline[0]+2, 0, 2, newline[0], newline[0]+1, newline[0]+2]
    for index3 in range(1, newline[lines-1]):
        x = 0
        if index3 in alive:
            for i in nearestblocks:
                if i in alive:
                    x += 1
            if x == 2 or x == 3:
                alive1.append(index3)
            else:
                dead1.append(index3)
        elif index3 in dead:
            for i in nearestblocks:
                if i in alive:
                    x += 1
            if x == 3:
                alive1.append(index3)
            else:
                dead1.append(index3)
        nearestblocks = [i+1 for i in nearestblocks]
    for i in range(1, newline[lines-1]+1):
        if i in alive1:
            print("■", end="")
        elif i in dead1:
            print("□", end="")
        elif i in newline:
            print("")
    dead = dead1
    alive = alive1

    if index7 <= 1 :
        inpu3 = input("")
        inpu3 = inpu3.split(" ")
        if inpu3[0] == "q":
            quit()
        if inpu3[0] == "s":
            if len(inpu3) == 2:
                file = open(inpu3[1], mode="w")
            else:
                file = open("save.txt", mode="w")
            for i in range(1, newline[lines-1]+1):
                if i in alive1:
                    file.write("1")
                elif i in dead1:
                    file.write("0")
                elif i in newline:
                    file.write("\n")
            file.close()
        if inpu3[0] == "n":
            if len(inpu3) == 2:
                try:
                    index7 = int(inpu3[1])+1
                except:
                    print("请输入整数")
            else:
                print("请指定行数")
        elif inpu3[0] != "":
            print("command not found")
    
    else:
        index7 -= 1
        time.sleep(1)
        print(index7)
        continue
