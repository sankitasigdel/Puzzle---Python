### write your code here

import numpy as np

#checking dosr
def checkDose (dose):
  #a= np.random.randint(0,1023)
  abin = np.binary_repr(dose,width = 10) 
  return abin

def sickMiceList(ratList):
  sickList = []
  binary = []
  for i,j in ratList:
    if int(j) == 1:
      sickList.append('''Mice {}'''.format(i))
  return sickList 

def checkMice (dose):
  check = list(dose)   
  finalList = [] 
  for c in enumerate(check,start=1 ):
    finalList.append(c)
  return sickMiceList(finalList)

def getMice ():
  print("Lets check status of Mice.")
  print("Enter - '0' for Good Condition ")
  print("Enter - '1' for Bad Condition ")
  print("....")
  rats = {}
  for i in range(1,11):
    rats.update({"Mice {}".format(i):int(input("Enter status of Mice {} (0 or 1)".format(i)))})
  return rats

def getDose(rats):
  a = ''
  affected_mice =''
  for key,value in rats.items():
    a = a + str(value)
    if value == 1 : 
      affected_mice = affected_mice + ', ' + str(key)
  dec = int(a,2)
  return dec,affected_mice[1:]

print("Welcome to Faulty Dose Checker!")
print("....")
print("....")
print("Mice are numbered from 1 to 10. ")
print("Doses are numbered from 1 to 1000. ")
print("You will be giving doses based on 10 digit binary number of the doses.")

while True :
  print("Press 1 - To get list of affected mice for a given dose number. ")
  print("Press 2 - To know faulty dose for combination of affected mices. ")
  print("Press any number - To end this program. ")
  check_operation = input("Enter 1, 2 or any other number ")

  if check_operation.strip() == '1':
    while True :
      input_dose = int(input("Enter a dose number "))
      if input_dose >1000 or input_dose < 1: 
        print("Your value is more than 1000 or less than 1 . Try again with new number! ")
      else : 
        break
    print("Getting Value....")
    print("....")
    check_dose = checkDose(input_dose)
    ratList = checkMice(check_dose)
    print ("For Dose {} , List of Mice - {} affected. ". format(input_dose,ratList))
    print("....")
    print("....")
  elif check_operation.strip() == '2' :
    miceData = getMice()
    doseData = getDose(miceData)
    if doseData[0] > 1000 :
      print("....")
      print("....")
      print ("Dose value must be between 1 and 1000. ")
      print("Your dose value was {} ".format(doseData[0]))
      print ("Not in range..Try again!!")
      print("....")
      print("....")
    else : 
      print("....")
      print("....")
      print ("For {} - mices affected, {} dose is faulty. ". format(doseData[1],doseData[0]))
      print("....")
      print("....")
  else :
    print("Did not choose a correct value..EXITING!!")
    break