@echo off

:start
cls
echo installing modules...
pip install discord.py
pip install tweepy
pip install praw

echo DONE!
pause
exit