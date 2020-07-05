# GraGiełdowa Exporter

## Instrukcja użytkowania
1. Wykonaj następująca komendę w PowerShell, aby włączyć WSL
```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
2. Zrestartuj komputer
3. Wykonaj następującą komendę w PowerShell, by zmienić wersję WSL na 2 (opcjonalne)
```
wsl.exe --set-default-version 2
```
4. Zainstaluj Ubuntu z [Microsoft Store](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab)
5. Pobierz [aplikację](https://github.com/Soni96pl/gragieldowa-exporter/releases/) i wypakuj
6. Uruchom install.cmd aby zainstalować wymagane komponenty aplikacji
7. Uruchom run.cmd aby wykonać aplikacje
8. Pobrane pliki CSV pojawią się w exports/purchase.csv i exports/sale.csv
