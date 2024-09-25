import sqlite3
import pandas as pd

df = pd.read_csv('LCK_2024_Season.csv')

conn = sqlite3.connect('LCK_2024_data.db')
cursor = conn.cursor()

df.to_sql('lck_stats', conn, if_exists='replace', index=False)

TopKilsQuery = """
SELECT DISTINCT
    a.playername, 
    a.teamname AS player_team, 
    a.champion,
    a.kills, 
    b.teamname AS opponent_team,
    a.date
FROM lck_stats a
JOIN lck_stats b
    ON a.gameid = b.gameid
    AND a.teamname != b.teamname
WHERE a.playername IS NOT NULL
ORDER BY a.kills DESC
LIMIT 10;
"""
TopChampPickRate = """
SELECT champion, COUNT(champion) AS pick_count 
FROM lck_stats 
GROUP BY champion 
ORDER BY pick_count DESC 
LIMIT 10;
"""

TopWardsPlaced = """
SELECT playername, SUM(wardsplaced) AS totalWardsPlaced
FROM lck_stats
WHERE playername IS NOT NULL
GROUP BY playername
ORDER BY totalWardsPlaced DESC
LIMIT 10;
"""

TopCsat10 = """
SELECT playername, AVG(totalgold)/AVG((kills + assists)/deaths) AS AvgKda, AVG((kills + assists)/deaths), AVG(totalgold)
FROM lck_stats
WHERE playername IS NOT NULL
GROUP BY playername
ORDER BY AvgKda DESC
LIMIT 10
"""

cursor.execute(TopChampPickRate)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()