#tictactoe game

#to assingn x or o to player
def player_configuation():
    print("Welcome to the tic tac toe game")
    player_one="no"
    while player_one!="O" and player_one!="X": 
        player_one=input("Player 1: Would you like to choose X or O: ")
    if(player_one=="X"):
        player_two="O"
    else:
        player_two="X"
    return (player_one,player_two)

#to display initial board
def display_board(row):
    print(row[0]+" |"+row[1]+" |"+row[2])
    print("---------")
    print(row[3]+" |"+row[4]+" |"+row[5])
    print("--------")
    print(row[6]+" |"+row[7]+" |"+row[8])

#to input from player1
def acc_input_one(player_one,row):
    print("player1 has the first turn")
    index=int(input("Enter a number from 0 to 8: "))
    row[index]=player_one
    return row

#to input from player2  
def acc_input_two(player_two,row):
    print("palyer2 has the turn")
    index=int(input("Enter a number from 0 to 8: "))
    row[index]=player_two
    return row

#to check for winning 3 streaks row wise 
def check_row(row):
    x="".join(row)
    for i in (0,3,6):
        if x[i:i+3:1]=="XXX":
            print("Player one has won")
            return True
        elif x[i:i+3:1]=="OOO":
            print ("player two has won")
            return True

#to check for winning 3 streaks column wise 
def check_column(row):
    x="".join(row)
    for i in (0,1,2):
        if x[i:i+7:3]=="XXX":
            print("Player one has won")
            return True
        elif x[i:i+7:3]=="OOO":
            print ("player two has won")
            return True

#to check for winning 3 streaks dagonal  wise
def check_dia(row):
    x="".join(row)
    for i in (0,2):
        if x[i:i+9:4]=="XXX":
            print("Player one has won")
            return True
        elif x[i:i+9:4]=="OOO":
            print ("player two has won")
            return True

#to ask whther aperson want to continue or not after finishing a game 
def game_on():
    cont=input("whether u like to continue(Y/N): ")
    if cont=="Y":
        return True
    else:
        return False

def main():
    row=[" "," "," "," "," "," "," "," "," "]
    (player_one,player_two) =player_configuation()
    display_board(row)
    z=1
    while z:
        for i in row:
            while z:
              if i==" ":
                row=acc_input_one(player_one,row)
                display_board(row)
                if check_row(row) or check_column(row) or check_dia(row):
                  if not game_on():
                      z=0
                      break
                  else:
                      row=[" "]*10
                row=acc_input_two(player_two,row)
                display_board(row)
                if check_row(row) or check_column(row) or check_dia(row):
                  if not game_on():
                      z=0
                      break
                  else:
                      row=[" "]*10
    print("Thank you for playing!")    
            
main()