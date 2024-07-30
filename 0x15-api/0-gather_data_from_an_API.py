#!/usr/bin/python3
"""
This script fetches and displays TODO list progress for a given employee ID from a REST API.
"""

import sys
import requests

def gather_data(employee_id):
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name", "Unknown")

    # Fetch todo data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print the result
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Print completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"     {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_data(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
