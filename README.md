# 🎌 AnimeZone — Django Anime Portal

AnimeZone — це повноцінний Django-проєкт для створення аніме-порталу: з кастомним UI, блогом, системою акаунтів, кошиком, AJAX-логікою та адаптованим шаблоном Anime від ThemeWagon.

---

## 🚀 Швидкий старт

### 🔽 1. Клонувати репозиторій

```bash
git clone https://github.com/whereismytime/AnimeZone.git
cd AnimeZone
```

---

### 🐍 2. Створити та активувати віртуальне середовище

```bash
python -m venv venv
.\venv\Scripts\activate        # Windows

# або для Mac/Linux:
# source venv/bin/activate
```

---

### 📦 3. Встановити залежності

```bash
pip install -r requirements.txt
```

> Якщо файл `requirements.txt` відсутній, згенеруй:
```bash
pip freeze > requirements.txt
```

---

### ⚙️ 4. Застосувати міграції

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 👤 5. Створити адміністратора

```bash
python manage.py createsuperuser
```

---

### 💽 6. Перевірити наявність `static/` і `media/`

Якщо немає — створити:

```bash
mkdir static
mkdir media
```

---

### 🔥 7. Запустити сервер

```bash
python manage.py runserver
```

Перейти в браузері:  
👉 http://127.0.0.1:8000/

---

## 🛠️ Стек технологій

- Django 5.x
- HTML5 + Bootstrap 4
- jQuery / AJAX
- SQLite
- Anime Template (ThemeWagon)

---

## 📄 Ліцензія

Open-source проєкт. Можна вільно редагувати, поширювати і використовувати в комерційних цілях.
