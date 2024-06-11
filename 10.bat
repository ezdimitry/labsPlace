@echo off
chcp 1251

:repeat
set /p "folder_path=������� ���� � �����: "

echo �������� ������ ������:
echo 1 - �������
echo 2 - ����
echo 3 - �������

set /p "output_choice=������� ����� ������� ������: "

if "%output_choice%"=="1" (
    goto process
) else if "%output_choice%"=="2" (
    goto process
) else if "%output_choice%"=="3" (
    goto process
) else (
    echo ������������ ����� ������� ������. ����������, �������� �� ��������� ���������.
    goto repeat
)

:process
if "%folder_path%"=="" (
    echo ����������, ������� ���� � �����.
    exit /b
)

if "%output_choice%"=="1" (
    tree /f %folder_path%
) else if "%output_choice%"=="2" (
    tree /f %folder_path% > tree_output.txt
    echo ���������� ��������� � ����� tree_output.txt
) else if "%output_choice%"=="3" (
    tree /f %folder_path% > prn
    echo ���������� ���������� �� �������
)