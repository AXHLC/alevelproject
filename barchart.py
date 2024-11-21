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
    # sort the data here########################################################################

    # Initialize scores dictionary
    scores = {}

    print("HEllo")
    for datum in data: print(datum) 
    print("bye")

    for datum in data:

        if not scores.get(datum[resultsIndex["date"]]):
            scores[datum[resultsIndex["date"]]] = {
                'Shooting': 0,
                'Dribbling': 0,
                'Passing': 0,
            }

        print(datum[resultsIndex["skill_id"]], datum[resultsIndex["score"]])

        if datum[resultsIndex["skill_id"]] == "01":
            scores[datum[resultsIndex["date"]]]["Shooting"] = datum[resultsIndex["score"]]

        elif datum[resultsIndex["skill_id"]] == "02":
            scores[datum[resultsIndex["date"]]]["Dribbling"] = datum[resultsIndex["score"]]
        
        elif datum[resultsIndex["skill_id"]] == "03":
            scores[datum[resultsIndex["date"]]]["Passing"] = datum[resultsIndex["score"]]



    print("printing scores:\n", scores)

############################################################################################


    # Set up bar chart parameters
    x = np.arange(len(data))
    width = 0.25

    fig, ax = plt.subplots()

    shooting_scores = [scores[datum]['Shooting'] for datum in data]
    dribbling_scores = [scores[datum]['Dribbling'] for datum in data]
    passing_scores = [scores[datum]['Passing'] for datum in data]

    ax.bar(x - width, shooting_scores, width, label='Shooting')
    ax.bar(x, dribbling_scores, width, label='Dribbling')
    ax.bar(x + width, passing_scores, width, label='Passing')

    # Set chart labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Score (0-10)')
    ax.set_title(f'Week Summary for {username}')
    ax.set_xticks(x)
    ax.set_xticklabels(data)
    ax.set_ylim(0, 10)
    ax.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    username = input("Enter the username: ")
    plot_week_summary(username)