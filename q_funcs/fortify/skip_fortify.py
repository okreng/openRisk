"""
This file contains the Q function for random fortification
Each territory held by the player has an equal probability of being selected
Output is a random vector of size T^2
Assuming that it is strictly better to fortify somewhere rather than not fortify
Env will not fortify only if there are no valid moves specified

Env will determine how many troops to move
TODO: How to determine this?  Is there an optimal decision?

"""

import numpy as np
import random

global MAX_ARMIES #max armies per player

class SkipFortify():
	"""
	Class to hold the maximum success policy
	"""
	def __init__(self, T, act_list):
		"""
		Constructor so RandomFortify can be held as an object
		:param T: int the length of the state vector
		:param act_list: 2D list mapping edges to territories
		:return : none
		"""
		self.T = T
		self.act_list = act_list
		return

	def call_Q(self, state_vector, update=None, action_taken=None, target=None, loss_weights=None):
		"""
		Function for executing maximum battle success
		:param state_vector: np-array 1D vector of armies on territory
		:return action_vector: np-array 1D vector of edges to attack along
		"""

		action_vector = np.zeros(len(self.act_list))
		action_vector[-1] = 1

		return action_vector

	def get_action(self, state_vector, valid_mask, update=None, action_taken=None, target=None, loss_weights=None):
		"""
		Chooses an action based on the state vector and valid_mask inputted
		"""
		q = self.call_Q(state_vector)
		return np.argmax(q)
