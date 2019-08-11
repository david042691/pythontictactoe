#python project 1 tic tac toe game
Game_end= False
Player1=''
Player2=''
def printstring(location):
	gameboard=f'			|			|\n		{location[1][0]}	|		{location[2][0]}	|	{location[3][0]}\n			|			|\n------------------------------------------------------------------------\n			|			|\n		{location[4][0]}	|		{location[5][0]}	|	{location[6][0]}\n			|			|\n------------------------------------------------------------------------\n			|			|\n		{location[7][0]}	|		{location[8][0]}	|	{location[9][0]}\n			|			|\n'
	print(gameboard)

def thegame(player1):
	locationreset=[[],['1',False],['2',False],['3',False],['4',False],['5',False],['6',False],['7',False],['8',False],['9',False]]
	location=[[],['1',False],['2',False],['3',False],['4',False],['5',False],['6',False],['7',False],['8',False],['9',False]]
	temp=''
	if (player1=='O'):
		itsplayerturn= True
		temp='X'
	else:
		itsplayerturn=False
		temp='O'

	while True:
		Inputed= False
		printstring(location)

		if itsplayerturn==True:
			print('Player 1 turn: ')
		else: print('Player 2 turn: ')

		newentry=input('choose a location: ')

		locator=1
		while locator <=9:
			if location[locator][0]== newentry:
				if itsplayerturn==True:
					location[locator][0]= Player1
					location[locator][1]=True
					Inputed=True
				else:
					location[locator][0]=temp
					Inputed=True
					location[locator][1]=True
			if Inputed==True:
				break
			locator+=1
		
		if Inputed==True:
			thereafalse=False
			if location[1][0]==location[2][0]==location[3][0] or location[1][0]==location[4][0]==location[7][0] or location[1][0]==location[5][0]==location[9][0] or location[2][0]==location[5][0]==location[8][0] or location[9][0]==location[6][0]==location[3][0] or location[3][0]==location[5][0]==location[7][0] or location[4][0]==location[5][0]==location[6][0] or location[7][0]==location[8][0]==location[9][0]:
				printstring(location)
				if itsplayerturn==True:
					print('Player 1 win')
				else: print('Player 2 win')
				break
			else:
				i=1
				while i<=9:
					if False in location[i]:
						thereafalse=True
						break
					i+=1
			if thereafalse== True:
				itsplayerturn= not itsplayerturn
			elif thereafalse==False:
				print('TIE')
				break
				
			

		elif Inputed==False:
			print('Please choose another location')
			continue

while Game_end == False:
	restartgame= input('Start Game? y or n: ')
	if restartgame== 'n':
		break
	elif restartgame== 'y':
		pass
	else: continue
	chosen= input('Player 1 Please Choose o or x (default:Player 1 is o):')
	if chosen == 'x':
		Player1='X'
		Player2='O'
	else:
		Player1='O'
		Player2='X'
	thegame(Player1)