<div align="center">

# 🍕 FoodZone

### Full-Stack Food Ordering Platform

*User Auth · Food Customization · Cart · Order Tracking · Email Invoices*

---

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat-square&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Prod-336791?style=flat-square&logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-FF6A00?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-28a745?style=flat-square)

<br/>

**[🚀 Live Demo](https://your-link-here.com)** &nbsp;·&nbsp; **[📝 Report Bug](https://github.com/YOUR_USERNAME/foodzone-django/issues)** &nbsp;·&nbsp; **[💡 Request Feature](https://github.com/YOUR_USERNAME/foodzone-django/issues)**

</div>

---

## 📖 About

**FoodZone** is a production-ready food ordering web app built with **Python & Django 6.0**. It supports end-to-end ordering — from browsing and customizing food to placing orders and receiving email invoices automatically.

> Built as a full-stack project with real-world features like reCAPTCHA, UUID order IDs, vendor panel, Docker support, and SMTP email invoices.

---

## 📸 Screenshots

> Add screenshots of your Home, Food Detail, Cart, and Order Success pages here

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **User Authentication** | Register, Login, Logout with session security & Google reCAPTCHA v2 |
| 👤 **User Profiles** | Profile picture upload, address management, User/Vendor roles |
| 🍔 **Food Catalogue** | Browse by category: Pizza, Burger, Biryani, Beverages, Desserts, Fries |
| ⚙️ **Food Customization** | Choose size, base, toppings & sauces with dynamic pricing |
| 🛒 **Cart System** | Add, update quantity, and remove items |
| 📦 **Order Management** | UUID-based orders · `Pending → Confirmed → Delivered` |
| 📧 **Email Invoices** | Auto-send bill to user email on order via SMTP (Gmail) |
| 🧑‍💼 **Vendor Panel** | Vendors can add & manage their food items |
| 🔒 **Secure Passwords** | PBKDF2, Argon2, BCrypt support |

---

## 🔄 Order Flow

```
🛍️ Browse  ──►  ⚙️ Customize  ──►  🛒 Add to Cart  ──►  📦 Place Order  ──►  📧 Invoice Sent  ──►  ✅ Delivered
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.x |
| **Framework** | Django 6.0 |
| **Database** | SQLite3 (dev) · PostgreSQL (prod) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Forms** | Django Crispy Forms |
| **Auth** | Django Auth + Google reCAPTCHA v2 |
| **Email** | SMTP via Gmail |
| **Container** | Docker |

---

## 📁 Project Structure

```
learning/
├── learning/               # Project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── learningapp/            # User auth & profile app
│   ├── models.py           # UserDetails model
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── foodsapp/               # Core food ordering app
│   ├── models.py           # FoodItems, Cart, Order, Customization models
│   ├── views.py
│   ├── urls.py
│   └── utils.py            # Email invoice utility
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── cart.html
│   ├── foods/
│   └── emails/
├── static/
├── media/
├── manage.py
└── requirements.txt
```

---

## ⚙️ Local Setup

### Without Docker

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/foodzone-django.git
cd foodzone-django
```

**2. Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Setup environment variables**
```bash
cp .env.example .env
```

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
RECAPTCHA_PUBLIC_KEY=your-recaptcha-site-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-secret-key
```

> ⚠️ Use a **Gmail App Password**, not your actual Gmail password. Never commit `.env` to git.

**5. Run migrations & start server**
```bash
cd learning
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

🌐 Open: **http://127.0.0.1:8000**

---

### With Docker

```bash
git clone https://github.com/YOUR_USERNAME/foodzone-django.git
cd foodzone-django

docker build -t foodzone .
docker run -p 8000:8000 foodzone
```

🌐 Open: **http://localhost:8000**

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for dev · `False` for production |
| `EMAIL_HOST_USER` | Gmail address for sending invoices |
| `EMAIL_HOST_PASSWORD` | Gmail App Password (not your login password) |
| `RECAPTCHA_PUBLIC_KEY` | Google reCAPTCHA v2 site key |
| `RECAPTCHA_PRIVATE_KEY` | Google reCAPTCHA v2 secret key |

---

## 📊 Database Models

```
UserDetails        →  Extended profile (phone, address, city, role)
FoodItems          →  Catalogue (category, price, rating, image)
CustomizedOption   →  Size / Base / Topping / Sauce options + pricing
Customization      →  User's saved customization per order item
Cart               →  Temporary cart items per session
Order              →  Placed orders (UUID, status, timestamp)
OrderItem          →  Line items per order
```

---

## 📧 Email Invoice

On successful order placement, an invoice is automatically emailed to the user via Django's SMTP backend.

Template: `templates/emails/bill_invoice_template.html`

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add your feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👨‍💻 Author

<div align="center">

**Aditya Kumar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://your-linkedin-url)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://your-github-url)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:adityachy0077@gmail.com)

</div>

---

## 📄 License

This project is open source and available under the **[MIT License](LICENSE)**.

---

<div align="center">

⭐ **If this project helped you, please give it a star!** ⭐

*Built with ❤️ by Aditya Kumar*

</div>
