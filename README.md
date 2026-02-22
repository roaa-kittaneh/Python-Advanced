# Python Advanced & Project Structuring 

A modular Python project demonstrating advanced OOP concepts, custom packages, and a professional virtual environment setup.

##  Features
- **Advanced OOP:** Implemented `@property`, `__iter__`, `__eq__`, `@classmethod`, and `@staticmethod`.
- **Modular Structure:** Code organized into a reusable Python package (`stu_co`).
- **Professional Environment:** Dependency management using `venv`, `pip`, and `requirements.txt`.
- **Quality Assurance:** Unit testing with `pytest` and code linting with `flake8`.

  <img width="294" height="302" alt="Screenshot 2026-02-23 013942" src="https://github.com/user-attachments/assets/37f3ee83-7088-46dd-9a52-68cdc36ad0de" />
  <img width="451" height="167" alt="Screenshot 2026-02-23 015803" src="https://github.com/user-attachments/assets/a3f14bf8-655d-415b-b502-e581095d53a8" />
  <img width="1094" height="187" alt="Screenshot 2026-02-23 020455" src="https://github.com/user-attachments/assets/d37406eb-e001-4ddc-9130-f6d39bc70fbf" />
  <img width="676" height="233" alt="Screenshot 2026-02-23 020531" src="https://github.com/user-attachments/assets/688474f9-3977-48f4-9c19-8961bdd35127" />





## 🛠️ Quick Start

```bash

cd <repository_folder_name>

#  Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # For Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests and check code quality
pytest
flake8 stu_co/
