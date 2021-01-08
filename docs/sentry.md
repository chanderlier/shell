pip3 install docker-compose
git clone https://github.com/getsentry/onpremise.git
cd onpremise/
./install.sh 
docker-compose up -d
pip3 install --upgrade sentry-sdk
