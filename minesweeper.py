import random
#Start Game
print("Hello to MineSweeper")
print("Choose Size: from 5x5 to 10x10")
size=-1
#Choose size
while size == -1:
    try:
        size = int(input("Enter a number from 5 to 10 to choose size: \n"))
        if size > 10 or size < 5:
            size = -1
    except:
        print("please enter a correct number \n")
#Initialize map
map = []


underscores = int(size**1.5)*"_"+"_"
def init_map():
    map_dict.clear()
    map.clear()
    total_bombs=0
    for i in range(size):
        column = []
        for j in range(size):
            rand = random.randint(0,10)
            if(rand > 6 and total_bombs <3):
                total_bombs +=1
                column.append("mine")
            else:
                column.append("safe")
        map.append(column)
    print(underscores+"MineSweeper"+underscores)       
    for i in range(size):
        for j in range(size):
            location = i+size*j+1
            if(location < 10):
                print(  str(i+size*j+1),  end ="       ")
            else:
                print(  i+size*j+1  ,  end ="      ")
        print("")
    return total_bombs          
map_dict = {}
def update_map(location,action):
    if(action == "reveal" ):
        map_dict[location]="  "
    elif(action == "bomb"):
        map_dict[location]="* "
    elif(action == "fake bomb"):
        map_dict[location] = "*-"
    else:
        map_dict[location]=str(action)+" " 
    print(underscores+"MineSweeper"+underscores)    
    for i in range(size):
        for j in range(size):
            spot = i+size*j+1
            if(spot in map_dict.keys() ):
                if(spot < 10):
                    print('\033[1m'+ map_dict[spot] + '\033[0m',  end ="      ")
                else:
                    print('\033[1m' +  map_dict[spot] + '\033[0m' ,  end ="      ")
            else:
                if(spot < 10):
                    print( str(spot) ,  end ="       ")
                else:
                    print(  spot  ,  end ="      ")
        print("")             

def start_game(total_bombs):
    bombs_found = 0
    print("Start Your Game By Choosing Your First Step")
    picked = -1
    game_on = True
    available_sweeps = [i+1 for i in range(size**2)]
    while(game_on):
        picked = -1
        while(picked == -1):
            try:    
                picked = int(input("Choose a Number From 1 to {} \n".format(size**2)))
                if(picked>size**2 or picked < 1  or picked  not in available_sweeps):
                    picked =- 1
                    print("please choose a valid number!")
            except:
                print("please choose a valid number!")
        available_sweeps.remove(picked)
        while(True):
            pick = input("please choose your guess for the chosen number (pick 1 for mine or 2 for safe) \n")
            if(pick == '1' or pick == '2'):
                break
            print("please choose a valid pick")
        j=int(((picked-1)-(picked-1)%size)/size)
        i =(picked-1)%size
        if(map[i][j] == "mine" and pick == "1"):
            bombs_found += 1
            update_map(picked,"bomb")
        elif(map[i][j] == "mine" and pick=="2"):
            update_map(picked,"bomb")
            game_on = False
            game_over(False)
        elif(map[i][j]=="safe" and pick=="2"):
            bombs_around = count_around(i,j)
            if(bombs_around == 0):
                update_map(picked,"reveal")
            else:
                update_map(picked,bombs_around)  
        else:
            available_sweeps.append(picked)
            update_map(picked,"fake bomb")
        print("Remaining bombs: {}".format(total_bombs-bombs_found))
        if(bombs_found == total_bombs):
            game_over(bombs_found == total_bombs)      
            return   

def count_around(i,j):
    bombs_num = 0
    if i>0:
        if(map[i-1][j]=="mine"):
            bombs_num += 1
        if j>0:
            if(map[i-1][j-1]=="mine"):
                bombs_num += 1   
        if j<size-1:
            if(map[i-1][j+1]=="mine"):
                bombs_num += 1
    if i<size-1:
        if(map[i+1][j]=="mine"):
            bombs_num += 1
        if j>0:
            if(map[i+1][j-1]=="mine"):
                bombs_num += 1
        if j<size-1:
            if(map[i+1][j+1]=="mine"):
                bombs_num += 1    
    if j>0:
        if(map[i][j-1]=="mine"):
            bombs_num += 1    
    if j<size-1:
        if(map[i][j+1]=="mine"):
            bombs_num += 1
    return bombs_num        
def game_over(bool):
    if(bool):
        print("VICTORY")
    else:
        print("DEFEAT")    
    while(True):
        again = input("Do you want to play again (y/n)?\n")
        if again == "y":    
            total_bombs=init_map()
            start_game(total_bombs)
            break
        if again == "n":
            print("GOODBYE :)")
            break
        else:
            print("Please choose either y or n")    
#Start game

total_bombs=init_map()
start_game(total_bombs)