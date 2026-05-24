<p align="center">
  <img src="[https://capsule-render.vercel.app/api?type=waving&color=0:075e54,100:128c7e&height=220&section=header&text=E-Sa%C4%9Fl%C4%B1k%20Connect&fontSize=42&fontColor=ffffff&fontAlignY=35](https://capsule-render.vercel.app/api?type=waving&color=0:075e54,100:128c7e&height=220&section=header&text=E-Sa%C4%9Fl%C4%B1k%20Connect&fontSize=42&fontColor=ffffff&fontAlignY=35)" />
</p>

<p align="center">
  <img src="[https://readme-typing-svg.herokuapp.com?font=Montserrat&size=22&duration=3000&pause=800&color=128C7E&center=true&vCenter=true&width=700&lines=Online+Healthcare+%26+Consultancy+Platform;Real-time+WhatsApp+Style+Live+Chat;Secure+Jitsi+Meet+Video+Consultation;Built+with+Django+and+Layered+Architecture](https://readme-typing-svg.herokuapp.com?font=Montserrat&size=22&duration=3000&pause=800&color=128C7E&center=true&vCenter=true&width=700&lines=Online+Healthcare+%26+Consultancy+Platform;Real-time+WhatsApp+Style+Live+Chat;Secure+Jitsi+Meet+Video+Consultation;Built+with+Django+and+Layered+Architecture)" />
</p>

<h1 align="center">🩺 E-Sağlık Connect</h1>

<p align="center">
  A comprehensive online healthcare and teleconsultancy web platform connecting clients with specialized consultants.
</p>

<p align="center">
  <img src="[https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)" />
  <img src="[https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white](https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white)" />
  <img src="[https://img.shields.io/badge/UI-HTML5%20%26%20CSS3-E34F26?style=for-the-badge&logo=html5&logoColor=white](https://img.shields.io/badge/UI-HTML5%20%26%20CSS3-E34F26?style=for-the-badge&logo=html5&logoColor=white)" />
  <img src="[https://img.shields.io/badge/Database-SQLite%20%2F%20PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white](https://img.shields.io/badge/Database-SQLite%20%2F%20PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)" />
  <img src="[https://img.shields.io/badge/Status-Active%20Development-128c7e?style=for-the-badge](https://img.shields.io/badge/Status-Active%20Development-128c7e?style=for-the-badge)" />
</p>

## 📖 About the Project

**E-Sağlık Connect** is a feature-rich, data-driven **web application** designed to digitize patient-expert interactions. It provides secure workflows tailored for both **clients (students)** looking for professional guidance and **specialized consultants** (Dietitians, Psychologists, and Physiotherapists).

The system prioritizes real-time communication, clean profile management, automated appointment schedules, and safe wallet/billing balances, making it an ideal choice for **academic presentations** and **real-world telehealth implementations**.

## ✨ Features

### 👤 Role-Based Authentication
- Distinct login/registration flows for Clients and Consultants.
- Unique consultant keys to maintain secure registration filters.
- Customizable profile cards with live avatar/biography updates.

### 💬 WhatsApp-Style Live Chat
- Dedicated, synchronized, persistent chat rooms between matching parties.
- Smooth iframe overlay dashboards ensuring unbroken layout integrity.
- Automated read/unread status badges ensuring message awareness.

### 📅 Appointment & Seans Management
- Dynamic scheduler for consultants to add or modify availability slots.
- Direct booking interfaces checking client account funding beforehand.
- Status workflows for administrative approvals, rejections, and refund rollbacks.

### 📹 Seamless Video Consultation
- Secure integration with Jitsi Meet APIs.
- One-click "Connect" buttons dynamically generated for verified, upcoming, or active slots.

### 💳 Digital Wallet & Revenue Engine
- Secure client balance updates through a simulated point-of-sale card screen.
- Automated consultant balance split triggers upon slot confirmations.

## 🛠 Tech Stack

<p align="center">
  <img src="[https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg)" width="55" />
  <img src="[https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg)" width="55" />
  <img src="[https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg)" width="55" />
  <img src="[https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg)" width="55" />
</p>

**Technologies Used**
- **Programming Language:** Python
- **Backend Web Framework:** Django
- **UI Components:** FontAwesome, Google Fonts (Plus Jakarta Sans)
- **Database Architecture:** Django ORM (SQLite for development / PostgreSQL production ready)
- **Video Platform API:** Jitsi Meet open-source integration

## 🚀 Installation & Run

1️⃣ Python 3.10+ must be installed on your local environment.

2️⃣ Clone the repository:

```bash
git clone https://github.com/cemreeyrtsvr/okul_projem.git
```

3️⃣ Set up a virtual environment and activate it:

```bash
python -m venv .venv
```

On Windows:
```bash
.venv\Scripts\activate
```

On macOS/Linux:
```bash
source .venv/bin/activate
```

4️⃣ Sync database schemas and migrations:

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

To securely run dashboard overlay structures and embedded live chat interfaces without rendering browser blocks, check your iframe configurations.

### 📌 Steps

1️⃣ Open your Django project's `settings.py` file.

2️⃣ Locate or append the following security middleware preference line:

```python
X_FRAME_OPTIONS = 'SAMEORIGIN'
```

3️⃣ Save the file and restart your local `runserver` task.

---

## 🧠 Purpose

This project was developed to:
- Learn robust full-stack model-view-template (MVT) paradigms.
- Practice atomic database transaction handling across simulated currency assets.
- Map complex frontend single-page communication aesthetics using nested overlay frames.
- Design modular, user-first teleconsultancy portals.

---

## 👩‍💻 Developer

**Cemre Yurtsever**

🎓 Software Engineering Student  
💻 C# • Python • Java  
🤖 AI & Data Science Enthusiast  

📫 Contact:

<p align="left">
  <a href="[https://www.linkedin.com/in/cemre-yurtsever](https://www.linkedin.com/in/cemre-yurtsever)">
    <img src="[https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg](https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg)" height="35"/>
  </a>
  <a href="mailto:cyurtsever64@gmail.com">
    <img src="[https://cdn-icons-png.flaticon.com/512/732/732200.png](https://cdn-icons-png.flaticon.com/512/732/732200.png)" height="35"/>
  </a>
</p>

---

⭐ If you find this repository useful, don’t forget to star it!

<p align="center">
  <img src="[https://capsule-render.vercel.app/api?type=waving&color=0:128c7e,100:075e54&height=120&section=footer](https://capsule-render.vercel.app/api?type=waving&color=0:128c7e,100:075e54&height=120&section=footer)"/>
</p>
