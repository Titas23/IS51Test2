"""

We will write a program that will calculate student grades on their final exam. 
I will display the number of grades and also the average grade. 
We will read in a Final.txt file where the grades are located.

Also include the percentange of grades with an above avergae score. 
display to the use the grades that are above average. 

We will begin with a main() function to start the program. 


"""

"""

main()
    infile = open Final.txt
    grades = line.rstrip()
    infile.close()
    for i in range(len(grades)):

calculate_percent_above_average():
    average = sum grades/ len
    num = 0 
    for grade in grades:
        if grade > average: 
            num += 1
print(Number of grades )
print(Average Grade )
print(Percentange of grades above average )

main()


"""



def calculate_percent_above_average(grades, average):
    count = 0
    for grade in grades:
        if grade > average:
            count += 1
    return (count * 100) / len(grades)


def main():
    file = open('Final.txt')
    grades = []
    for line in file:
        grades.append(int(line.strip()))
    print("Number of grades:", len(grades))
    average = 0
    for grade in grades:
        average += grade
    average /= len(grades)
    print("Average grade:", average)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades, average)))
    file.close()


main()
