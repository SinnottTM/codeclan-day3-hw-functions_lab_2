tasks = [
    {"description": "Wash Dishes", "completed": False, "time_taken": 10},
    {"description": "Clean Windows", "completed": False, "time_taken": 15},
    {"description": "Make Dinner", "completed": True, "time_taken": 30},
    {"description": "Feed Cat", "completed": False, "time_taken": 5},
    {"description": "Walk Dog", "completed": True, "time_taken": 60},
]

# MVP
# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks


def uncompleted_tasks(tasks):
    results_uncompleted_tasks = []
    for task in tasks:
        if task["completed"] == False:
            results_uncompleted_tasks.append(task["description"])
    return results_uncompleted_tasks


# Print a list of completed tasks
def completed_tasks(tasks):
    results_completed_tasks = []
    for task in tasks:
        if task["completed"] == True:
            results_completed_tasks.append(task["description"])
    return results_completed_tasks

# Print a list of all task descriptions


def task_descriptions(tasks):
    results_task_descriptions = []
    for task in tasks:
        if task["description"] != None:
            results_task_descriptions.append(task["description"])
    return results_task_descriptions

# Print a list of tasks where time_taken is at least a given time


def task_with_time(tasks, time):
    results_task_with_times = []
    for task in tasks:
        if task["time_taken"] >= time:
            results_task_with_times.append(task["description"])
    return results_task_with_times

# Print any task with a given description


def task_with_description(tasks, description):
    results_task_with_description = []
    for task in tasks:
        if task["description"] == description:
            results_task_with_description = task
    return results_task_with_description

# Extension

# Given a description update that marks task it as complete.


def task_checklist(tasks, description):
    completed_tasks = []
    for task in tasks:
        if task["description"] == description:
            task["completed"] = True
            completed_tasks.append(tasks["completed"] == True)
    return completed_tasks

# Add a task to the list


def add_task(task_name, boolean, task_time):
    tasks.append(
        {"description": task_name, "completed": True or False, "time_taken": task_time})
    return tasks
# EXAMPLE TEST - print(add_task("bed", True, 30))

# Further Extensions

# Use a while loop to display the following menu and allow the use to enter an option.
# Call the appropriate function depending on the users choice.

#  Note: list_of_user_options just information, no interactivity = no parameters needed


def list_of_user_options():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")


# Set flag. Note, flags seem to make iteration much easier in loops
is_menu_in_use = True

# By setting this to True, this while loop will only end when a user command is linked to changing that option to false
while is_menu_in_use == True:

    # seek input to allow for navigation
    user_input = input(
        "Please select an option, if unsure please press M/m for menu to see full range of options: ")

    #  see all tasks
    if user_input == "1":
        print(tasks)

    # check all tasks that are not completed
    if user_input == "2":
        print(uncompleted_tasks(tasks))

    # check all tasks that are completed
    if user_input == "3":
        print(completed_tasks(tasks))

    # check if specific task complete. Note: Initial attempt with security, couldn't get to work
    # if user_input == "4":
    #     got_task_yet = False
    #     while got_task_yet == False:
    #         task_checklist_complete = task_checklist(tasks, input("Please select a task description: "))
    #         if task_checklist_complete in tasks:
    #             print(task_checklist(tasks, task_checklist_complete))
    #             got_task_yet = True
    #         else:
    #             task_checklist_complete = input("Incorect data-entry. Please select a task: ")

    # Get task time
    if user_input == "5":
        got_time_yet = False
        while got_time_yet == False:
            task_length = float(input("Type a time in minutes only: "))
            if task_length != None:
                print(task_with_time(tasks, task_length))
                got_time_yet = True
            else:
                task_length = float(input("Incorect data-entry. Type a time: "))

    # Get task name, return description. Note: Initial attempt with security, couldn't get to work

    # if user_input == "4":
    #     got_task_name_yet = False
    #     while got_task_name_yet == False:
    #         user_task_input = input("Enter a task name for details: ")
    #         if user_task_input in tasks:
    #             print(task_with_description(tasks, user_task_input))
    #             got_task_name_yet = True
    #         else:
    #             user_task_input = input("Incorrect data-entry. Enter a task name for details: ")

    #  Enters new task, interesting as has to take boolean
    if user_input == "7":
        task_name = input("Enter new task name: ")
        got_boolean_yet = False
        while got_boolean_yet == False:
            boolean = input("New Task completed? Please enter True/False?: ")
            if boolean.lower() == "true":
                boolean = True
                got_boolean_yet = True
            elif boolean.lower() == "false":
                boolean = False
                got_boolean_yet = True
            else:
                boolean = input(
                    "Please try again. Task completed? Please enter true/false?: ")
        task_time = int(
            input("How long with this new task take in minutes only?: "))
        print(add_task(task_name, boolean, task_time))

    # Displays menu
    if user_input.lower() == "m":
        print(list_of_user_options())

    # Ends program by changing flag from True to False
    if user_input.lower() == "q":
        print("Goodbye")
        is_menu_in_use = False
