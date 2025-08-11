# 🚀 **Quick Deployment Checklist**

## **✅ Pre-Deployment (Local)**
- [ ] Code committed to GitHub
- [ ] `requirements.txt` updated
- [ ] `build.sh` created and executable
- [ ] Production settings configured
- [ ] Environment variables documented

## **🌐 Render Setup**
- [ ] Create Render account
- [ ] Connect GitHub repository
- [ ] Create Web Service
- [ ] Set build command: `./build.sh`
- [ ] Set start command: `gunicorn portfolio_site.wsgi:application`

## **🔑 Environment Variables**
- [ ] `SECRET_KEY` (generate new one)
- [ ] `DEBUG=False`
- [ ] `ALLOWED_HOSTS` (your-app-name.onrender.com)
- [ ] `EMAIL_HOST_USER` (your Gmail)
- [ ] `EMAIL_HOST_PASSWORD` (Gmail app password)

## **🗄️ Database**
- [ ] Create PostgreSQL service
- [ ] Connect to web service
- [ ] Run migrations
- [ ] Create superuser

## **🧪 Testing**
- [ ] Home page loads
- [ ] Navigation works
- [ ] Contact form sends emails
- [ ] Admin panel accessible
- [ ] Static files load
- [ ] Images display

## **🔒 Security**
- [ ] `DEBUG=False` in production
- [ ] HTTPS working
- [ ] Admin panel accessible
- [ ] No sensitive data in code

## **📱 Final Steps**
- [ ] Test on mobile
- [ ] Check performance
- [ ] Update README with live URL
- [ ] Share your portfolio! 🎉

---

**Your portfolio will be live at: `https://your-app-name.onrender.com`**
