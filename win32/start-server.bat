@echo off
title otp-socket-server

cd ../

:main
python -m server.base.ServerStart
pause
goto main
