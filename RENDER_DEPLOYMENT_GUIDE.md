# 🚀 **Deploy Your Django Portfolio to Render - Complete Guide**

## **📋 Prerequisites**
- GitHub account with your portfolio code
- Render account (free tier available)
- Gmail account for email functionality

## **🔧 Step 1: Prepare Your Code**

### **1.1 Update requirements.txt**
Your `requirements.txt` is already updated with production dependencies:
- Django 4.2.7
- Pillow for image handling
- django-ckeditor for rich text editing
- whitenoise for static files
- gunicorn for production server
- psycopg2-binary for PostgreSQL
- python-decouple for environment variables
- dj-database-url for database configuration

### **1.2 Build Script**
The `build.sh` script is ready and will:
- Install dependencies
- Collect static files
- Run database migrations

### **1.3 Production Settings**
Your Django settings are configured for production with:
- Environment variable support
- PostgreSQL database support
- Security headers
- Static file optimization
- Production logging

## **🌐 Step 2: Deploy to Render**

### **2.1 Create Render Account**
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Verify your email

### **2.2 Create New Web Service**
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select your portfolio repository

### **2.3 Configure Web Service**

#### **Basic Settings:**
- **Name**: `your-portfolio-name`
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)

#### **Build & Deploy Settings:**
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn portfolio_site.wsgi:application`
- **Plan**: Free (or paid for more resources)

### **2.4 Environment Variables**
Add these environment variables in Render:

#### **Required:**
```
SECRET_KEY=your-very-long-random-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```

#### **Email (Optional - for contact form):**
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
DEFAULT_TO_EMAIL=your-email@gmail.com
```

#### **Database (Auto-provided by Render):**
```
DATABASE_URL=postgresql://... (Render provides this automatically)
```

### **2.5 Deploy**
1. Click "Create Web Service"
2. Wait for build to complete (5-10 minutes)
3. Your app will be available at `https://your-app-name.onrender.com`

## **🗄️ Step 3: Database Setup**

### **3.1 Create PostgreSQL Database**
1. In Render dashboard, click "New +" → "PostgreSQL"
2. Choose plan (Free tier available)
3. Connect it to your web service

### **3.2 Run Migrations**
Migrations will run automatically via `build.sh`, but you can also:
1. Go to your web service
2. Click "Shell"
3. Run: `python manage.py migrate`

### **3.3 Create Superuser**
1. In the shell, run: `python manage.py createsuperuser`
2. Follow prompts to create admin account

## **📧 Step 4: Email Configuration (Optional)**

### **4.1 Gmail App Password**
1. Enable 2-factor authentication on Google account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Generate password for "Mail"
4. Use this password in `EMAIL_HOST_PASSWORD`

### **4.2 Test Email**
1. Go to your deployed site
2. Test the contact form
3. Check if emails are sent successfully

## **🔍 Step 5: Verify Deployment**

### **5.1 Check Functionality**
- ✅ Home page loads
- ✅ Navigation works
- ✅ Contact form functions
- ✅ Admin panel accessible
- ✅ Static files load
- ✅ Images display correctly

### **5.2 Performance Check**
- ✅ Page load times
- ✅ Mobile responsiveness
- ✅ Dark/light mode toggle
- ✅ Smooth scrolling

## **🚨 Troubleshooting**

### **Common Issues:**

#### **Build Fails:**
- Check `requirements.txt` syntax
- Verify Python version compatibility
- Check build logs for errors

#### **Static Files Not Loading:**
- Ensure `build.sh` runs `collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` settings
- Verify whitenoise middleware

#### **Database Errors:**
- Check `DATABASE_URL` format
- Ensure PostgreSQL service is running
- Verify database permissions

#### **Email Not Working:**
- Check Gmail app password
- Verify SMTP settings
- Check environment variables

### **Debug Mode:**
If needed, temporarily set `DEBUG=True` to see detailed error messages.

## **🔒 Security Notes**

### **Production Security:**
- ✅ `DEBUG=False` in production
- ✅ `SECRET_KEY` is environment variable
- ✅ HTTPS enforced by Render
- ✅ Security headers enabled
- ✅ CSRF protection active

### **Environment Variables:**
- Never commit `.env` files
- Use Render's environment variable system
- Keep sensitive data out of code

## **📱 Custom Domain (Optional)**

### **Add Custom Domain:**
1. In Render dashboard, go to your web service
2. Click "Settings" → "Custom Domains"
3. Add your domain
4. Update DNS records as instructed

## **🔄 Continuous Deployment**

### **Auto-Deploy:**
- Render automatically deploys on git push
- Builds and deploys from your main branch
- No manual intervention needed

### **Manual Deploy:**
- Go to your web service
- Click "Manual Deploy"
- Choose branch to deploy

## **💰 Cost Optimization**

### **Free Tier Limits:**
- 750 hours/month (31 days)
- 512 MB RAM
- Shared CPU
- 1 GB storage

### **Upgrade When:**
- Need more resources
- Want custom domain
- Need dedicated IP
- Want faster performance

## **🎉 Success!**

Your Django portfolio is now live on Render with:
- ✅ Professional hosting
- ✅ Automatic deployments
- ✅ PostgreSQL database
- ✅ Static file optimization
- ✅ Security best practices
- ✅ Scalable infrastructure

## **📞 Support**

- **Render Docs**: [docs.render.com](https://docs.render.com)
- **Django Docs**: [docs.djangoproject.com](https://docs.djangoproject.com)
- **Community**: Stack Overflow, Django forums

---

**Happy Deploying! 🚀**
