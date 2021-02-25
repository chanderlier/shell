###install
```sh
$ scp root@10.0.10.168:/root/kafka_2.13-2.7.0.tgz .
$ tar -xzf kafka_2.13-2.7.0.tgz
$ mv kafka_2.13-2.7.0 /alidata/server/kafka
```
使用jdk12
```sh
vim /etc/profile
```
添加下面内容
```sh
export JAVA_HOME=/alidata/server/jdk
export PATH=$JAVA_HOME/bin:$PATH
```
确认
```sh
java -version
```
###systemd
```sh
vim /usr/lib/systemd/system/zookeeper.service 
```
```sh
[Unit]
Description=Apache Zookeeper server
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target

 

[Service]
Type=simple
ExecStart=/alidata/server/kafka/bin/zookeeper-server-start.sh /alidata/server/kafka/config/zookeeper.properties
ExecStop=/alidata/server/kafka/bin/zookeeper-server-stop.sh
Restart=on-failure

 

[Install]
WantedBy=multi-user.target

```
```sh
$ systemctl enable zookeeper
$ systemctl start zookeeper
```
```sh
vim /usr/lib/systemd/system/kafka.service
```

```sh
[Unit]
Description=Apache Kafka server (broker)
Documentation=http://kafka.apache.org/documentation.html
Requires=zookeeper.service

 

[Service]
Type=simple
ExecStart=/alidata/server/kafka/bin/kafka-server-start.sh /alidata/server/kafka/config/server.properties
ExecStop=/alidata/server/kafka/bin/kafka-server-stop.sh
Restart=on-failure

 

[Install]
WantedBy=multi-user.target
```

```sh
cd /alidata/server/kafka
```
```sh
bin/kafka-server-start.sh config/server.properties
```
create topic
```sh
bin/kafka-topics.sh --create --topic test-events --bootstrap-server localhost:9092
```
describe topic
another terminal
```sh
bin/kafka-topics.sh --describe --topic test-events --bootstrap-server localhost:9092
```
write some events into the topic
another terminal
```sh
bin/kafka-console-producer.sh --topic test-events --bootstrap-server localhost:9092
```
read the events
another terminal
```sh
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

bin/kafka-acls.sh --authorizer kafka.security.auth.SimpleAclAuthorizer \
--authorizer-properties zookeeper.connect=localhost:2181 --add \
--allow-principal User:producer --operation Read --group test-group --allow-host 10.0.*.*


bin/kafka-acls.sh --authorizer kafka.security.auth.SimpleAclAuthorizer \
--authorizer-properties zookeeper.connect=localhost:2181 --list




$ bin/kafka-configs.sh --zookeeper localhost:2181 --alter --add-config 'SCRAM-SHA-256=[password=writer],SCRAM-SHA-512=[password=writer]' --entity-type users --entity-name writer
Completed Updating config for entity: user-principal 'writer'.


$ bin/kafka-configs.sh --zookeeper localhost:2181 --alter --add-config 'SCRAM-SHA-256=[password=reader],SCRAM-SHA-512=[password=reader]' --entity-type users --entity-name reader
Completed Updating config for entity: user-principal 'reader'.


$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test  --producer.config config/producer.conf
>hello, world



$KAFKA_OPTS=-Djava.security.auth.login.config=/alidata/server/kafka/config/kafka-broker.jaas bin/kafka-server-start.sh config/server.properties
......
[2019-07-02 13:30:34,822] INFO Kafka commitId: fc1aaa116b661c8a (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-02 13:30:34,822] INFO Kafka startTimeMs: 1562045434820 (org.apache.kafka.common.utils.AppInfoParser)
[2019-07-02 13:30:34,823] INFO [KafkaServer id=0] started (kafka.server.KafkaServer)