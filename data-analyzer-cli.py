#Data Analyzer CLI
import statistics
data = []

def has_data(data):
    if len(data) == 0:
        print("No data available")
        return False
    else:
        return True

while True:
    print("\n--- DATA ANALYZER ---")
    print("1\n--- add number ---")
    print("2\n--- SHOW DATA ---")
    print("3\n--- ANALYSIS ---")
    print("4\n--- SORT DATA ---")
    print("5\n--- EXIT")

    choice = input("Enter your choice: ")

    #insert data
    if choice == "1":
        number = int(input("Enter a number: "))
        data.append(number)
        print("Added:",number)


    #show data
    elif choice == "2":
        print(data)

    #analysis-min, max, average, even, odd, greater/smaller than, sort
    elif choice == "3":
        if not has_data(data):
            print("No data available")
            continue

        #min,max,average, lenght
        print(min(data))
        print(max(data))
        print(sum(data))
        print(len(data))
        average = statistics.mean(data)
        print(average)

        #greater, smaller, equal, even, odd
        even_count = 0
        odd_count = 0
        greater_count = 0
        smaller_count = 0
        equal_count = 0

        for number in data:
            if number % 2 == 0:
                even_count += 1
        else:
            odd_count += 1

            x = int(input("Enter a number to check if your data is greater or smaller: "))
            for number in data:
                if number > x:
                    greater_count += 1
                elif number < x:
                    smaller_count += 1
            else:
                equal_count += 1



            print("\n---ANALYSIS---")
            print("Even: ",even_count)
            print("Odd: ",odd_count)
            print("Smaller: ",smaller_count)
            print("Greater: ", greater_count)
            print("Equal: ", equal_count)

        #sort data
    elif choice == "4":
        if not has_data(data):
            print("No data available")
            continue

        sorted_data = sorted(data)
        order = input("Ascending or descending? (a/d): ")
        if order == "a":
            print("sorted data:", sorted(data))
        elif order == "d":
            print("sorted data", sorted(data), reverse = True)
        else:
            print("Invalid choice")


    #exit
    elif choice == "5":
        break

    #invalid choice
    else:
        print("Invalid choice")
