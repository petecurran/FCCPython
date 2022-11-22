def add_time(start, duration, day=None):
  """
  Adds an amount of time to a 12 hour format digital clock. 
  """
  #Cleaning up the inputs - start
  splitTime = start.split(":")
  getMinutesAmPm = splitTime[1].split(" ")

  #Cleaning up the inputs - duration
  splitDuration = duration.split(":")  

  #Clean start time
  hours = int(splitTime[0])
  minutes = int(getMinutesAmPm[0])

  #Turn am / pm into an integer. Evens are am, Odds are pm.
  if getMinutesAmPm[1].lower() == "am":
    ampm = 0
  else:
    ampm = 1

  #Clean duration
  durationHours = int(splitDuration[0])
  durationMinutes = int(splitDuration[1])

  #Add the times together
  newMinutes = (minutes+durationMinutes) % 60 #Calc new minutes
  hoursFromMinutes = (minutes + durationMinutes) // 60 #Check if we rolled over an hour
  
  newHour = (hours + durationHours + hoursFromMinutes) % 12 #Calc new hour  
  cycles = (hours + durationHours + hoursFromMinutes) // 12 #Check if we rolled over am / pm
  #ampm += cycles #add the number of cycles to am / pm integer

  #Calc whether we're on the next day.
  #Each new day begins on an even number
  numDaysPassed = (ampm + cycles)//2

  #If a day has been passed in...
  if day != None:
    #Work out how many days have passed
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    currentDayIndex = days.index(day.lower()) #find the index of the current day
    newDayIndex = (currentDayIndex + numDaysPassed) % 7 #Find the new day index, loop if needed.
    newDay = days[newDayIndex].capitalize()
  
  #Calculate the output
  if newHour == 0: #Convert 0's to 12's to match clock.
    newHour = 12
  hour = str(newHour) #New hour
  minute = str(newMinutes).rjust(2,"0") #New minute, padded if single digit
  #Calc am/pm. Evens are AM.
  if (ampm + cycles) % 2 == 0:
    suffix = "AM"
  else:
    suffix = "PM"

  #Formatted output string
  new_time = "{}:{} {}".format(hour,minute,suffix)
  if day != None:
    new_time += ", {}".format(newDay)
  if numDaysPassed == 1:
    new_time += " (next day)"
  elif numDaysPassed > 1:
    new_time += " ({} days later)".format(numDaysPassed)

  return new_time