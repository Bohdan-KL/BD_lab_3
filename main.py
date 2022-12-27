import psycopg2
import matplotlib.pyplot as plt

username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

query_1 = '''
SELECT white_id AS player_id, white_rating AS player_rating FROM white
UNION 
SELECT * FROM black
ORDER BY player_rating DESC
LIMIT 10; 
'''


query_2 = '''
SELECT victory_status, COUNT(victory_status) FROM game
GROUP BY victory_status;

'''

query_3 = '''
SELECT winner, COUNT(winner) FROM game
GROUP BY winner;

'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur1 = conn.cursor()
    cur1.execute(query_1)
    player_id = []
    player_rating = []

    for row in cur1:
        player_id.append(row[0])
        player_rating.append(row[1])

    cur2 = conn.cursor()
    cur2.execute(query_2)
    victory_status = []
    victory_status_amount = []

    for row in cur2:
        victory_status.append(row[0])
        victory_status_amount.append(row[1])

    cur3 = conn.cursor()
    cur3.execute(query_3)
    wins = []
    win_nature = []

    for row in cur3:
        wins.append(row[0])
        win_nature.append(row[1])


x_range = range(len(player_id))


bar = plt.bar(x_range, player_rating, width=0.5)
plt.title('Рейтинг гравців')
plt.xlabel('Гравці')
plt.xticks(x_range, player_id, rotation=90)
plt.ylabel('Рейтинг')
plt.bar_label(bar, label_type='center')

plt.show()


plt.pie(victory_status_amount, labels=victory_status, autopct='%1.1f%%')
plt.title('Частка причин закінчення гри')
plt.show()


x_range = range(len(wins))
plt.plot(x_range, win_nature, marker='o')
plt.xticks(x_range, wins)
plt.title('Загальний обсяг перемог білих, чорних або нічиїх')
plt.ylabel('Закінчення гри')
plt.xlabel('Причина')

for x,y in zip(x_range, win_nature):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,4.5), ha='center')

plt.tight_layout()
plt.show()
