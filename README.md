<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:075e54,100:128c7e&height=220&section=header&text=E-Sa%C4%9Fl%C4%B1k%20Connect&fontSize=42&fontColor=ffffff&fontAlignY=35" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Montserrat&size=22&duration=3000&pause=800&color=128C7E&center=true&vCenter=true&width=700&lines=Online+Healthcare+%26+Consultancy+Platform;Real-time+WhatsApp+Style+Live+Chat;Secure+Jitsi+Meet+Video+Consultation;Built+with+Python+and+Django" />
</p>

<h1 align="center">🩺 E-Sağlık Connect</h1>

<p align="center">
  A comprehensive, data-driven web application connecting clients with specialized healthcare consultants.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/UI-HTML5%20%26%20CSS3-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active%20Development-128c7e?style=for-the-badge" />
</p>

## 📖 About the Project

**E-Sağlık Connect** is a feature-rich **web application** designed to digitize patient-expert interactions.  
It provides secure workflows tailored for both **clients (students)** looking for professional guidance and **specialized consultants** (Dietitians, Psychologists, and Physiotherapists).

The system prioritizes real-time communication, clean profile management, automated appointment schedules, and secure digital wallet balances, making it an ideal choice for **academic projects**, **portfolio presentation**, and **real-world telehealth implementations**.

## ✨ Features

### 👤 Role-Based Authentication
- Distinct login and registration workflows for Clients and Consultants.
- Unique registration keys for verifying expert accounts.
- Customizable user profile dashboards with dynamic data binding.

### 💬 WhatsApp-Style Live Chat
- Real-time, synchronized, and persistent chat rooms between matching parties.
- Smooth iframe overlay dashboards ensuring an unbroken UI experience.
- Automated read/unread status badges for message tracking.

### 📅 Appointment & Session Management
- Dynamic scheduler for experts to define availability slots.
- Direct booking interfaces with automated wallet balance checks.
- Workflow management for approvals, rejections, and refund rollbacks.

### 📹 Seamless Video Consultation
- Embedded integration using Jitsi Meet for secure telehealth sessions.
- Auto-generated, one-click "Connect" buttons for approved appointments.

### 💳 Digital Wallet System
- Secure client balance top-ups simulating payment gateway logic.
- Automated revenue splitting and wallet deduction upon appointment confirmation.

## 🛠 Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="55" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="55" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="55" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="55" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="55" />
</p>

**Technologies Used**
- **Programming Language:** Python 3.10+
- **Backend Framework:** Django (MVT Architecture)
- **Frontend / UI:** HTML5, CSS3, JavaScript, FontAwesome
- **Database:** SQLite (Development) / PostgreSQL (Production Ready)
- **External APIs:** Jitsi Meet (Video calls)

## 🚀 Installation & Run

1️⃣ Python 3.10+ must be installed on your system.

2️⃣ Clone the repository:

```bash
git clone [https://github.com/cemreeyrtsvr/okul_projem.git](https://github.com/cemreeyrtsvr/okul_projem.git)
```

3️⃣ Set up a virtual environment and activate it:

```bash
python -m venv .venv
```

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

4️⃣ Synchronize the database schemas and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Run the local development server 🚀:

```bash
python manage.py runserver
```

---
---

## 🔐 Security Configuration (settings.py)

To securely run the embedded live chat and iframe overlay features without browser restrictions, verify your Django security settings.

### 📌 Steps

1️⃣ Open the `settings.py` file in the project.

2️⃣ Locate or append the following security preference:

```python
X_FRAME_OPTIONS = 'SAMEORIGIN'
```

3️⃣ Save the file and restart your local `runserver` instance.

⚠️ **Note:** This configuration is essential to prevent `Connection Refused` errors inside the dashboard chat windows.

---

## 🧠 Purpose

This project was developed to:

- Learn and implement the Django Model-View-Template (MVT) architecture.
- Practice relational database design and ORM queries.
- Build complex frontend logic using dynamic iframes and asynchronous-like UI flows.
- Implement transactional data handling for digital wallets and appointment bookings.

---

## 👩‍💻 Developer

**Cemre Yurtsever**

🎓 Software Engineering Student  
💻 Python • C# • Java  
🤖 AI & Data Science Enthusiast  

📫 Contact:

<p align="left">
  <a href="https://www.linkedin.com/in/cemre-yurtsever">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" height="35"/>
  </a>
  <a href="mailto:cyurtsever64@gmail.com">
    <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" height="35"/>
  </a>
</p>

---

⭐ If you find this repository useful, don’t forget to star it!

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:128c7e,100:075e54&height=120&section=footer"/>
</p>
