# rosbag2_edit_sample


rosbag2 のレコードをpython のスクリプトから編集するサンプルです。  
特定のトピックのメッセージ内容を、すべて一番最初のメッセージ内容に変更します。

dbのtimestampはメッセージを受け取った時刻であり、header.stampとは異なるので注意。


```
sqlite> .tables
messages  topics


sqlite > select * from topics
1|/vehicle/status/twist|geometry_msgs/msg/TwistStamped|cdr|
...
2~23 topic info
...
24|/sensing/gnss/fixed|autoware_debug_msgs/msg/BoolStamped|cdr|- history: 1
  depth: 1
  reliability: 1
  durability: 2
  deadline:
    sec: 9223372036
    nsec: 854775807
  lifespan:
    sec: 9223372036
    nsec: 854775807
  liveliness: 1
  liveliness_lease_duration:
    sec: 9223372036
    nsec: 854775807
  avoid_ros_namespace_conventions: false



sqlite> .schema messages
CREATE TABLE messages(id INTEGER PRIMARY KEY,topic_id INTEGER NOT NULL,timestamp INTEGER NOT NULL, data BLOB NOT NULL);
CREATE INDEX timestamp_idx ON messages (timestamp ASC);


> unify 前
sqlite> select * from messages where topic_id=18 limit 10;
93|18|1618559266855522762|@1
252|18|1618559266955105215|@2
411|18|1618559267055079535|@3
569|18|1618559267155279695|@4
729|18|1618559267254905301|@5
880|18|1618559267354337859|@6
1040|18|1618559267454647297|@7
1200|18|1618559267557422604|@8
1358|18|1618559267655768034|@9
1519|18|1618559267757423073|@10

※　@ はバイナリ文字列

> unify 後

sqlite> select * from messages where topic_id=18 limit 10;
93|18|1618559266855522762|@1
252|18|1618559266955105215|@1
411|18|1618559267055079535|@1
569|18|1618559267155279695|@1
729|18|1618559267254905301|@1
880|18|1618559267354337859|@1
1040|18|1618559267454647297|@1
1200|18|1618559267557422604|@1
1358|18|1618559267655768034|@1
1519|18|1618559267757423073|@1
```
