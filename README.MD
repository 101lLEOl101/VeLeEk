## Руководство по запуску
### 1.  Перед началом запустите Postgresql с такими данными на localhost
```bash
POSTGRES_DB: VeLeEk
```
```bash
POSTGRES_PASSWORD: root
```
```bash
POSTGRES_USER: root
```
```bash
ports: 5432:5432
```
###	2.	Установить Python 3
###	3.	Создать виртуальное окружение:
#### Linux & Mac
```bash
python3 -m venv .venv
```
#### Windows
```bash
python -m venv .venv
```
###	4.	Активировать виртуальное окружение:
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
###	6.	Установить зависимости:
```bash
pip install -r requirements.txt
```
###	7. Запуск:
#### Linux & Mac
```bash
python3 main.py
```
#### Windows
```bash
python main.py
```
## При добавлении новых зависимостей
### Обновляем requirements.txt
```bash
pip freeze > requirements.txt
```
