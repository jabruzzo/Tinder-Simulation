# Program: TINDER_SIM.py
# Author: JOSEPH M ABRUZZO
# Date: Aug. 2016
# ------------------------
# This program implements an original agent-based simulation of heterosexual user behavior on the dating app Tinder.
# The intention of the model is to explain the origin of the disparity between male and female mate selectivity on 
# the app.


import random
import math
import gc
import io
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


NUM_TIME_STEPS = 10000
NUM_AGENTS = 200
MALE_SELECTIVITY_INIT = 0.55
FEMALE_SELECTIVITY_INIT = 0.45
PARAM_LAMBDA = 2


def match(p1):
	p = random.random()

	if p <= p1:
		return True

	return False


def turn(males, females):
	m = random.randint(0, NUM_AGENTS - 1)
	f = random.randint(0, NUM_AGENTS - 1)

	male = males[m]
	female = females[f]

	if match(male) == True and match(female) == False:
		males[m] = (1 + male) / float(PARAM_LAMBDA)
		
	if match(male) == False and match(female) == True:
		females[f] = (1 + female) / float(PARAM_LAMBDA)

	if match(male) == True and match(female) == True:
		males[m] = male - male / float(PARAM_LAMBDA)
		females[f] = female - female / float(PARAM_LAMBDA)


def main():
	males = [MALE_SELECTIVITY_INIT] * NUM_AGENTS
	females = [FEMALE_SELECTIVITY_INIT] * NUM_AGENTS

	maleAvgs = [MALE_SELECTIVITY_INIT]
	femaleAvgs = [FEMALE_SELECTIVITY_INIT]

	for i in range(NUM_TIME_STEPS):
		turn(males, females)

		maleAvgs.append(sum(males) / float(len(males)))
		femaleAvgs.append(sum(females) / float(len(females)))

	t = range(NUM_TIME_STEPS + 1)

	plt.plot(t, maleAvgs, 'r--', t, femaleAvgs, 'b--')
	plt.xlabel("Time step")
	plt.ylabel("Average selectivity (Percent right swipes)")
	red_patch = mpatches.Patch(color='red', label='Male agents')
	blue_patch = mpatches.Patch(color='blue', label='Female agents')

	plt.legend(handles=[red_patch, blue_patch], loc=2)
	plt.show()


main()