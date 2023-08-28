# imports
import numpy as np
import mplcursors
import matplotlib.pyplot as plt

# global variables
steps = 0
evenCount = 0
oddCount = 0

# Collatz Class
class Collatz:

    # Main loop
    @staticmethod
    def main(num):
        global evenCount, oddCount
        sequence = [num]

        while num != 1: 
            if(num % 2) == 0: 
                num = num // 2
                evenCount += 1
            else: 
                num = num * 3 + 1
                oddCount += 1
            sequence.append(num)
        return sequence
        
    # Information results
    @staticmethod
    def resultsText(sequence):
        steps = oddCount + evenCount
        for num in sequence:
            if(num % 2 ==0):
                print("\n{0} Number is even.".format(num))
            else:
                print("\n{0} Number is odd.".format(num))

        print("\nNumber of steps taken: {0}".format(steps))
        print("Number of even numbers {0}".format(evenCount))
        print("Number of odd numbers {0}".format(oddCount))

    @staticmethod
    def resultsGraphical(sequences):
        
        for i, sequence in enumerate(sequences):
            x = list(range(len(sequence)))
            y = sequence
            plt.plot(x,y, label=f"Sequence {i+1}")
            plt.draw()
            plt.pause(0.1)

        plt.title("Collatz Conjecture Sequence")
        plt.xlabel("Step")
        plt.ylabel("Number")
        plt.grid(True)
        

        if len(sequences) <= 5:
            plt.legend()

        cursor = mplcursors.cursor(hover=True)

        @cursor.connect("add")
        def on_add(sel):
            x_int = int(sel.target[0])
            y_int = int(sel.target[1])
            sel.annotation.set_text(f"Step: {x_int}, Number: {y_int}")

        plt.show()


    # Initalise the global variables
    @staticmethod
    def userInput():
        print("Collatz Conjecture Numbers\n")
        print("1) Single number\n2) Range of numbers") 
        choice = int(input("please choose an option: "))

        if choice == 1: 
            num = int(input("Please enter a number: "))
            sequence = Collatz.main(num)
            Collatz.displayResults([sequence])

        elif choice == 2: 
            start = int(input("Please enter the start of the range: "))
            end = int(input("Please enter the end of the range: "))
            sequence_list = []
            for num in range(start, end + 1):
                sequence_list.append(Collatz.main(num))
            Collatz.displayResults(sequence_list)

        else: 
            Collatz.userInput()     

    @staticmethod
    def rangeMain(start, end): 
        for num in range(start, end + 1):
            Collatz.displayResults(Collatz.main(num))

    # Allows the user to choose a way to visualise their data
    @staticmethod
    def displayResults(sequences):
        print("Please choose a view for you results. ")
        print("1) Text results \n2) Graphical results")
        choice = int(input("Please choose an option: "))
        if(choice == 1):
            for sequence in sequences: 
                Collatz.resultsText(sequence)  
        elif(choice == 2):
            Collatz.resultsGraphical(sequences)   
        else:
            Collatz.displayResults(sequence)

# First call
Collatz.userInput()