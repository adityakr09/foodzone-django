# 🍕 FoodZone — Full-Stack Food Ordering Web App

A production-ready food ordering platform built with **Python & Django**, featuring user authentication, food customization (size, base, toppings, sauces), cart management, order tracking, and automated email invoices.

---

## 🚀 Live Demo
> _Add your deployed link here (Railway / Render / PythonAnywhere)_

---

## 📸 Screenshots

> _Add screenshots of your home page, food detail, cart, and order success pages here_

---

## ✨ Features

- 🔐 **User Authentication** — Register, Login, Logout with session-based security & Google reCAPTCHA
- 👤 **User Profiles** — Profile picture upload, address management, User/Vendor roles
- 🍔 **Food Catalogue** — Browse items by category (Pizza, Burger, Biryani, Beverages, Desserts, French Fries)
- ⚙️ **Food Customization** — Choose size, base, toppings, and sauces with dynamic pricing
- 🛒 **Cart System** — Add, update quantity, and remove items
- 📦 **Order Management** — Place orders with UUID-based order IDs and status tracking (Pending → Confirmed → Delivered)
- 📧 **Email Invoices** — Automated bill/invoice sent to user email on order placement via SMTP
- 🧑‍💼 **Vendor Panel** — Vendors can add and manage food items
- 🔒 **Secure Password Hashing** — PBKDF2, Argon2, BCrypt support

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Framework | Django 6.0 |
| Database | SQLite3 (dev) / PostgreSQL (prod) |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Forms | Django Crispy Forms |
| Auth | Django Auth + reCAPTCHA |
| Email | SMTP (Gmail) |
| Container | Docker |
| Media | Django Media Files |

---

## 📁 Project Structure

```
learning/                   # Django project root
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
├── templates/              # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── cart.html
│   ├── foods/
│   └── emails/
├── static/                 # CSS, JS, images
├── media/                  # User & food uploaded images
├── manage.py
└── requirements.txt
```

---

## ⚙️ Local Setup (Without Docker)

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/foodzone-django.git
cd foodzone-django
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root (copy from `.env.example`):
```bash
cp .env.example .env
```

Edit `.env` with your values:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
```

### 5. Run migrations
```bash
cd learning
python manage.py migrate
```

### 6. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## 🐳 Local Setup (With Docker)

```bash
git clone https://github.com/YOUR_USERNAME/foodzone-django.git
cd foodzone-django

# Build and run
docker build -t foodzone .
docker run -p 8000:8000 foodzone
```

Visit: **http://localhost:8000**

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | True for development, False for production |
| `EMAIL_HOST_USER` | Gmail address for sending invoices |
| `EMAIL_HOST_PASSWORD` | Gmail App Password (not your login password) |
| `RECAPTCHA_PUBLIC_KEY` | Google reCAPTCHA v2 site key |
| `RECAPTCHA_PRIVATE_KEY` | Google reCAPTCHA v2 secret key |

> ⚠️ Never commit your real `.env` file. It is listed in `.gitignore`.

---

## 📊 Database Models

- **UserDetails** — Extended user profile (phone, address, city, user type)
- **FoodItems** — Food catalogue with category, price, rating, image
- **CustomizedOption** — Size / Base / Topping / Sauce options with pricing
- **Customization + CustomizationItem** — Stores user's customization choices
- **Cart** — Temporary cart items per session
- **Order + OrderItem** — Placed orders with UUID, status, and line items

---

## 📧 Email Invoice

On successful order placement, the system automatically emails a bill/invoice to the registered user using Django's SMTP backend with Gmail. Template located at `templates/emails/bill_invoice_template.html`.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 👨‍💻 Author

**Aditya Kumar**
- LinkedIn: [your-linkedin-url]
- GitHub: [your-github-url]
- Email: adityachy0077@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
