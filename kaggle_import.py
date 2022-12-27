import pandas as pd
import psycopg2

username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'



data = pd.read_csv(r'C:\Users\Windows\Desktop\Bigdon_lab3\games.csv')

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

df = pd.DataFrame(data, columns=['black_id', 'black_rating'])

black_id = df['black_id']
black_rating = df['black_rating']

for i, item in df.iteritems():
    unique_clubs = item.unique()



cur1 = conn.cursor()

for i in range(len(black_id)):
    query1 = """ 
    INSERT INTO black(black_id, black_rating) VALUES (('%s'), ('%s')) 
    ON CONFLICT (black_id)
    DO NOTHING;
    """ % (black_id[i], black_rating[i])
    cur1.execute(query1)



cur2 = conn.cursor()

df = pd.DataFrame(data, columns=['white_id', 'white_rating'])
white_id = df['white_id']
white_rating = df['white_rating']

for i in range(len(white_id)):
    query2 = """
    INSERT INTO white(white_id, white_rating) VALUES (('%s'), ('%s')) 
    ON CONFLICT (white_id)
    DO NOTHING;
    """ % (white_id[i], white_rating[i])
    cur2.execute(query2)

conn.commit()

cur3 = conn.cursor()

df = pd.DataFrame(data, columns=['id', 'winner', 'turns', 'victory_status'])

game_id = df['id']
winner = df['winner']
turns = df['turns']
victory_status = df['victory_status']

for i in range(len(black_id)):
    query3 = """
    INSERT INTO game(game_id, white_player_id,black_player_id, winner, turns, victory_status) VALUES (('%s'), ('%s'), ('%s'), ('%s'),('%s'), ('%s'));
    """ % (game_id[i] + str(i), white_id[i], black_id[i], winner[i], turns[i], victory_status[i])
    cur3.execute(query3)

conn.commit()

