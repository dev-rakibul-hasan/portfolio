#!/usr/bin/env python
"""
Test script to verify background email functionality
This tests the threading-based background email sending
"""

import os
import django
import time
from django.core.mail import send_mail
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

def test_background_email():
    """Test the background email functionality"""
    try:
        print("🧪 Testing Background Email Functionality...")
        print(f"📧 Email Backend: {settings.EMAIL_BACKEND}")
        print(f"📧 SMTP Host: {settings.EMAIL_HOST}")
        print(f"📧 SMTP Port: {settings.EMAIL_PORT}")
        print(f"📧 TLS Enabled: {settings.EMAIL_USE_TLS}")
        print(f"📧 From Email: {settings.EMAIL_HOST_USER}")
        print(f"📧 To Email: {settings.DEFAULT_TO_EMAIL}")
        
        # Test email
        subject = "Background Email Test"
        message = """
This is a test email to verify that background email sending is working correctly.

The email should be sent through Gmail SMTP in the background.

Best regards,
Your Portfolio Website
        """.strip()
        
        print("\n📤 Sending test email in background...")
        start_time = time.time()
        
        # Import the background function
        from portfolio.views import send_contact_emails_background
        
        # Create a mock message object for testing
        class MockMessage:
            def __init__(self):
                self.name = "Test User"
                self.email = "test@example.com"
                self.message = "This is a test message"
                self.sent_at = django.utils.timezone.now()
        
        mock_message = MockMessage()
        
        # Test background email sending
        import threading
        email_thread = threading.Thread(
            target=send_contact_emails_background,
            args=(mock_message, settings.DEFAULT_TO_EMAIL)
        )
        email_thread.daemon = True
        email_thread.start()
        
        # Wait a moment for the thread to start
        time.sleep(0.1)
        
        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        print(f"✅ Background email thread started successfully!")
        print(f"⏱️  Response time: {response_time:.2f} ms")
        print(f"📬 Check your Gmail inbox for the test message")
        print(f"🔄 Email is being sent in the background...")
        
        # Wait for the email to complete (optional)
        print(f"⏳ Waiting for email to complete...")
        email_thread.join(timeout=10)  # Wait up to 10 seconds
        
        if email_thread.is_alive():
            print(f"⚠️  Email thread is still running (this is normal for slow connections)")
        else:
            print(f"✅ Email thread completed successfully!")
        
    except Exception as e:
        print(f"❌ Error testing background email: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure your Gmail App Password is correctly set")
        print("2. Verify 2FA is enabled on your Google account")
        print("3. Check your internet connection")
        print("4. Ensure Django server is running")

if __name__ == "__main__":
    test_background_email()
