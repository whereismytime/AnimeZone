# 🎌 AnimeZone — Django Anime Portal

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/django-5.x-green.svg)](https://www.djangoproject.com)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

AnimeZone is a full-featured Django web portal for anime fans. It includes a custom UI, blog system, user accounts, dynamic content and an adapted Anime template from ThemeWagon.

## ✨ Features

- 📺 **Extensive Anime Catalog** with filtering and search
- 👥 **User Accounts** with registration and profiles  
- 📝 **Blog System** for news and articles
- 🎨 **Custom UI** with responsive design
- ⚡ **Dynamic Frontend** using jQuery/AJAX
- 🔑 **Admin Panel** for content management

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/whereismytime/AnimeZone.git
cd AnimeZone
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User

```bash 
python manage.py createsuperuser
```

### 6. Check Static & Media Directories

Create if missing:
```bash
mkdir static
mkdir media
```

### 7. Start Development Server

```bash
python manage.py runserver
```

Visit 👉 http://127.0.0.1:8000/

## 🛠️ Tech Stack

- Django 5.x
- HTML5 + Bootstrap 4
- jQuery / AJAX
- SQLite
- Anime Template (ThemeWagon)

---

## 📄 License

Open-source project. Feel free to edit, share, and use for commercial purposes.


