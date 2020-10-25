import numpy as np
import numpy.linalg as la
import random
import math


def main():
    print("Enter in the following inputs and see how many people are infected or die in the simulation. \nWarning: Large inputs may cause the program to quit due to time inefficiencies. In this case, refresh the page.\n")
    not_int = True
    while not_int:
        size_pop = input("Enter size of population: ")
        try:
            size_pop = int(size_pop)
            size_pop = abs(size_pop)
            not_int = False
        except ValueError:
            print("This is not an integer number! Please enter a valid number.")
    # End of while loop
    not_int = True
    while not_int:
        connection = input("Enter chance of connection between people: ")
        try:
            connection = int(connection)
            connection = abs(connection)
            if (connection <= -1) or (connection >= 101):
                print("Chance of connection must be between 0 and 100! Please enter a valid number.")
                not_int = True
            else:
                not_int = False
        except ValueError:
            print("This is not an integer number! Please enter a valid number.")
    # end while loop
    not_int = True
    while not_int:
        inf_pop = input("Enter size of initial infected population: ")
        try:
            inf_pop = int(inf_pop)
            inf_pop = abs(inf_pop)
            if inf_pop > size_pop:
                print(
                    "Infected population can not be greater than total population! Please enter a valid number.")
                not_int = True
            else:
                not_int = False
        except ValueError:
            print("This is not an integer number! Please enter a valid number.")
    # end while loop
    not_int = True
    while not_int:
        inf_rate = input("Enter infection rate: ")
        try:
            inf_rate = int(inf_rate)
            inf_rate = abs(inf_rate)
            if (inf_rate <= -1) or (inf_rate >= 101):
                print("Infection rate must be between 0 and 100! Please enter a valid number.")
                not_int = True
            else:
                not_int = False
        except ValueError:
            print("This is not an integer number! Please enter a valid number.")
    # end while loop
    not_int = True
    while not_int:
        rounds = input("Enter rounds of infection spread: ")
        try:
            rounds = int(rounds)
            rounds = abs(rounds)
            if (rounds <= -1):
                print("Rounds must be greater than 0! Please enter a valid number.")
                not_int = True
            else:
                not_int = False
        except ValueError:
            print("This is not an integer number! Please enter a valid number.")
    # end while loop
    not_int = True
    while not_int:
        dead_per = input("Enter mortality rate: ")
        try:
            dead_per = int(dead_per)
            dead_per = abs(dead_per)
            if (dead_per <= -1) or (dead_per >= 101):
                print(
                    "Mortality rate must be between 0 and 100! Please enter a valid number.")
                not_int = True
            else:
                not_int = False
        except ValueError:
            print("This is not an integer number! Please enter a valid number.")
    # end while loop
    AbbyMatrix = generate_array(size_pop, connection)
    # create the array of infected people's indexs
    whomst = random.sample(range(0, size_pop), inf_pop)

    # print initial infection
    print("Initially Infected:",inf_pop)

    # iterate over the number of rounds the user 
    # wishes to spread with
    for x in range(0,rounds):

        # make the new list to collect the newly infected
        # individuals
        new_whomst = []

        # iterate over every infected person's index ---------------
        for t in range(0,len(whomst)):
    
            # get the infected person's index at index t
            who = whomst[t]

            # get the size of AbbyMatrix
            n = AbbyMatrix.shape[0]

            # for every index in the matrix of people's 
            # connections (AbbyMatrix)
            for i in range(0,n):

                # if the index is not in whomst
                if (i not in whomst and i not in new_whomst):

                    # get the item in the matrix at the row
                    # of the infected person
                    oh = AbbyMatrix[who][i]

                    # if there is a connection between the
                    # infected individual and the given 
                    # column index
                    if (oh == 1):
                        # generate a random number and...
                        are_inf = random.randint(1,100)
                        # ... use that in connection to the rate 
                        # of infection to determine if individual
                        # 'oh' gets infected

                        if(are_inf <= inf_rate):
                            # add the newly infected individual's index 
                            # to the list of this round's infected 
                            # individuals
                            new_whomst.append(i)

                            # add this individual to the count of infected
                            inf_pop += 1
        # ----------------------------------------------------------

        # sort the list of originally infected individuals in reverse
        whomst.sort(reverse=True)

        # iterating over every item in whomst from the largest
        # to the smallest (thanks to sort)
        for d in range(0,len(whomst)):
            # delete that row from AbbyMatrix
            AbbyMatrix = np.delete(AbbyMatrix, whomst[d], axis=0)
            
            # initialize the new matrix. this is created in order to
            # reinitalize the matrix when removing the old infected 
            # individuals from the system
            NewMatrix = []

        # for every row in the AbbyMatrix (with the infected Rows
        # already removed) 
        for row in AbbyMatrix:
            # initialize a empty row to add
            new_row = []

            # for every index/column index for the row in AbbyMatrix
            for col in range(0,len(row)):
                # if the column is not the index of a previously infected
                # individual
                if (col not in whomst):
                    # append the value in that row to the new row
                    new_row.append(row[col])
        
            # add that row into the NewMatrix
            NewMatrix.append(new_row)
        
        # Set the AbbyMatrix to the NewMatrix as a numpy array
        AbbyMatrix = np.array(NewMatrix)

        # if the newly infected individuals were at any indexs after the
        # old index this adjustes it accordingly
        for h in range(0,len(new_whomst)):
            for w in range(0,len(whomst)):
                if (new_whomst[h] >= whomst[w]):
                    new_whomst[h] = new_whomst[h] - 1

        # set the list of infected individual indexes to the newly
        # infected individuals
        whomst = new_whomst

        # print round results
        print("People Infected in Round ",x+1,": ",len(new_whomst),sep="")
    
    Num_dead = math.floor(inf_pop * dead_per / 100)

    # Infected people
    print("\nTotal Infected:", inf_pop)
    for i in range(1, math.floor(inf_pop/5)+1):
        print(" o  "*5)
        print("<|> "*5)
        print("/ \\ "*5)
    temp = (inf_pop) % 5
    if temp > 0:
        print(" o  "*temp)
        print("<|> "*temp)
        print("/ \\ "*temp)
    # Dead people
    print("\nTotal From Infected That Will Die:", Num_dead)
    for i in range(1, math.floor(Num_dead/5)+1):
        print(" x  "*5)
        print("<|> "*5)
        print("/ \\ "*5)
    temp = (Num_dead)%5
    if temp > 0:
        print(" x  "*temp)
        print("<|> "*temp)
        print("/ \\ "*temp)



def generate_array(pop, connection):
  final = []

  first = np.random.randint(1, 100, size=pop)
  for p in range(0, len(first)):
    first[p] = make_connect(first[p], connection)
  final.append(first)

  for i in range(1, pop):
    next_row = np.random.randint(1, 100, size=pop)
    for x in range(0, pop):
      if (x < i):
        next_row[x] = final[x][i]
      elif (x == i):
        next_row[i] = 0
      else:
        next_row[x] = make_connect(next_row[x], connection)

    final.append(next_row)

  return np.array(final)


def make_connect(x, connect):
  if (x <= connect):
    return 1
  else:
    return 0


def clean_matrix(AbbyMatrix):
    # An integer showing the number of rows in the Abby Matrix
    shape = AbbyMatrix.shape[0]
    # creates a matrix that connects each node to itself
    ConnectedAbbyMatrix = la.matrix_power(AbbyMatrix, shape-1)
    # takes the same matrix but only cares about whether the number is greater than 0
    SimplifiedConnectedAbbyMatrix = (ConnectedAbbyMatrix > 0).astype(int)
    UniqueAbbyMatrix = np.unique(SimplifiedConnectedAbbyMatrix, axis=0)  # finds unique groups
    return UniqueAbbyMatrix  # returns the matrix containing the unique groups

main()