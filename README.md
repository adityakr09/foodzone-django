<div align="center">

<img src="./header.svg" width="100%"/>

<br/>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Coming_Soon-f97316?style=for-the-badge)](https://github.com/adityakr09)
[![GitHub](https://img.shields.io/badge/GitHub-adityakr09-181717?style=for-the-badge&logo=github)](https://github.com/adityakr09)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aditya_Kumar-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/aditya-kumar-O1)

<br/>

![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django_6.0-092E20?style=flat-square&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

<br/>

> **Built by — [Aditya Kumar](https://github.com/adityakr09)**

</div>

---

## ✨ Features

<table>
  <tr>
    <td>🔐 <b>User Authentication</b></td>
    <td>Register, Login, Logout with session-based security & Google reCAPTCHA</td>
  </tr>
  <tr>
    <td>👤 <b>User Profiles</b></td>
    <td>Profile picture upload, address management, User/Vendor roles</td>
  </tr>
  <tr>
    <td>🍔 <b>Food Catalogue</b></td>
    <td>Browse by category — Pizza, Burger, Biryani, Beverages, Desserts, French Fries</td>
  </tr>
  <tr>
    <td>⚙️ <b>Food Customization</b></td>
    <td>Choose size, base, toppings & sauces with dynamic pricing</td>
  </tr>
  <tr>
    <td>🛒 <b>Cart System</b></td>
    <td>Add, update quantity, and remove items</td>
  </tr>
  <tr>
    <td>📦 <b>Order Management</b></td>
    <td>UUID-based order IDs, status tracking — Pending → Confirmed → Delivered</td>
  </tr>
  <tr>
    <td>📧 <b>Email Invoices</b></td>
    <td>Automated bill sent to user email on order placement via SMTP</td>
  </tr>
  <tr>
    <td>🧑‍💼 <b>Vendor Panel</b></td>
    <td>Vendors can add and manage their food items</td>
  </tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.x |
| **Framework** | Django 6.0 |
| **Database** | SQLite3 (dev) / PostgreSQL (prod) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Forms** | Django Crispy Forms |
| **Auth** | Django Auth + Google reCAPTCHA |
| **Email** | SMTP (Gmail) |
| **Container** | Docker |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip
- Git

### 1️⃣ Clone the repo

```bash
git clone https://github.com/adityakr09/foodzone-django.git
cd foodzone-django
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

```bash
cp .env.example .env
# Edit .env with your values
```

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
```

### 5️⃣ Run migrations & start server

```bash
cd learning
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> 🟢 Visit: `http://127.0.0.1:8000`

---

## 🐳 Docker Setup

```bash
git clone https://github.com/adityakr09/foodzone-django.git
cd foodzone-django

docker build -t foodzone .
docker run -p 8000:8000 foodzone
```

> 🟢 Visit: `http://localhost:8000`

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for dev, `False` for prod |
| `EMAIL_HOST_USER` | Gmail address for sending invoices |
| `EMAIL_HOST_PASSWORD` | Gmail App Password (not login password) |
| `RECAPTCHA_PUBLIC_KEY` | Google reCAPTCHA v2 site key |
| `RECAPTCHA_PRIVATE_KEY` | Google reCAPTCHA v2 secret key |

> [!WARNING]
> Never commit your real `.env` file — it is listed in `.gitignore`.

---

## 📊 Database Models

<details>
<summary><b>👤 UserDetails</b></summary>
<br/>
Extended user profile — phone, address, city, user type (User/Vendor)
</details>

<details>
<summary><b>🍔 FoodItems</b></summary>
<br/>
Food catalogue with category, price, rating, and image
</details>

<details>
<summary><b>⚙️ CustomizedOption + Customization</b></summary>
<br/>
Size / Base / Topping / Sauce options with pricing — stores user's customization choices per order
</details>

<details>
<summary><b>🛒 Cart</b></summary>
<br/>
Temporary cart items per user session
</details>

<details>
<summary><b>📦 Order + OrderItem</b></summary>
<br/>
Placed orders with UUID, status tracking, and line items
</details>

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
│   ├── models.py           # FoodItems, Cart, Order, Customization
│   ├── views.py
│   ├── urls.py
│   └── utils.py            # Email invoice utility
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── cart.html
│   ├── foods/
│   └── emails/             # Invoice email template
├── static/                 # CSS, JS, images
├── media/                  # User & food uploaded images
├── manage.py
└── requirements.txt
```

---

## 📧 Email Invoice

On successful order placement, the system automatically emails a bill/invoice to the registered user via Django's SMTP backend with Gmail.

> Template: `templates/emails/bill_invoice_template.html`

---

## 📝 Notes

> [!IMPORTANT]
> Use a **Gmail App Password** for `EMAIL_HOST_PASSWORD` — not your regular login password. [Generate one here](https://myaccount.google.com/apppasswords).

> [!NOTE]
> Database defaults to **SQLite** for development. Set `DATABASE_URL` in `.env` for PostgreSQL in production.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f97316,50:ec4899,100:8b5cf6&height=120&section=footer" width="100%"/>

**Made with ❤️ by [Aditya Kumar](https://github.com/adityakr09)**

</div>
