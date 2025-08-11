from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
import threading
from .models import Profile, Skill, Project, Certification, Message, BlogPost, AboutPage, Achievement
from .forms import ContactForm

def send_contact_emails_background(message, recipient_email):
    """
    Send contact form emails in the background using threading
    This function runs in a separate thread to avoid blocking the main request
    """
    try:
        # Prepare email content
        subject = f"Portfolio Contact Form: Message from {message.name}"
        
        # Create a well-formatted email body
        email_body = f"""
New message received from your portfolio contact form:

Name: {message.name}
Email: {message.email}
Date: {message.sent_at.strftime('%B %d, %Y at %I:%M %p')}

Message:
{message.message}

---
This message was sent from your portfolio website contact form.
        """.strip()
        
        # Send email to your email address
        send_mail(
            subject=subject,
            message=email_body,
            from_email=message.email,  # From the person who filled the form
            recipient_list=[recipient_email],  # To your email
            fail_silently=False,
        )
        
        # Also send a copy to the sender (optional - you can remove this if you don't want it)
        sender_confirmation_subject = "Thank you for contacting me"
        sender_confirmation_body = f"""
Dear {message.name},

Thank you for reaching out through my portfolio website. I have received your message and will get back to you as soon as possible.

Your message:
{message.message}

Best regards,
Md. Rakibul Hasan
        """.strip()
        
        try:
            send_mail(
                subject=sender_confirmation_subject,
                message=sender_confirmation_body,
                from_email=recipient_email,  # From your email
                recipient_list=[message.email],  # To the person who contacted you
                fail_silently=True,  # Don't fail if this email fails
            )
        except:
            pass  # Ignore errors for confirmation email
            
    except Exception as e:
        # Log the error for debugging (in production, you might want to use proper logging)
        print(f"Background email error: {e}")

# Create your views here.

def home(request):
    # Get profile data
    try:
        profile = Profile.objects.first()  # Get the first (and likely only) profile
    except Profile.DoesNotExist:
        profile = None
    
    # Get data for home page summary
    skills = Skill.objects.all()[:6]  # Show top 6 skills
    recent_projects = Project.objects.filter(featured=True)[:3] or Project.objects.all()[:3]  # Show featured projects first
    certifications = Certification.objects.all()[:4]  # Show 4 certifications
    recent_posts = BlogPost.objects.filter(status='published').order_by('-publish_date')[:3]  # Show 3 recent published posts
    
    context = {
        'profile': profile,
        'skills': skills,
        'recent_projects': recent_projects,
        'certifications': certifications,
        'recent_posts': recent_posts,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    # Get profile data
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    # Get about page content
    try:
        about_content = AboutPage.objects.first()
        if not about_content:
            # Create default about page content if none exists
            about_content = AboutPage.objects.create()
    except:
        about_content = None
    
    skills = Skill.objects.all()
    # Limit a few achievements for the About page preview
    achievements_preview = Achievement.objects.filter(profile=profile).order_by('-priority', '-date')[:6] if profile else []
    return render(request, 'portfolio/about.html', {
        'skills': skills, 
        'profile': profile, 
        'about': about_content,
        'achievements_preview': achievements_preview,
    })

def projects(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 6)  # 6 projects per page
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    return render(request, 'portfolio/projects.html', {'projects': projects})

def certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'portfolio/certifications.html', {
        'certifications': certifications,
    })

def contact(request):
    # Get profile data
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            
            # Get recipient email
            recipient_email = profile.email if profile and profile.email else 'pentester.rakib@gmail.com'
            
            # Send emails in background using threading
            email_thread = threading.Thread(
                target=send_contact_emails_background,
                args=(message, recipient_email)
            )
            email_thread.daemon = True  # Thread will be terminated when main process ends
            email_thread.start()
            
            # Show success message immediately (emails are being sent in background)
            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors in the form.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form, 'profile': profile})

def blog_list(request):
    posts = BlogPost.objects.order_by('-publish_date')
    return render(request, 'portfolio/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def cv_view(request):
    # Get profile data
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    projects = Project.objects.all()[:6]  # Limit to 6 projects for CV
    
    context = {
        'profile': profile,
        'skills': skills,
        'certifications': certifications,
        'projects': projects,
    }
    return render(request, 'portfolio/cv.html', context)


def achievements(request):
    """List all achievements with pagination."""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    qs = Achievement.objects.all().order_by('-priority', '-date')
    paginator = Paginator(qs, 9)
    page_number = request.GET.get('page')
    achievements_page = paginator.get_page(page_number)
    return render(request, 'portfolio/achievements.html', {
        'profile': profile,
        'achievements': achievements_page,
    })
