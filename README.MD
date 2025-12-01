## Руководство по запуску
###	1.	Установить Python 3
###	2.	Создать виртуальное окружение:
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
###	4.	Установить зависимости(запускать в корне проекта):
```bash
pip install -r requirements.txt
```
###	5. Запуск:
```bash
python main.py
```