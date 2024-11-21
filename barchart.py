import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def plot_week_summary(username: str) -> None:
    # Connect to the database
    conn = sqlite3.connect('basketball_tracker.db')
    cursor = conn.cursor()

    # Retrieve user_id based on username
    cursor.execute('SELECT user_id FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()

    if not result:
        print("Username not found.")
        conn.close()
        return
    user_id = result[0]

    # Retrieve data from the Results table for the specified user
    cursor.execute('''
        SELECT date, skill_id, score
        FROM Results
        WHERE user_id = ?
          AND date BETWEEN date('now', '-6 days') AND date('now')
    ''', (user_id,))
    data = cursor.fetchall()
    conn.close()

    resultsIndex = { "date": 0, "skill_id": 1, "score": 2 }

    if not data:
        print("No data available for this user in the past week.")
        return

    # Prepare data for plotting

    # Extract unique dates and sort them
    dates = sorted(set([row[resultsIndex["date"]] for row in data]))

    # Map skill IDs to skill names
    skills = {1: 'Shooting', 2: 'Dribbling', 3: 'Passing'}

    # Initialize scores dictionary with dates and zero-initialized skill scores
    scores = {date: {'Shooting': 0, 'Dribbling': 0, 'Passing': 0} for date in dates}

    # Fill in the scores from data
    for datum in data:
        date = datum[resultsIndex["date"]]
        skill_id = int(datum[resultsIndex["skill_id"]])
        score = float(datum[resultsIndex["score"]])

        # Get the skill name from the skills dictionary
        skill_name = skills.get(skill_id)
        if skill_name:
            scores[date][skill_name] = score

    print("Printing scores:\n", scores)

    # Plotting the data
    # Set up bar chart parameters
    x = np.arange(len(dates))
    width = 0.25

    fig, ax = plt.subplots()

    shooting_scores = [scores[date]['Shooting'] for date in dates]
    dribbling_scores = [scores[date]['Dribbling'] for date in dates]
    passing_scores = [scores[date]['Passing'] for date in dates]

    ax.bar(x - width, shooting_scores, width, label='Shooting')
    ax.bar(x, dribbling_scores, width, label='Dribbling')
    ax.bar(x + width, passing_scores, width, label='Passing')

    # Set chart labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Score (0-10)')
    ax.set_title(f'Week Summary for {username}')
    ax.set_xticks(x)
    ax.set_xticklabels(dates)
    ax.set_ylim(0, 10)
    ax.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    username = input("Enter the username: ")
    plot_week_summary(username)