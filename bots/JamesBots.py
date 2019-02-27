#!/usr/bin/python

from utils.log import log
from bots.simpleBots import BasicBot
import random

def get_Chosen():
	nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	chosen = []
	while True:
		idx = random.randint(0,len(nums)-1)
		if not nums[idx] in chosen:
			chosen.append(nums[idx])
			total = 0
			for x in chosen:
				total = total + x
			total += nums[idx]
			nums.remove(nums[idx])
			if total >= 46:
				break
	chosen.sort(reverse = True)
	return chosen



class HalfPointsBot(BasicBot): #can extend one of the simple bots, BasicBot, ObviousBot, RandomBot
	#these are the three methods called by GameArena.  If your bot doesn't need one, you can delete it.

	def __init__(self, player_num, num_players, num_cards):
		#Bot is initialized once at the beginning of the competition, and persists between games.
		self.chosen = get_Chosen()
		self.player_num = player_num #your player number
		self.num_players = num_players #normally 2, but ideally, you should allow your bot to gracefully handle more
		self.num_cards = num_cards
		return
	def end_game(self, result):
		#Called by GameArena upon game end. Result is the number of the winning bot previous game, -1 if tie
		#Likely want to reset any tracking variables that persist between rounds here.
		self.chosen = get_Chosen()
		return
	def take_turn(self, game_state, verbose = False):
		"""
		Called by GameArena when it's time to take your turn.  You are passed a "game" object with this info to work with:

		card = (int) value 1 thru num_cards

		variables available to your bot:
			self.player_num  = your player number
			self.num_players = normally 2, but ideally, you should allow your bot to gracefully handle more
			self.num_cards = normally 13, but ideally, you should allow your bot to gracefully handle any amount
			
			game_state.current_won_cards[player_num][cards] = list of cards each player has won so far
			game_state.current_scores[player_num]           = current score of each each player
			game_state.current_hands[player][cards]			= list of cards currently in each player's hand
			game_state.current_prizes[cards]                = list of prizes remaining
			game_state.prize_this_round (int)               = current prize showing for this round
		"""

		#use log(self,"text") instead of print("text") so we know what module is printing, for cleaner output
		#log(self,"This is how I do a print statement!") 
		

		#a completed bot should wrap all log statments in verbosity checks, so we don't get a flooded console if running 1000 iterations
		if verbose:
			log(self, str(self.chosen) )


		#do fun logic
		if not game_state.prize_this_round in self.chosen:
			return min(game_state.current_hands[self.player_num])
		else:
			finder = self.chosen.index(game_state.prize_this_round)
			return game_state.current_hands[self.player_num][-finder:][0]


#class HalfPointsAdaptBot(BasicBot): #can extend one of the simple bots, BasicBot, ObviousBot, RandomBot
#	#these are the three methods called by GameArena.  If your bot doesn't need one, you can delete it.
#
#	def __init__(self, player_num, num_players, num_cards):
#		#Bot is initialized once at the beginning of the competition, and persists between games.
#		self.chosen = []
#		self.player_num = player_num #your player number
#		self.num_players = num_players #normally 2, but ideally, you should allow your bot to gracefully handle more
#		self.num_cards = num_cards
#		for i in range(0,10000):
#			num = random.randint(1,13)
#			if not num in self.chosen:
#				self.chosen.append(num)
#				total = 0
#				for x in self.chosen:
#					total = total + x
#				if total >= 46:
#					break
#		self.chosen.sort(reverse = True)
#		return
#	def end_game(self, result):
#		#Called by GameArena upon game end. Result is the number of the winning bot previous game, -1 if tie
#		#Likely want to reset any tracking variables that persist between rounds here.
#		for i in range(0,10000):	
#			num = random.randint(1,13)
#			if not num in self.chosen:
#				self.chosen.append(num)
#				total = 0
#				for x in self.chosen:
#					total = total + x
#				if total >= 46:
#					break
#		self.chosen.sort(reverse = True)
#		return
#	def take_turn(self, game_state, verbose = False):
#		"""
#		Called by GameArena when it's time to take your turn.  You are passed a "game" object with this info to work with:
#
#		card = (int) value 1 thru num_cards
#
#		variables available to your bot:
#			self.player_num  = your player number
#			self.num_players = normally 2, but ideally, you should allow your bot to gracefully handle more
#			self.num_cards = normally 13, but ideally, you should allow your bot to gracefully handle any amount
#			
#			game_state.current_won_cards[player_num][cards] = list of cards each player has won so far
#			game_state.current_scores[player_num]           = current score of each each player
#			game_state.current_hands[player][cards]			= list of cards currently in each player's hand
#			game_state.current_prizes[cards]                = list of prizes remaining
#			game_state.prize_this_round (int)               = current prize showing for this round
#		"""
#
#		#use log(self,"text") instead of print("text") so we know what module is printing, for cleaner output
#		#log(self,"This is how I do a print statement!") 
#		
#
#		#a completed bot should wrap all log statments in verbosity checks, so we don't get a flooded console if running 1000 iterations
#		if verbose:
#			log(self, str(self.chosen) )
#
#
#		#do fun logic
#		if not game_state.prize_this_round in self.chosen:
#			return min(game_state.current_hands[self.player_num])
#		else:
#			finder = self.chosen.index(game_state.prize_this_round)
#			return game_state.current_hands[self.player_num][-finder:][0]