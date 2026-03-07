# Flask Student Portal v2 

A modular Flask web application demonstrating advanced Python OOP, database integration (SQLite), and full CRUD operations.

##  Features
- **Database & ORM:** Uses **Flask-SQLAlchemy** and **Flask-Migrate** for managing students and courses.
- **Scalable Architecture:** Built with the **Application Factory Pattern** (`create_app`) and **Flask Blueprints**.
- **Full CRUD:** Create, Read, Update, and Delete student records via dynamic Jinja2 templates.
- **Seeding Script:** Quickly populate the database with demo data using `seed.py`.


<img width="1080" height="400" alt="Screenshot 2026-03-07 030218" src="https://github.com/user-attachments/assets/93dcba64-92ec-419c-8e44-2d44519d4bc5" />
<img width="1072" height="387" alt="Screenshot 2026-03-07 030242" src="https://github.com/user-attachments/assets/0e8d4305-c2b2-4575-ad15-f8a58fb3cdcb" />
<img width="482" height="397" alt="Screenshot 2026-03-07 025633" src="https://github.com/user-attachments/assets/fd9f58d5-14d6-419f-bef6-88af6a651055" />
<img width="447" height="327" alt="Screenshot 2026-03-07 025715" src="https://github.com/user-attachments/assets/8171cb71-ce90-4ed0-8766-365c3d97ea78" />
<img width="475" height="284" alt="Screenshot 2026-03-07 025735" src="https://github.com/user-attachments/assets/4dd76635-d919-417a-a288-45f21af2dc4d" />
<img width="970" height="467" alt="Screenshot 2026-03-07 025810" src="https://github.com/user-attachments/assets/4576f455-ab55-4613-8c27-a9cc640f485e" />
<img width="456" height="241" alt="Screenshot 2026-03-07 025817" src="https://github.com/user-attachments/assets/4c0a008e-80f0-4763-8a88-14e3e74cc296" />


##  Quick Start

```bash
# 1. cd Python-Advanced
python -m venv venv
venv\Scripts\activate      

# 2. Install Dependencies
pip install -r requirements.txt

# 3. Seed Database & Run
python seed.py
python run.py
