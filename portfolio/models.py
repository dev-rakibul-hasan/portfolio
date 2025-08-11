from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100, default='Md. Rakibul Hasan')
    title = models.CharField(max_length=200, default='Ethical Hacker | Junior Penetration Tester | Programmer | Django Developer')
    about = models.TextField(default='I am an ethical hacker and programmer with strong expertise in web application security, penetration testing, and backend development.')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    email = models.EmailField(default='pentester.rakib@gmail.com')
    secondary_email = models.EmailField(default='pentester.rakib@outlook.com', blank=True, help_text='Secondary email address')
    phone = models.CharField(max_length=20, default='+8801309598979', help_text='Phone number with country code')
    whatsapp = models.CharField(max_length=20, default='+8801309598979', help_text='WhatsApp number with country code')
    location = models.CharField(max_length=100, default='Rangpur, Bangladesh')
    github_url = models.URLField(default='https://github.com/dev-rakibul-hasan')
    linkedin_url = models.URLField(default='https://www.linkedin.com/in/dev-rakibul-hasan/')
    facebook_url = models.URLField(default='https://www.facebook.com/HasanRakib.Dev')
    x_url = models.URLField(default='https://x.com/PentesterRakib', blank=True, help_text='X (Twitter) profile URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Profile Settings"
        verbose_name_plural = "Profile Settings"

class Skill(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner (0-30%)'),
        ('Intermediate', 'Intermediate (31-60%)'),
        ('Advanced', 'Advanced (61-80%)'),
        ('Expert', 'Expert (81-100%)'),
    ]
    
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=50, help_text='Skill level percentage (0-100)')
    category = models.CharField(max_length=100, default='General', help_text='e.g., Programming, Cybersecurity, Tools')
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.level}%)"
    
    class Meta:
        ordering = ['-level', 'name']

class Project(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High Priority'),
        ('Medium', 'Medium Priority'),
        ('Low', 'Low Priority'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True, help_text='Live demo URL')
    tags = models.CharField(max_length=200, help_text='Comma-separated tags')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    featured = models.BooleanField(default=False, help_text='Show on homepage')
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    technologies = models.TextField(blank=True, help_text='Technologies used (one per line)')
    
    def __str__(self):
        return self.title
    
    def get_tags(self):
        """Return a list of tags split by comma"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []
    
    def get_technologies(self):
        """Return a list of technologies"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split('\n') if tech.strip()]
        return []
    
    class Meta:
        ordering = ['-featured', '-created_date']

class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    verification_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, help_text='Brief description of the certification')
    
    def __str__(self):
        return f"{self.title} - {self.organization}"
    
    class Meta:
        ordering = ['-issue_date']

class Experience(models.Model):
    EXPERIENCE_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('contract', 'Contract'),
        ('volunteer', 'Volunteer'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences', help_text='Profile this experience belongs to')
    title = models.CharField(max_length=200, help_text='Job title or role')
    company = models.CharField(max_length=200, help_text='Company or organization name')
    location = models.CharField(max_length=100, blank=True, help_text='City, Country')
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPE_CHOICES, default='full_time')
    start_date = models.DateField(help_text='Start date of the experience')
    end_date = models.DateField(blank=True, null=True, help_text='End date (leave blank if current)')
    is_current = models.BooleanField(default=False, help_text='Check if this is your current position')
    description = models.TextField(help_text='Detailed description of your role and achievements')
    technologies = models.TextField(blank=True, help_text='Technologies, tools, and skills used (one per line)')
    achievements = models.TextField(blank=True, help_text='Key achievements and accomplishments (one per line)')
    company_logo = models.ImageField(upload_to='experience/', blank=True, null=True, help_text='Company logo or image')
    company_website = models.URLField(blank=True, null=True, help_text='Company website URL')
    featured = models.BooleanField(default=False, help_text='Feature this experience prominently')
    priority = models.IntegerField(default=0, help_text='Display order (higher numbers appear first)')
    
    def __str__(self):
        if self.is_current:
            return f"{self.title} at {self.company} (Current)"
        return f"{self.title} at {self.company}"
    
    def get_technologies(self):
        """Return a list of technologies"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split('\n') if tech.strip()]
        return []
    
    def get_achievements(self):
        """Return a list of achievements"""
        if self.achievements:
            return [achievement.strip() for achievement in self.achievements.split('\n') if achievement.strip()]
        return []
    
    def duration_display(self):
        """Return formatted duration string"""
        if self.is_current:
            return f"{self.start_date.strftime('%b %Y')} - Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        return f"{self.start_date.strftime('%b %Y')} - Present"
    
    class Meta:
        ordering = ['-priority', '-start_date']
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField(help_text='Use the rich text editor for formatting')
    excerpt = models.TextField(max_length=300, blank=True, help_text='Brief description for blog listing')
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=200, blank=True, help_text='Comma-separated tags')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    featured = models.BooleanField(default=False, help_text='Feature on homepage')
    read_time = models.IntegerField(default=5, help_text='Estimated read time in minutes')
    
    def __str__(self):
        return self.title
    
    def get_tags(self):
        """Return a list of tags split by comma"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []
    
    class Meta:
        ordering = ['-featured', '-publish_date']

class AboutPage(models.Model):
    """Model for managing about page content dynamically"""
    hero_title = models.CharField(max_length=200, default='About Me', help_text='Main title for the about page')
    hero_subtitle = models.TextField(default='I am an ethical hacker, programmer, and developer passionate about building secure and scalable applications. I love learning new technologies and solving challenging problems that make a real impact.', help_text='Subtitle text below the main title')
    
    # Journey Section
    journey_title = models.CharField(max_length=200, default='My Journey', help_text='Title for the journey section')
    journey_content = models.TextField(default='I am a Computer Science and Engineering student passionate about ethical hacking, web security, and backend development.', help_text='Main journey description')
    
    # Quick Facts Section
    quick_facts_title = models.CharField(max_length=200, default='Quick Facts', help_text='Title for the quick facts section')
    fact_1 = models.CharField(max_length=200, default='Junior Penetration Tester Intern at Bytecapsule IT', help_text='First quick fact')
    fact_2 = models.CharField(max_length=200, default='CSE Student at Begum Rokeya University', help_text='Second quick fact')
    fact_3 = models.CharField(max_length=200, default='Django Developer & Security Specialist', help_text='Third quick fact')
    fact_4 = models.CharField(max_length=200, default='IoT Security Researcher', help_text='Fourth quick fact')
    
    # Skills Section
    skills_title = models.CharField(max_length=200, default='Technical Skills', help_text='Title for the skills section')
    
    # Experience Section
    experience_title = models.CharField(max_length=200, default='Experience', help_text='Title for the experience section')
    
    # Meta
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"About Page Content (Last updated: {self.last_updated.strftime('%B %d, %Y')})"
    
    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
    
    def get_facts_list(self):
        """Return a list of facts for easy iteration"""
        return [self.fact_1, self.fact_2, self.fact_3, self.fact_4]


class Education(models.Model):
    """Model for managing education details"""
    DEGREE_CHOICES = [
        ('bsc', 'BSc'),
        ('msc', 'MSc'),
        ('phd', 'PhD'),
        ('diploma', 'Diploma'),
        ('certificate', 'Certificate'),
        ('other', 'Other'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education', help_text='Profile this education belongs to')
    degree = models.CharField(max_length=200, help_text='Degree or qualification name')
    institution = models.CharField(max_length=200, help_text='Institution or university name')
    location = models.CharField(max_length=100, blank=True, help_text='City, Country')
    start_date = models.DateField(help_text='Start date')
    end_date = models.DateField(blank=True, null=True, help_text='End date (leave blank if current)')
    is_current = models.BooleanField(default=False, help_text='Check if this is your current education')
    description = models.TextField(blank=True, help_text='Additional details about your education')
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, help_text='GPA if applicable')
    achievements = models.TextField(blank=True, help_text='Notable achievements, awards, or activities')
    degree_type = models.CharField(max_length=20, choices=DEGREE_CHOICES, default='bsc', help_text='Type of degree')
    featured = models.BooleanField(default=False, help_text='Feature this education prominently')
    priority = models.IntegerField(default=0, help_text='Display order (higher numbers appear first)')
    
    def __str__(self):
        if self.is_current:
            return f"{self.degree} at {self.institution} (Current)"
        return f"{self.degree} at {self.institution}"
    
    def duration_display(self):
        """Return formatted duration string"""
        if self.is_current:
            return f"{self.start_date.strftime('%Y')} – Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%Y')} – {self.end_date.strftime('%Y')}"
        return f"{self.start_date.strftime('%Y')} – Present"
    
    class Meta:
        ordering = ['-priority', '-start_date']
        verbose_name = "Education"
        verbose_name_plural = "Education"


class Language(models.Model):
    """Model for managing language skills"""
    PROFICIENCY_CHOICES = [
        ('native', 'Native'),
        ('fluent', 'Fluent'),
        ('professional', 'Professional Proficiency'),
        ('intermediate', 'Intermediate'),
        ('basic', 'Basic'),
        ('beginner', 'Beginner'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages', help_text='Profile this language belongs to')
    name = models.CharField(max_length=100, help_text='Language name')
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate', help_text='Proficiency level')
    description = models.TextField(blank=True, help_text='Additional details about your language skills')
    featured = models.BooleanField(default=False, help_text='Feature this language prominently')
    priority = models.IntegerField(default=0, help_text='Display order (higher numbers appear first)')
    
    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"
    
    class Meta:
        ordering = ['-priority', 'name']
        verbose_name = "Language"
        verbose_name_plural = "Languages"


class Achievement(models.Model):
    """Model for managing achievements, awards, and competitions"""
    ACHIEVEMENT_TYPE_CHOICES = [
        ('award', 'Award'),
        ('competition', 'Competition'),
        ('certification', 'Certification'),
        ('publication', 'Publication'),
        ('presentation', 'Presentation'),
        ('project', 'Project'),
        ('other', 'Other'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='achievements', help_text='Profile this achievement belongs to')
    title = models.CharField(max_length=200, help_text='Achievement title')
    description = models.TextField(help_text='Description of the achievement')
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPE_CHOICES, default='award', help_text='Type of achievement')
    organization = models.CharField(max_length=200, blank=True, help_text='Organization or institution')
    date = models.DateField(help_text='Date of achievement')
    certificate_image = models.ImageField(upload_to='achievements/', blank=True, null=True, help_text='Certificate or award image')
    url = models.URLField(blank=True, null=True, help_text='Related URL or verification link')
    featured = models.BooleanField(default=False, help_text='Feature this achievement prominently')
    priority = models.IntegerField(default=0, help_text='Display order (higher numbers appear first)')
    
    def __str__(self):
        return f"{self.title} - {self.organization or self.achievement_type.title()}"
    
    class Meta:
        ordering = ['-priority', '-date']
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
