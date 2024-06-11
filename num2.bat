@echo off
setlocal enabledelayedexpansion
set /p grades="Введите номера курсов: "
set /p max="Введите максимум студентов в группе: "
mkdir "Студенты"
cd "Студенты"
set del="*"
rem dir *
for %%i in (%grades%) do (
	mkdir "курс %%i"
	cd "курс %%i"
	dir *
	set /p groups="Введите шифры групп: "
	for %%j in (!groups!) do (
		rem if %%j
		mkdir "%%j"
		rem dir *
		cd "%%j"
		rem dir *
		for /l %%k in (1, 1, !max!) do (
			mkdir "папка %%k"
		)
		rem mkdir "proverka" 
		cd ..
	)
	cd ..
)

endlocal
pause
rmdir /s /q "D:\Учеба\студенты"
