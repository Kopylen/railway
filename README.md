# 🌱 CraftyNet

**CraftyNet** is a developer-friendly social platform where users can share tips, hacks, and posts related to coding. It's built with Django and styled using Tailwind CSS to deliver a clean and responsive UI.

---

## 🚀 Features

- 🔐 User authentication (register, login, logout)
- 🧑‍💻 User profiles with photo, bio, and follower stats
- 📝 Create, edit, and delete posts
- 💬 Comment and reply to posts
- ❤️ Like posts and view popular ones
- 📁 Upload user photos and post images
- 🧭 Categories (Tips, Hacks)
- 🫂 Follow/unfollow other users
- 🔍 Search users or browse followers/following
- 🧑 Admin panel for managing data

---

## 🛠️ Technologies Used

- **Backend:** Django 5.2
- **Frontend:** Tailwind CSS + Bootstrap (light)
- **Database:** SQLite (default, can switch to PostgreSQL)
- **Static Files:** Managed via Django static system
- **Templates:** Django templating engine

---

## 📸 Screenshots

![Screenshot](static/srcp/images/icon.png)

---

## 🧑‍💻 Getting Started

### Clone the repository
```bash
git clone https://github.com/Kopylen/CraftyNet.git
cd CraftyNet

### Create a virtual environment

python3 -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows

### Install dependencies

pip install -r requirements.txt

### Run migrations

python manage.py migrate

### Create superuser

python manage.py createsuperuser

### Run the development server

python manage.py runserver
