if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/GouthamSER/Filter-bot.git /EvaMaria
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Filter-bot
fi
cd /Filter-bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
