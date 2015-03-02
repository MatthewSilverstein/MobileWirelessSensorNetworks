""" This module will handle graphing functions live steps vs coverage """
import matplotlib.pyplot as plt

def graphCoverage(steps, coverage):
	plt.plot(steps, coverage)
	plt.show()

def graphMoves(steps, moves):
	plt.plot(steps, moves)
	plt.show()