@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
title TutorLink - Phat Song Online 24/7 Tam Thoi
cd /d "%~dp0"
python share_online.py
pause

