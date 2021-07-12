import sqlite3
import binascii

# 特定トピックのメッセージのデータを一番最初のデータで上書きする。

dbname = 'rosbag2_2021_04_16-16_47_46_0.db3' # 上書きするrosbagのdb
conn = sqlite3.connect(dbname)

cur = conn.cursor()

# topic_id は

cur.execute('SELECT * FROM messages where topic_id=18 limit 1')
for row in cur:
    base_binary = row[3]
# print(base_binary[:100])

command = 'UPDATE messages SET data = x\'' + base_binary.hex() +'\' WHERE topic_id=18'
cur.execute(command)
conn.commit()
# print(command)

conn.close()
