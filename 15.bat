@echo off
chcp 1251

cd /d %1

echo ������ ������ ���������� � �������� � � ���������:
dir /b /s /a-d "*.doc" "*.docx" "*.pdf" "*.txt" "*.rtf" "*.odt" "*.xls" "*.xlsx" "*.ppt" "*.pptx" "*.odp"