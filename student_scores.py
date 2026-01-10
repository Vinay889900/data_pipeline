import matplotlib.pyplot as plt
import random

def fetch_student_data():
    """
    Simulates fetching data from an API.
    Returns a list of dictionaries with 'name' and 'score'.
    """
    # Mock data
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "Diana", "score": 88},
        {"name": "Evan", "score": 76},
        {"name": "Fiona", "score": 95},
        {"name": "George", "score": 81},
        {"name": "Hannah", "score": 89}
    ]
    return students

def calculate_average(data):
    if not data:
        return 0
    total_score = sum(student['score'] for student in data)
    return total_score / len(data)

def create_bar_chart(data, avg_score):
    names = [student['name'] for student in data]
    scores = [student['score'] for student in data]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, scores, color='skyblue')
    
    # Add a line for the average
    plt.axhline(y=avg_score, color='r', linestyle='--', label=f'Average Score: {avg_score:.2f}')
    
    plt.xlabel('Students')
    plt.ylabel('Scores')
    plt.title('Student Test Scores')
    plt.legend()
    plt.ylim(0, 100)
    
    # Add values on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height}',
                 ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('scores_chart.png')
    print("Chart saved as 'scores_chart.png'")

def main():
    print("Fetching student data...")
    data = fetch_student_data()
    
    avg_score = calculate_average(data)
    print(f"Average Score: {avg_score:.2f}")
    
    print("Generating chart...")
    create_bar_chart(data, avg_score)

if __name__ == "__main__":
    main()
