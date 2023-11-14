from collections import defaultdict


def grade_participation(chat_logs):
    # Create a dictionary to store the participation count for each student
    participation_count = defaultdict(int)

    # Iterate through each chat entry
    for entry in chat_logs:
        student = entry['student']  # Assuming each chat entry has a 'student' field
        participation_count[student] += 1

    # Display the participation count for each student
    for student, count in participation_count.items():
        print(f"{student} participated {count} times.")


# Example usage
chat_logs = [
    {'student': 'Alice', 'message': '...'},
    {'student': 'Bob', 'message': '...'},
    {'student': 'Alice', 'message': '...'},
    # ... more chat entries
]

grade_participation(chat_logs)
