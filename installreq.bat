@echo off

:start
cls

echo setting python ver...
set python_ver=39

echo getting pip...
python ./get-pip.py

echo finding python...
cd \
cd \python%python_ver%\Scripts\
echo installing modules...
pip install discord.py
pip install tweepy
pip install praw

echo DONE!
pause
exit