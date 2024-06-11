@echo off
chcp 1251

:repeat
set /p "folder_path=Введите путь к папке: "

echo Выберите формат вывода:
echo 1 - Консоль
echo 2 - Файл
echo 3 - Принтер

set /p "output_choice=Введите номер формата вывода: "

if "%output_choice%"=="1" (
    goto process
) else if "%output_choice%"=="2" (
    goto process
) else if "%output_choice%"=="3" (
    goto process
) else (
    echo Недопустимый выбор формата вывода. Пожалуйста, выберите из доступных вариантов.
    goto repeat
)

:process
if "%folder_path%"=="" (
    echo Пожалуйста, укажите путь к папке.
    exit /b
)

if "%output_choice%"=="1" (
    tree /f %folder_path%
) else if "%output_choice%"=="2" (
    tree /f %folder_path% > tree_output.txt
    echo Результаты сохранены в файле tree_output.txt
) else if "%output_choice%"=="3" (
    tree /f %folder_path% > prn
    echo Результаты отправлены на принтер
)