# Email Forwarding Setup for Portfolio Contact Form

This guide explains how to set up email forwarding so that when someone submits a message through your portfolio contact form, it gets forwarded to your email address.

## Current Status

✅ **Form clearing functionality** - Implemented  
✅ **Email forwarding functionality** - Implemented  
✅ **Success/error messages** - Implemented  
✅ **Auto-reply to sender** - Implemented  

## How It Works

1. **User submits contact form** → Message is saved to database
2. **Email is sent to you** → You receive a formatted email with the message details
3. **Auto-reply sent to user** → User gets a confirmation email
4. **Form is cleared** → User is redirected to a clean form
5. **Success message shown** → User sees confirmation that their message was sent

## Setup Instructions

### Option 1: Development (Console Backend)

For development/testing, emails will be printed to your console/terminal:

```python
# In settings.py (already configured)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

**Pros:** No configuration needed, see emails in terminal  
**Cons:** Emails don't actually get sent to your inbox

### Option 2: Production with Gmail

1. **Enable 2-Factor Authentication** on your Google account
2. **Generate an App Password:**
   - Go to [Google Account Settings](https://myaccount.google.com/)
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. **Update settings.py:**

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use the generated app password
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
DEFAULT_TO_EMAIL = 'your-email@gmail.com'
```

### Option 3: Production with Outlook/Hotmail

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@outlook.com'
EMAIL_HOST_PASSWORD = 'your-password'
DEFAULT_FROM_EMAIL = 'your-email@outlook.com'
DEFAULT_TO_EMAIL = 'your-email@outlook.com'
```

### Option 4: Other Email Providers

Check your email provider's SMTP settings and adjust accordingly. Common settings:

- **Yahoo:** `smtp.mail.yahoo.com`, port 587
- **ProtonMail:** `127.0.0.1`, port 1025 (requires bridge)
- **Custom SMTP:** Check with your hosting provider

## Email Content

### Email Sent to You
- **Subject:** "Portfolio Contact Form: Message from [Name]"
- **Content:** Name, email, date, and message from the contact form
- **From:** The person who filled out the form
- **To:** Your email address

### Auto-Reply to User
- **Subject:** "Thank you for contacting me"
- **Content:** Confirmation that you received their message
- **From:** Your email address
- **To:** The person who contacted you

## Testing

1. **Start your Django server:** `python manage.py runserver`
2. **Go to contact page** and submit a test message
3. **Check console/terminal** for email output (development mode)
4. **Check your email inbox** (production mode)

## Troubleshooting

### Common Issues

1. **"Authentication failed"**
   - Check your email/password
   - For Gmail, use App Password, not regular password
   - Enable 2FA if using Gmail

2. **"Connection refused"**
   - Check SMTP host and port
   - Verify firewall settings
   - Check if your email provider blocks SMTP

3. **"SSL/TLS required"**
   - Set `EMAIL_USE_TLS = True`
   - Try port 587 instead of 465

### Debug Mode

Enable debug logging in settings.py:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.core.mail': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

## Security Notes

- **Never commit real passwords** to version control
- **Use environment variables** for sensitive data in production
- **App passwords are safer** than regular passwords
- **Consider rate limiting** contact form submissions

## Next Steps

1. **Choose your email provider** and update settings.py
2. **Test the functionality** with a real email
3. **Customize email templates** if needed
4. **Deploy to production** with proper email settings

## Support

If you encounter issues:
1. Check the Django error logs
2. Verify your email provider's SMTP settings
3. Test with a simple email client first
4. Check firewall and network settings
