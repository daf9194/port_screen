# Сканер портов

## Описание
Для проверки безопасности сетей, а также для сбора информации о работающих сетевых сервисах применяется процесс, называемый сканированием сети. Это консольное приложение, принимающее на вход диапазон ip-адресов (например 192.168.1.0) и список портов (например 80, 443,22, 21, 25). Результатом выполнения является список открытых портов с указанием удаленного хоста.

### Работа с приложением
- В файле hosts.txt неоходимо указать список ip-адресов, которые необходимо проверить:
![Пример](https://raw.githubusercontent.com/daf9194/port_screen/master/img/scr_1.png)

- В файле main.py в строке №6, в переменной `port_lst` указать список портов для проверки:
![Пример](https://raw.githubusercontent.com/daf9194/port_screen/master/img/scr_2.png)

## Установка приложения
1. Клонировать текущий репозиторий.
2. Установка необходимых Python-пакетов  
`python3 -m pip install -r requirements.txt`
3. Указание ip-адресов и портов.
3. Запуск скрипта  
`python3 main.py`
