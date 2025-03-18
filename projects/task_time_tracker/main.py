''' 
The program will:
1. Ask the user to enter a task name 
2. Ask how many minutes they spent on it 
3. Keep a running total of all time spent 
4. Allow the user to see their most time-consuming task  
5. Quit when the user is done 
6. This exercise builds on the concepts covered in class, applying them to a real-world scenario that could help with personal productivity or workplace time management.
'''

# Create variables to (1)store time spent on a task and the most consuming task
total_time = 0       #total time spent on tasks
max_time_task = ""   #name of the most time-consuming task
most_time_spent = 0  #time spent on the most consuming task

# Start task tracking and ask user for the task name
while True:
    task_name = input("Enter task name (or type 'quit' to stop):")

    if task_name.lower() == 'quit':
        #If user types "quit", break out of the loop and stop program
        break

# Ask user for time spent of the task in minutes
    try: 
        time_spent = int(input(f'How many minutes did you spend on "{task_name}"?'))
    except ValueError: 
        # If the user enters a non-numeric value, display an error message and prompt
        print("Please enter a valid number for the number of minutes")
        continue
# Calculate total time spent (total_time) on task and store the time
    total_time += time_spent

# Check if the current task is the most time-consuming task
if time_spent > most_time_spent: 
    most_time_spent = time_spent
    max_time_task = task_name

# Display current total time spent on task and the most time-consuming task 
print(f'Total time spent on task: {total_time} minutes')
print(f'Your most time-consuming task: {max_time_task} with {most_time_spent} minutes')