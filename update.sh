rm -rf /usr/local/teleserver/*
rm -rf /usr/local/teleserver/.git
cd /usr/local/
git clone https://github.com/Dysproz/teleserver.git
chmod 0777 /usr/local/teleserver/*
pkill -f teleserver
nohup python /usr/local/teleserver/run.py &