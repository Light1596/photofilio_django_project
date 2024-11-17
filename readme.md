# Photos Django Project

**Photos** is a Django-based web application designed to showcase photography portfolios. The main app, **Photofolio**, allows users to upload, manage, and display images in a visually appealing gallery. This README will guide you through setting up the project locally.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

---

## Prerequisites
Make sure you have the following installed on your system:
- Python (>= 3.8)
- Django (>= 4.0)
- Pip
- Virtualenv (optional but recommended)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Light1596/photofilio_django_project.git
   cd photofilio_django_project
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows, use `venv\Scripts\activate`
   ```

3. **Install django if not already installed**
   ```bash
   pip install django
   ```


## Running the Project
**Run the Development Server**
   ```bash
   python manage.py runserver
   ```

4. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the application.

## Project Structure

The project structure follows Django’s standard structure:
```plaintext
photofilio_django_project/
├── photos/               # Main project folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   └── ...
├── photofolio/           # Main app for managing images
│   ├── models.py         # Database models
│   ├── views.py          # Application logic
│   ├── templates/        # HTML templates
│   └── ...          
├── manage.py             # Django management script
└── static/               # Static files (CSS, JS, images)
```

## Contributing

If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

