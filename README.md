# 🚀 **Md. Rakibul Hasan - Portfolio Website**

A modern, responsive portfolio website built with Django, featuring dynamic content management, dark/light mode, and professional design.

## ✨ **Features**

- **🎨 Modern Design**: Clean, professional interface with dark/light mode toggle
- **📱 Responsive**: Mobile-first design that works on all devices
- **⚡ Dynamic Content**: All content managed through Django admin panel
- **📧 Contact Form**: Working contact form with email notifications
- **🔐 Admin Panel**: Enhanced Django admin with custom styling
- **📊 Dynamic Sections**: Projects, skills, achievements, experience, and more
- **🌐 SEO Optimized**: Meta tags, structured data, and performance optimized

## 🛠️ **Tech Stack**

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Database**: PostgreSQL (production), SQLite (development)
- **Email**: Gmail SMTP with background processing
- **Deployment**: Render (production-ready configuration)
- **Static Files**: WhiteNoise for production optimization

## 🚀 **Quick Start (Development)**

### **Prerequisites**
- Python 3.8+
- pip
- Git

### **Installation**
```bash
# Clone the repository
git clone <your-repo-url>
cd portfolio

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### **Access Points**
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🌐 **Deploy to Render**

### **1. Push to GitHub**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### **2. Deploy on Render**
1. Go to [render.com](https://render.com)
2. Create new **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn portfolio_site.wsgi:application`
   - **Environment**: Python 3

### **3. Environment Variables**
Add these in Render:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

### **4. Database Setup**
1. Create **PostgreSQL** service in Render
2. Connect it to your web service
3. Render will provide `DATABASE_URL` automatically

## 📁 **Project Structure**

```
portfolio/
├── portfolio/                 # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── admin.py             # Admin panel customization
│   ├── templates/           # HTML templates
│   └── static/              # CSS, JS, images
├── portfolio_site/          # Django project settings
│   ├── settings.py          # Main settings file
│   ├── urls.py              # URL configuration
│   └── wsgi.py              # WSGI application
├── requirements.txt          # Python dependencies
├── build.sh                 # Render build script
├── env_template.txt         # Environment variables template
└── README.md                # This file
```

## 🔧 **Configuration**

### **Email Setup**
1. Enable 2-factor authentication on Gmail
2. Generate App Password
3. Update environment variables

### **Admin Panel**
- Enhanced with custom styling
- Bulk actions for projects and experience
- Image previews and rich text editing
- Organized fieldsets and filters

### **Content Management**
- **Profile**: Personal information and social links
- **Projects**: Portfolio projects with images and links
- **Skills**: Technical skills with proficiency levels
- **Experience**: Work history and achievements
- **Achievements**: Awards, certifications, and competitions
- **Blog**: Blog posts with rich text editor

## 🎨 **Customization**

### **Styling**
- Modify `portfolio/static/portfolio/css/styles.css`
- Update Tailwind classes in templates
- Customize admin panel in `portfolio/static/admin/css/custom_admin.css`

### **Content**
- All content managed through Django admin
- No need to edit code for content changes
- Rich text editor for blog posts and descriptions

## 📱 **Responsive Design**

- **Mobile-first approach**
- **Dark/light mode toggle**
- **Smooth animations and transitions**
- **Optimized for all screen sizes**

## 🔒 **Security Features**

- **CSRF protection**
- **XSS prevention**
- **HTTPS enforcement (production)**
- **Environment variable configuration**
- **Secure admin panel**

## 🚨 **Troubleshooting**

### **Common Issues**

#### **Build Fails on Render**
- Check `requirements.txt` syntax
- Verify Python version compatibility
- Check build logs for errors

#### **Static Files Not Loading**
- Ensure `build.sh` runs `collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` settings
- Verify whitenoise middleware

#### **Database Errors**
- Check `DATABASE_URL` format
- Ensure PostgreSQL service is running
- Verify database permissions

#### **Email Not Working**
- Check Gmail app password
- Verify SMTP settings
- Check environment variables

### **Debug Mode**
If needed, temporarily set `DEBUG=True` to see detailed error messages.

## 📞 **Support**

- **Documentation**: Check the deployment guides in this repository
- **Issues**: Create GitHub issues for bugs or feature requests
- **Community**: Django forums, Stack Overflow

## 📄 **License**

This project is open source and available under the [MIT License](LICENSE).

## 🙏 **Acknowledgments**

- Django community for the excellent framework
- Tailwind CSS for the utility-first CSS framework
- Render for the hosting platform
- All contributors and supporters

---

**Built with ❤️ by Md. Rakibul Hasan**

*Ethical Hacker | Jr Penetration Tester | Programmer | Django Developer*