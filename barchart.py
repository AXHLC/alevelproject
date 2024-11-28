import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def plot_week_summary(username: str):
    # Connect to the database
    conn = sqlite3.connect('basketball_tracker.db')
    cursor = conn.cursor()

    print("username:", username)

    # Retrieve user_id based on username
    cursor.execute('SELECT user_id FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()

    if not result:
        print("Username not found.")
        conn.close()
        return None  # Return None if user not found
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

    print("data:", data)

    if not data:
        print("No data available for this user in the past week.")
        return None  # Return None if no data

    # Prepare data for plotting
    dates = sorted(set([row[0] for row in data]))
    print("dates:", dates)
    skills = {"01": 'Shooting', "02": 'Dribbling', "03": 'Passing'}

    # Initialize scores dictionary
    scores = {date: {'Shooting': 0, 'Dribbling': 0, 'Passing': 0} for date in dates}

    # Fill in the scores from data
    for row in data:
        date = row[0]
        skill_id = row[1]
        score = row[2]
        skill_name = skills.get(skill_id)
        print("date:", date, "skill_id:", skill_id, "score:", score, "skill_name:", skill_name)
        if skill_name:
            scores[date][skill_name] = score

    # Set up bar chart parameters
    x = np.arange(len(dates))
    width = 0.25

    fig, ax = plt.subplots(figsize=(8, 4))

    shooting_scores = [scores[date]['Shooting'] for date in dates]
    dribbling_scores = [scores[date]['Dribbling'] for date in dates]
    passing_scores = [scores[date]['Passing'] for date in dates]

    print("Shooting scores:", shooting_scores)
    print("Dribbling scores:", dribbling_scores)
    print("Passing scores:", passing_scores)

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

    return plt.gcf()  # Return the figure object instead of showing it