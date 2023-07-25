
players = int(input('enter the number of players:'))
player_scores = [0 for _ in range(players)]
print(len(player_scores))

print(player_scores)
# player_scores is a list which have have scores of the players 

#  [0 for _ in range(players)]
#  the above code shows that if the number of the players is given as 3 for example then the list will have three zeros considering it as the scores for the players 
#  '_' is because it is a convention to use where we not using the loop variable.