powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/k cd /d %~dp0 & start /b cleari.py & exit'"