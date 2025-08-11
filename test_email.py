#!/usr/bin/env python
"""
Test script to verify Gmail SMTP configuration
Run this after setting up your App Password to test the email functionality
"""

import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

def test_email():
    """Test sending an email through Gmail SMTP"""
    try:
        print("🧪 Testing Gmail SMTP configuration...")
        print(f"📧 Email Backend: {settings.EMAIL_BACKEND}")
        print(f"📧 SMTP Host: {settings.EMAIL_HOST}")
        print(f"📧 SMTP Port: {settings.EMAIL_PORT}")
        print(f"📧 TLS Enabled: {settings.EMAIL_USE_TLS}")
        print(f"📧 From Email: {settings.EMAIL_HOST_USER}")
        print(f"📧 To Email: {settings.DEFAULT_TO_EMAIL}")
        
        # Test email
        subject = "Portfolio Contact Form Test"
        message = """
This is a test email from your portfolio website to verify Gmail SMTP configuration.

If you receive this email, your contact form email forwarding is working correctly!

Best regards,
Your Portfolio Website
        """.strip()
        
        print("\n📤 Sending test email...")
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.DEFAULT_TO_EMAIL],
            fail_silently=False,
        )
        
        print("✅ Test email sent successfully!")
        print("📬 Check your Gmail inbox for the test message")
        
    except Exception as e:
        print(f"❌ Error sending test email: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you've replaced 'your-app-password' with your actual App Password")
        print("2. Verify 2FA is enabled on your Google account")
        print("3. Check that the App Password was generated for 'Mail'")
        print("4. Ensure your internet connection is working")

if __name__ == "__main__":
    test_email()
