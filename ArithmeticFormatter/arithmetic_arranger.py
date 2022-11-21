def arithmetic_arranger(problems,displayAnswers=False):
  """Display up to 5 arithmetic problems in column notation.
  Max length of 4 per operand. Only accepts + and - operators."""  
  
  #Check number of problems
  if len(problems)>5:
      return "Error: Too many problems."  

  #2D array to hold data structure
  builder = [
    [], #First line
    [], #Second line
    [] #Answer
  ]

  operators = [] #stores the operators in order.
  widths = [] #stores the required width for each problem

  for problem in problems:
    separatedProblem = problem.split(" ") #Split the problem string
    
    #Check lengths of operands
    if len(separatedProblem[0]) >4 or len(separatedProblem[2]) >4:
      return "Error: Numbers cannot be more than four digits."

    if not separatedProblem[0].isnumeric() or not separatedProblem[2].isnumeric():
      return "Error: Numbers must only contain digits."
      
    #Assign operands to data structures
    builder[0].append(separatedProblem[0]) #Assign the first operand to the first line list
    builder[1].append(separatedProblem[2]) #Assign the second operand to the second line list
    
    #Check that only correct operators are used.
    if separatedProblem[1] == "*" or separatedProblem[1] == "/":
      return "Error: Operator must be '+' or '-'."

    operators.append(separatedProblem[1]) #Assign the operator to operators list

    #Calculate the answer and store in data structure
    if separatedProblem[1] == "+":
      builder[2].append( str(int(separatedProblem[0]) 
                             + int(separatedProblem[2])) )
    else:
      builder[2].append( str(int(separatedProblem[0]) 
                             - int(separatedProblem[2])) )


  #Calculate the required width of each problem.
  for i in range(len(problems)):
    maxWidth = max([len(builder[0][i]), #First operand
                    len(builder[1][i]) #Second operand
                    ])
    widths.append(maxWidth)

  #Structure for the output strings
  output= [
    "", #Operand 1
    "", #Operand 2
    "", #Dashes
    "", #Answer
  ]

  #Construct line 1, padding spaces.
  for i in range(len(problems)):

    #Operand 1 printing
    output[0] += "  " #2 spaces to account for the operator
    output[0] += builder[0][i].rjust(widths[i]) #Add the operand, padded with spaces.    
    #Operand 2 printing
    output[1] += operators[i] + " " #Operator followed by space
    output[1] += builder[1][i].rjust(widths[i]) #Add operand 2, padded with spaces

    #Dashes printing
    numDashes = 2 + widths[i]
    output[2] += "-" * numDashes

    #Answer Printing
    #Answer can be bigger than strings above, so no deliberate space for operator
    #Instead, adds two to widths for padding.
    output[3] += builder[2][i].rjust(widths[i]+2)

    #4 spaces to separate problems, unless it's the last problem
    if i != len(problems) -1:
      output[0] += "    "
      output[1] += "    "
      output[2] += "    "
      output[3] += "    "

  #Output as single string
  if displayAnswers:
    return output[0] + "\n" + output[1] + "\n" + output[2] + "\n" + output[3]
  return output[0] + "\n" + output[1] + "\n" + output[2]