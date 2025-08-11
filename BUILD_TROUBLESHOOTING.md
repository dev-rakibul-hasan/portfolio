# 🚨 **Build Troubleshooting Guide for Render**

## **❌ Common Build Errors & Solutions**

### **1. psycopg2 Build Error (Python 3.13)**
```
error: subprocess-exited-with-error
× Getting requirements to build wheel did not run successfully.
```

**Solution**: The build script now automatically detects Python 3.13 and uses compatible requirements.

### **2. Database Driver Issues**
```
ModuleNotFoundError: No module named 'psycopg2'
```

**Solutions**:
- ✅ **Automatic**: Build script tries multiple psycopg2 versions
- ✅ **Fallback**: Uses asyncpg for Python 3.13
- ✅ **Manual**: Add `psycopg2-binary>=2.9.7` to requirements

### **3. Python Version Compatibility**
```
SyntaxError: invalid syntax
```

**Solutions**:
- ✅ **requirements.txt**: Standard Python 3.8+ compatibility
- ✅ **requirements-py3.13.txt**: Python 3.13 specific
- ✅ **requirements-simple.txt**: Minimal dependencies

## **🔧 Build Script Features**

### **Smart Dependency Installation**
```bash
# Tries multiple approaches:
1. Standard requirements.txt
2. Python 3.13 specific requirements
3. Simple requirements
4. Minimal manual installation
```

### **Database Driver Fallbacks**
```bash
# Tries multiple psycopg2 versions:
1. psycopg2-binary>=2.9.7
2. psycopg2-binary>=2.9.6
3. asyncpg (Python 3.13)
```

## **📋 Render Configuration**

### **Build Command**
```bash
./build.sh
```

### **Start Command**
```bash
gunicorn portfolio_site.wsgi:application
```

### **Environment Variables**
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
DATABASE_URL=postgresql://... (auto-provided)
```

## **🚀 Quick Fixes**

### **If Build Still Fails:**
1. **Check Python Version**: Render might be using Python 3.13
2. **Use Simple Requirements**: Try `requirements-simple.txt`
3. **Manual Installation**: Let build script handle dependencies
4. **Check Logs**: Look for specific error messages

### **Database Issues:**
1. **PostgreSQL Service**: Ensure it's created and connected
2. **Migration Errors**: Check if models are compatible
3. **Connection Issues**: Verify DATABASE_URL format

## **📞 Getting Help**

### **Render Support**
- **Documentation**: [docs.render.com](https://docs.render.com)
- **Community**: [community.render.com](https://community.render.com)

### **Django Support**
- **Documentation**: [docs.djangoproject.com](https://docs.djangoproject.com)
- **Stack Overflow**: Tag with `django` and `render`

---

**Your build should now work automatically! 🎉**
