
1、查日志
# cd /var/log/gitlab/gitlab-rails/
# grep 'Rack_Attack' production.log|more
Rack_Attack: blacklist 192.130.160.212 GET /xxx
Rack_Attack: blacklist 192.130.160.212 GET /xxxxxx
Rack_Attack: blacklist 192.130.160.212 GET /xxxxxxxx
确认这个ip是否是访问者的ip
2、进入redis：
# /opt/gitlab/embedded/bin/redis-cli -s /var/opt/gitlab/redis/redis.socket
redis /var/opt/gitlab/redis/redis.socket> keys *rack::attack*
1) "cache:gitlab:rack::attack:26176509:allow2ban:count:192.130.160.212"
2) "cache:gitlab:rack::attack:allow2ban:ban:192.130.160.212"

通过两步即可确认，就是这个原因。在redis里清除该条即可：
del cache:gitlab:rack::attack:allow2ban:ban:192.130.160.212

