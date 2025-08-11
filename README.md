# Portfolio Site

A dynamic personal portfolio website built with Django.

## Features
- Home, About, Projects, Certifications, Contact, Blog pages
- Dynamic content from database
- REST API for mobile apps
- Modern admin panel with dark mode
- Responsive Bootstrap 5 frontend
- Dark/Light mode toggle

## Setup Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
3. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```
4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the site**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the portfolio
   - Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) for the admin panel

## Deployment
- Uses SQLite for development
- Static/media files ready for Render or PythonAnywhere

## API Endpoints
- `/api/skills/` — List skills
- `/api/projects/` — List projects
- `/api/certifications/` — List certifications
- `/api/blogposts/` — List blog posts

---

**Customize your profile, add your CV, and update social links in the templates.**