# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:59:26 2021

@author: Jospin Amisi
         Co-founder at ADAI Circle

"""

"""

You have a set of unlabeled foods to eat and you attempt to identify what each item is. 
The probability of guessing each food correctly is in the list probs. 
You make a guess for every food and you pay cost dollars per guess. 
For each food you identify correctly, you receive get dollars. 

Write a Monte Carlo simulation that runs num_trials number of trials of this guessing game.

More specifically, write a function according to the specifications below (you are also given a helper function):
   
"""

def guessfood_sim(num_trials, probs, cost, get):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    counter = 0
    for i in range(num_trials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        picks = []
        for j in range(3):
            k = random.choice(bucket)
            picks.append(k)
            bucket.remove(k)
        if picks[0] == picks[1] == picks[2]:
            counter += 1
    return counter/num_trials  
