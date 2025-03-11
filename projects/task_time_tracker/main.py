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
    task_name = input("Enter the task name (or type 'quit' to stop):")

    #If the user types "quit", exit the loop
    if task_name.lower() in ['quit', 'q']: 
        break
    
# Ask user for time spent of the task in minutes

# Calculate total time spent on task and store the time