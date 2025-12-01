## Руководство по запуску
###	1.	Установить Python 3
###	2.	Создать виртуальное окружение:
#### Linux & Mac
```bash
python3 -m venv .venv
```
#### Windows
```bash
python -m venv .venv
```
###	3.	Активировать виртуальное окружение:
#### Linux & Mac
```bash
source .venv/bin/activate
```
#### Windows
```bash
.venv\Scripts\activate     
```
###	5.	Обновить pip:
```bash
pip install --upgrade pip
```
###	4.	Установить зависимости:
```bash
pip install -r requirements.txt
```
###	5. Запуск:
#### Linux & Mac
```bash
python3 main.py
```
#### Windows
```bash
python main.py
```