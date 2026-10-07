from tasks import tasks

name = input("what is your name? ")
print("Welcome " + name)
while True:
    user_tasks = input("put a task: ")
    tasks.append(user_tasks)
    print(f"your tasks are {tasks}")