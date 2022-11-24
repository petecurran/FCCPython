import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **kwargs):
    self.contents = [] #Holds the balls in the bag

    for key in kwargs: #Go through the keys...
      #Get the number of balls using that key
      for i in range (kwargs[key]):
        #Add that many balls to the bag
        self.contents.append(key)

  def draw(self,number):
    """Draws a set number of balls from the hat"""
    #If the request is higher than the remaining balls
    #Return them all
    if number > len(self.contents):
      return self.contents

    sample = [] #Holds the sampled balls
    for i in range(number):
      #Pick an index
      choice = random.randrange(0,len(self.contents))
      #Pop it from the list
      ball = self.contents.pop(choice)
      #Add it to the sample
      sample.append(ball)

    return sample
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  """Calculates the probability of an outcome using a set number of experiments."""
  #Initialise number of successes
  matches = 0
  
  #Run all experiments
  for i in range(num_experiments):
    #Create a deep copy of the object so we don't overwrite attributes
    thisHat = copy.deepcopy(hat)
    #Draw the number of balls for the experiment
    ballsDrawn = thisHat.draw(num_balls_drawn)

    #Flag to check for matches. Assumes true.
    match = True
    
    #Map the result to a dictionary so we can compare with expected balls
    result = {}
    for key in expected_balls:
      #Count the number of balls matching the input key
      #Assign the key and count to result dict above.
      result[key] = ballsDrawn.count(key) 
      #See if we can disprove a match.
      #We're looking for AT LEAST the right number of balls.
      if result[key] < expected_balls[key]:
        match = False
        
    #If the match wasn't disproven, update the total number of matches.
    if match == True:
      matches += 1
  
  return matches / num_experiments
    
    
