apt-get install update
apt-get install ffmpeg -y
apt-get install python3-dev python-dev -y
apt-get install pavucontrol -y
apt-get install espeak -y
apt-get install python3-dev -y
apt-get install pyaudio -y
apt-get install python-pyaudio python3-pyaudio portaudio19-dev python-all-dev python3-all-dev -y
apt-get install pulseaudio -y
apt-get install flac -y
apt-get install update

curl https://yt-dl.org/latest/youtube-dl -o /usr/local/youtube-dl
chmod a+rx /usr/local/bin/youtube-dl
youtube-dl -U

pip3 install requests
pip3 install wheel
pip3 install youtube_dl
pip3 install --upgrade youtube_dl
pip3 install pyaudio
pip3 install pytube
pip3 install BeautifulSoup4
pip3 install pyttsx3
pip3 install SpeechRecognition
pip3 install PyAudio
pip3 install google-api-python-client

chmod +x scrape_cron.sh
chmod +x selim_init.py
./scrape_cron.sh
chmod +x youtube.sh

mv -f selim-start.conf /etc/init 