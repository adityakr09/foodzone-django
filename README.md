<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=FF6A00&center=true&vCenter=true&width=500&lines=🍕+FoodZone;Full-Stack+Food+Ordering;Built+with+Django+6.0" alt="Typing SVG" />

<br/>

> **A production-ready food ordering platform** — user auth, food customization, cart, order tracking & automated email invoices.

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-FF6A00?style=for-the-badge)

<br/>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-FF6A00?style=for-the-badge)](https://your-link-here.com)

</div>

---

## 📸 Screenshots

> _Add screenshots of your Home, Food Detail, Cart, and Order Success pages here_

---

## ✨ Features

<table>
<tr>
<td>

**🔐 User Authentication**  
Register, Login, Logout with session-based security & Google reCAPTCHA v2

**👤 User Profiles**  
Profile picture upload, address management, User/Vendor roles

**🍔 Food Catalogue**  
Browse by category: Pizza, Burger, Biryani, Beverages, Desserts, Fries

**⚙️ Food Customization**  
Dynamic size, base, toppings & sauces with live pricing

</td>
<td>

**🛒 Cart System**  
Add, update quantity, and remove items seamlessly

**📦 Order Management**  
UUID-based orders with status tracking: `Pending → Confirmed → Delivered`

**📧 Email Invoices**  
Automated bill sent via SMTP (Gmail) on every order placement

**🧑‍💼 Vendor Panel**  
Vendors can independently add & manage food items

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology |
|:---:|:---:|
| **Language** | Python 3.x |
| **Framework** | Django 6.0 |
| **Database** | SQLite3 (dev) / PostgreSQL (prod) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Forms** | Django Crispy Forms |
| **Auth** | Django Auth + Google reCAPTCHA v2 |
| **Email** | SMTP (Gmail) |
| **Container** | Docker |

---

## 🔄 Order Lifecycle

```
🛍️ Browse  →  ⚙️ Customize  →  🛒 Cart  →  📦 Order Placed  →  📧 Invoice Sent  →  ✅ Delivered
```

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

### 2. Create & activate virtual environment
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
```bash
cp .env.example .env
```

Edit `.env` with your values:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
```

> ⚠️ **Never commit your `.env` file** — it's listed in `.gitignore`

### 5. Run migrations & start server
```bash
cd learning
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## 🐳 Docker Setup

```bash
git clone https://github.com/YOUR_USERNAME/foodzone-django.git
cd foodzone-django

docker build -t foodzone .
docker run -p 8000:8000 foodzone
```

Visit: **http://localhost:8000**

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for dev, `False` for prod |
| `EMAIL_HOST_USER` | Gmail address for sending invoices |
| `EMAIL_HOST_PASSWORD` | Gmail App Password _(not your login password)_ |
| `RECAPTCHA_PUBLIC_KEY` | Google reCAPTCHA v2 site key |
| `RECAPTCHA_PRIVATE_KEY` | Google reCAPTCHA v2 secret key |

---

## 📊 Database Models

```
UserDetails        →  Extended user profile (phone, address, city, role)
FoodItems          →  Catalogue with category, price, rating, image
CustomizedOption   →  Size / Base / Topping / Sauce options + pricing
Customization      →  Stores user's full customization choices
Cart               →  Temporary cart items per session
Order + OrderItem  →  Placed orders with UUID, status, and line items
```

---

## 📧 Email Invoice

On successful order placement, the system automatically sends a bill/invoice to the registered user using Django's SMTP backend with Gmail.

> Template: `templates/emails/bill_invoice_template.html`

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 👨‍💻 Author

<div align="center">

### Aditya Kumar

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://your-linkedin-url)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://your-github-url)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:adityachy0077@gmail.com)

</div>

---

## 📄 License

This project is open source and available under the **[MIT License](LICENSE)**.

---

<div align="center">

**If you found this helpful, drop a ⭐ — it means a lot!**

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&duration=4000&pause=500&color=FF6A00&center=true&vCenter=true&width=400&lines=Built+with+❤️+by+Aditya+Kumar;Django+%7C+Python+%7C+Bootstrap+5" alt="Footer" />

</div>
