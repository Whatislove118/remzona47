# install docker
iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
apt-get install iptables-persistent -y
docker pull registry
mkidr /var/lib/docker/registry-repo

# Auth # master L1TF99qv
apt-get install apache2-utils -y
mkdir /etc/docker/auth
htpasswd -Bbn username password > /etc/docker/auth/htpasswd
# https://stackoverflow.com/questions/49674004/docker-repository-server-gave-http-response-to-https-client
# in /etc/docker/daemon.json
# {
#     "insecure-registries" : ["docrepo.dmosk.local:5000"]
# }
# start container
# docker run -d -p 5000:5000 --restart=always --name registry -v /dockerrepo:/var/lib/registry -v /etc/docker/auth:/auth  -e REGISTRY_AUTH=htpasswd -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" registry:2