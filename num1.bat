@echo off
setlocal

set /p directory="Введите путь к директории: "
set /p extension="Введите расширение файлов (без точки): "

echo Выберите атрибуты для применения:
echo 1. Чтение
echo 2. Запись
echo 3. Скрытый
echo 4. Открытый
set /p selected_attribute="Введите номер атрибута: "

echo %selected_attribute%| findstr /R "[^1-4]" > nul
if errorlevel 1 (
    if "%selected_attribute%"=="1" set attributes=+r
    if "%selected_attribute%"=="2" set attributes=-r
    if "%selected_attribute%"=="3" set attributes=+h
    if "%selected_attribute%"=="4" set attributes=-h
    pushd %directory%
    for %%i in (*.%extension%) do attrib %%i %attributes%
    popd

    echo Атрибуты для файлов с расширением .%extension% в директории %directory% успешно изменены.
) else (
    echo Введен недопустимый символ. Пожалуйста, выберите номер атрибута от 1 до 4.
)

endlocal
pause