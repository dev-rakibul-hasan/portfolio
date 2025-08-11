# Gmail Setup for Portfolio Contact Form

## 🚀 Quick Setup (3 Steps)

### Step 1: Enable 2-Factor Authentication
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Click **Security** → **2-Step Verification**
3. Follow the steps to enable 2FA

### Step 2: Generate App Password
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Click **Security** → **2-Step Verification** → **App passwords**
3. Select **Mail** from the dropdown
4. Click **Generate**
5. **Copy the 16-character password** (e.g., `abcd efgh ijkl mnop`)

### Step 3: Update Your Settings
1. Open `portfolio_site/settings.py`
2. Find this line:
   ```python
   EMAIL_HOST_PASSWORD = 'your-app-password'
   ```
3. Replace `'your-app-password'` with your actual App Password:
   ```python
   EMAIL_HOST_PASSWORD = 'abcdefghijklmnop'
   ```
4. Save the file
5. Restart your Django server

## ✅ What Happens Next

- **Contact form submissions** → Forwarded to `pentester.rakib@gmail.com`
- **Auto-reply emails** → Sent from `pentester.rakib@gmail.com` to the person who contacted you
- **All emails** → Sent through Gmail's secure SMTP server

## 🔒 Security Notes

- ✅ **App Password is safe** - Can only be used for email
- ✅ **2FA required** - Protects your main account
- ❌ **Never use regular password** - Will not work and is unsafe
- ❌ **Don't share App Password** - Keep it private

## 🧪 Testing

1. **Start server:** `python manage.py runserver`
2. **Go to contact page** and submit a test message
3. **Check your Gmail inbox** for the forwarded message
4. **Check your Gmail sent folder** for the auto-reply

## 🆘 Troubleshooting

### "Authentication failed"
- Make sure you're using the **App Password**, not your regular password
- Verify 2FA is enabled
- Check that the App Password was copied correctly

### "Connection refused"
- Check your internet connection
- Verify firewall isn't blocking port 587
- Try again in a few minutes

### "SSL/TLS required"
- Settings are already correct (TLS enabled, port 587)
- This error shouldn't occur with current configuration

## 📱 Mobile Access

The App Password works on all devices and email clients. You can use it with:
- Gmail app
- Outlook app
- Thunderbird
- Any email client that supports SMTP

## 🔄 Regenerating App Password

If you need a new App Password:
1. Go to [App Passwords](https://myaccount.google.com/apppasswords)
2. Click the trash icon next to the old one
3. Generate a new one
4. Update your `settings.py` file
5. Restart Django server

---

**Need help?** Check the main `EMAIL_SETUP_README.md` for more detailed troubleshooting.
