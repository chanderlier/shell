公司gitlab，突然有一天访问的时候显示403 forbidden，排查后确认问题是和gitlab的安全机制有关。需要在redis中删除一个key
1、查日志
# cd /var/log/gitlab/gitlab-rails/
# grep 'Rack_Attack' production.log|more
Rack_Attack: blacklist 132.123.33.22 GET /xxx
Rack_Attack: blacklist 132.123.33.22 GET /xxxxxx
Rack_Attack: blacklist 132.123.33.22 GET /xxxxxxxx
确认这个ip是否是访问者的ip
2、进入redis：
# /opt/gitlab/embedded/bin/redis-cli -s /var/opt/gitlab/redis/redis.socket
redis /var/opt/gitlab/redis/redis.socket> keys *rack::attack*
1) "cache:gitlab:rack::attack:26176509:allow2ban:count:132.123.33.22"
2) "cache:gitlab:rack::attack:allow2ban:ban:132.123.33.22"

通过两步即可确认，就是这个原因。在redis里清除该条即可：
del cache:gitlab:rack::attack:allow2ban:ban:132.123.33.22

