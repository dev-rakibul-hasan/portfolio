# Email Configuration Example for Portfolio Contact Form
# Copy the settings you want to use to your settings.py file

# For Development (emails print to console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For Production with Gmail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'
# DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
# DEFAULT_TO_EMAIL = 'your-email@gmail.com'

# For Production with Outlook/Hotmail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp-mail.outlook.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@outlook.com'
# EMAIL_HOST_PASSWORD = 'your-password'
# DEFAULT_FROM_EMAIL = 'your-email@outlook.com'
# DEFAULT_TO_EMAIL = 'your-email@outlook.com'

# For Production with other providers
# Check your email provider's SMTP settings and adjust accordingly

# Gmail Setup Instructions:
# 1. Enable 2-factor authentication on your Google account
# 2. Generate an App Password: https://myaccount.google.com/apppasswords
# 3. Use the App Password instead of your regular password
# 4. Make sure "Less secure app access" is enabled (if using regular password)

# After configuring, restart your Django server for changes to take effect
