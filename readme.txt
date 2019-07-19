Setup:
---

cd personal_site/
git pull
sudo killall gunicorn
sudo nohup gunicorn -w 4 serve:app -b 0.0.0.0:80 --log-file=stderr.log --enable-stdio-inheritance &
