powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/k cd /d %~dp0 & start /b clear.py & exit'"