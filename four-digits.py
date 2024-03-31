import random

numberList = "0123456789"

fourDigitsActual = []

for i in range(4):
  numberListLen = len(numberList)
  randomIndexChosen = random.randint(0,numberListLen-1)
  digitChosen = numberList[randomIndexChosen]
  fourDigitsActual.append(digitChosen)
  numberList = numberList[:randomIndexChosen] + numberList[randomIndexChosen+1:]
  
print("""
      Welcome to the 4 digits game! 
      You have to guess a 4 digit number where each digit is unique.
      After you have entered all 4 digits to guess , if I tell you: 
      
      eg. 
      1A = 1 digit exists in the answer and is in the right position
      1B = 1 digit exists in the answer but not in the right position
      1A 1B = 2 digits exists in the answer but only 1 is in the right position
      2A 2B = All digits exists in the answer but only 2 are in the right position

      Hope you understand the rules, best of luck!
      
      Find the 4 digits: 
      _ _ _ _
      
      """)

totalTries = 0
notSolved = True

# print(fourDigitsActual)

def check(fourDigitsAnswer,fourDigitsActual):
  A = 0
  B = 0
  response = {"correct":False,
              "output":""}
  # Add up B to check counts of existance
  for i in range(4):
    currentAnswerDigit = fourDigitsAnswer[i]
    if currentAnswerDigit in fourDigitsActual:
      B += 1
  # Check for A for each digit , minus off from B and add to A if digit position correct
  for i in range(4):
    if fourDigitsAnswer[i] == fourDigitsActual[i]:
      A += 1
      B -= 1
  
  if A == 4 and B == 0:
    response["correct"] = True
    
  response["output"] = f"{str(A)}A & {str(B)}B"
  
  return response
  
def getFourDigitsAnswer():
  while (True):
    fourDigitInput = input("Enter a four digit number where each digit is unique: ")
    if len(fourDigitInput) != 4:
      print("Re-enter four digit number where each digit is unique again...")
    else:
      return [x for x in str(fourDigitInput)]
  
while(notSolved):
  if totalTries > 1:
    print("Try again!")
  totalTries += 1
  
  fourDigitsAnswer = getFourDigitsAnswer()
  
  response = check(fourDigitsAnswer,fourDigitsActual)
  
  if response["correct"] == True:
    notSolved = False
  
  print(response["output"])
  

print(f"""
      Congrats! You have solved the four digits!
      Number of tries = {totalTries}
      """)
  
  


  

  
