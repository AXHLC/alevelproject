import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def plot_week_summary():
    # Connect to the database
    conn = sqlite3.connect('basketball_tracker.db')
    cursor = conn.cursor()

    # Retrieve data from the Results table
    cursor.execute('''
        SELECT date, skill_id, score
        FROM Results
        WHERE date BETWEEN date('now', '-7 days') AND date('now')
    ''')
    data = cursor.fetchall()
    conn.close()

    # Prepare data for plotting
    dates = sorted(set([row[0] for row in data]))
    skills = {1: 'Shooting', 2: 'Dribbling', 3: 'Passing'}

    # Initialize scores dictionary
    scores = {date: {'Shooting': 0, 'Dribbling': 0, 'Passing': 0} for date in dates}

    # Aggregate scores for each date and skill
    for date in dates:
        for skill_id, skill_name in skills.items():
            skill_scores = [row[2] for row in data if row[0] == date and row[1] == skill_id]
            if skill_scores:
                avg_score = sum(skill_scores) / len(skill_scores)
                scores[date][skill_name] = avg_score

    # Set up bar chart parameters
    x = np.arange(len(dates))
    width = 0.2

    fig, ax = plt.subplots()

    shooting_scores = [scores[date]['Shooting'] for date in dates]
    dribbling_scores = [scores[date]['Dribbling'] for date in dates]
    passing_scores = [scores[date]['Passing'] for date in dates]

    ax.bar(x - width, shooting_scores, width, label='Shooting')
    ax.bar(x, dribbling_scores, width, label='Dribbling')
    ax.bar(x + width, passing_scores, width, label='Passing')

    # Set chart labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Score')
    ax.set_title('Week Summary')
    ax.set_xticks(x)
    ax.set_xticklabels(dates)
    ax.set_ylim(0, 10)
    ax.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_week_summary()