class Category:
  #Constructor. Label is the chosen category.
  def __init__(self,label):
    self.label = label #Category
    self.ledger = [] #Holds dicts.

  #Returning as a string
  def __repr__(self):
    """Returns the ledger as a formatted list."""
    outputBuilder = [] #Holds the lines as they're made
    header = self.label.center(30,"*") #Center the label
    outputBuilder.append(header)
    #Build each entry
    for item in self.ledger:
      slicedDescription = item["description"][:23] #Get the first 23 characters
      amountToString = f'{item["amount"]:.2f}' #Turn the amount into a 2dp string
      itemOutput = slicedDescription.ljust(23," ") #Left just the description and pad if needed
      itemOutput += amountToString.rjust(7," ") #Right just the number and pad
      outputBuilder.append(itemOutput) #Add the row
    outputBuilder.append(f"Total: {self.get_balance():.2f}") #When done, add the balance.

    #Build the string to output
    outputString = ''
    for i in range(len(outputBuilder)):
      #Catch the different behaviour of last entry
      if i == len(outputBuilder) -1:
        outputString += outputBuilder[i]
      #If not, add the line and a new line.
      else:
        outputString += outputBuilder[i] + "\n"

    return outputString

  def deposit(self,amount,description=""):
    """Add an amount and an optional description to ledger."""
    #Adds spend as dict.
    depositObject = {"amount":amount,"description":description}
    #Add to ledger and return
    return self.ledger.append(depositObject)

  def withdraw(self,amount,description=""):
    """Withdraws an amount. Takes an optional description. Will return False if funds not available."""
    if self.check_funds(amount): #If there's enough in the balance
      self.ledger.append({"amount":-amount,"description":description}) #Update the ledger
      return True #Confirm transaction
    return False #Reject transaction

  def get_balance(self):
    """Get current balance of ledger."""
    balance = 0 #Init balance
    for item in self.ledger: #Add up all of the amounts in the ledger
      balance += item["amount"]
    return balance #Return the current balance

  def transfer(self,amount,otherCategory):
    """Move funds to another Category instance. Takes an amount and the instance to transfer to.
    Will return False if funds not available."""
    if self.check_funds(amount): #Check balnce
      self.withdraw(amount,"Transfer to {}".format(otherCategory.label)) #Update sending ledger
      otherCategory.deposit(amount,"Transfer from {}".format(self.label)) #Update receiving ledger
      return True #Confirm transaction
    return False #Reject transaction

  def check_funds(self,amount):
    """Check if there are enough funds for a transaction. Returns True or False."""
    if self.get_balance() - amount <0:
      return False
    return True
    
def create_spend_chart(categories):
  """Takes list of categories. Returns a bar chart."""
  #Calculate percentages to the nearest 10.
  categoryObjects = [] #Holds an object for each category given
  totalAllSpends = 0 #Adds up the total spend so we can calc percentages.
  
  for category in categories: 
    totalSpend = 0 #Spend of this category
    for entry in category.ledger:
      if entry["amount"] < 0: #Only find withdrawals, not deposits.
        totalSpend += entry["amount"]
    #Note - total spend is flipped for easier percentages
    categoryObjects.append({"label":category.label,"amount":-totalSpend}) 
    #Note - subtracting total spend so we end up with a positive number.
    totalAllSpends -= totalSpend

  percentages = [] #Store the percentages
  longestLabel = 0 #Find the longest label name, used in our output below.
  for category in categoryObjects:
    percent = (category["amount"]/totalAllSpends) *100 #Turn the amount into a percent of the whole.
    
    #Note - this doesn't round to a percent, but to a single digit.
    #This saves an extra process later on.
    roundedPercent = int(percent/10) #Rounds down to a digit representing a percentage /10

    #Note - add one to the percent because the chart requires a o in the 0 row.
    #Therefore 2 o's is 10, so we need to add 1 to all results.
    roundedPercent += 1
    percentages.append(roundedPercent) #Add it to the list above.

    #While we're looping - find the longest name. Used to output columns below
    if len(category["label"])>longestLabel:
      longestLabel = len(category["label"])
      
  #Prepare the output
  outputColumns = []
  legend = []
  for i in range(100,-1,-10):
    legend.append(str(i).rjust(3)+"|")

  outputColumns.append(legend)
  #Create a string of o's for each category
  for percent in percentages:
    outputString = "o" * percent #Add the number of o's to match the percent
    formattedOutputString = outputString.rjust(11) #Padd with spaces to the left
    outputList = [*formattedOutputString] #* splits the string into a list of chars
    outputColumns.append(outputList) #Add the column to the cols to render

  #String to hold the top half of output
  topHalfString =""
    
  #Print the graph
  for i in range(11): #11 because 100 - 0 in increments of 10
    row="{}".format(legend[i]) #Create a row with the right legend
    for j in range(1,len(outputColumns)): #for the remaining columns to print...
      row += " {} ".format(outputColumns[j][i]) #Add the matching character
    topHalfString +=(row+" \n") #Populate the first half of the output

  #Calculate the number of dashes needed for divider
  numDashes = ((len(outputColumns) -1 ) *3) + 1#3 for each category, + 1 at the end. Skip the legend.
  dividerString = "    " + ("-" *numDashes) + "\n"

  #Get the labels
  labelColumns = []
  for object in categoryObjects:
    #Mammoth method here.
    #Get the label, pad it to the length of the longest label. Capitalise the first letter.
    labelColumns.append(object["label"].ljust(longestLabel).capitalize())

  #String to hold the bottom half
  bottomHalfString = ""
  
  #Create the rows
  for i in range(longestLabel):
    row = "    " #4 spaces to skip legend
    for j in range(len(labelColumns)): #For each category in use...
      row += " {} ".format(labelColumns[j][i]) #Add the matching letter vertically.

    #Catch the different behaviour of the bottom row.
    if i == longestLabel-1: 
      bottomHalfString += row + " "
    else:
      bottomHalfString += row + " \n"

  #Build the output string.
  outputString = "Percentage spent by category\n"
  outputString += topHalfString
  outputString += dividerString
  outputString += bottomHalfString
 
  return outputString
  
