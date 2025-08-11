from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.admin import AdminSite
from .models import Profile, Skill, Project, Certification, Message, BlogPost, Experience, AboutPage, Education, Language, Achievement

# Customize admin site headers and styling
admin.site.site_header = "Md. Rakibul Hasan - Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"

# Custom admin site class for better organization
class PortfolioAdminSite(AdminSite):
    site_header = "Md. Rakibul Hasan - Portfolio Admin"
    site_title = "Portfolio Admin"
    index_title = "Portfolio Management Dashboard"
    site_url = "/"

# Register the custom admin site
portfolio_admin = PortfolioAdminSite(name='portfolio_admin')

# Add custom CSS for better admin styling
class Media:
    css = {
        'all': ('admin/css/custom_admin.css',)
    }

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'about', 'profile_image', 'cv_file')
        }),
        ('Contact Information', {
            'fields': ('email', 'secondary_email', 'phone', 'whatsapp', 'location')
        }),
        ('Social Media', {
            'fields': ('github_url', 'linkedin_url', 'facebook_url', 'x_url'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['preview_profile_image']
    
    def preview_profile_image(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px; border-radius: 10px;" />', obj.profile_image.url)
        return "No image uploaded"
    preview_profile_image.short_description = "Profile Image Preview"

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category', 'colored_level', 'preview_icon']
    list_filter = ['category', 'level']
    search_fields = ['name', 'category']
    list_editable = ['level', 'category']
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'level', 'category')
        }),
        ('Visual', {
            'fields': ('icon', 'preview_icon')
        }),
    )
    readonly_fields = ['preview_icon']
    
    def colored_level(self, obj):
        if obj.level >= 80:
            color = '#10B981'  # Green
        elif obj.level >= 60:
            color = '#F59E0B'  # Yellow
        elif obj.level >= 40:
            color = '#EF4444'  # Orange
        else:
            color = '#6B7280'  # Gray
        return format_html('<span style="color: {}; font-weight: bold;">{}%</span>', color, obj.level)
    colored_level.short_description = "Level"
    
    def preview_icon(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.icon.url)
        return "No icon"
    preview_icon.short_description = "Icon Preview"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'featured', 'created_date', 'preview_image', 'tags_preview']
    list_filter = ['priority', 'featured', 'created_date', 'tags']
    search_fields = ['title', 'description', 'tags', 'technologies']
    list_editable = ['priority', 'featured']
    prepopulated_fields = {'tags': ('title',)}
    ordering = ['-created_date', 'priority']
    list_per_page = 20
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'image', 'preview_image'),
            'classes': ('wide',)
        }),
        ('Links', {
            'fields': ('github_link', 'live_link'),
            'classes': ('wide',)
        }),
        ('Classification', {
            'fields': ('tags', 'technologies', 'priority', 'featured'),
            'classes': ('wide',)
        }),
        ('Advanced Settings', {
            'fields': ('created_date',),
            'classes': ('collapse',),
            'description': 'Advanced project settings and metadata'
        }),
    )
    
    readonly_fields = ['preview_image', 'created_date', 'tags_preview']
    
    # Add actions for bulk operations
    actions = ['make_featured', 'remove_featured', 'set_high_priority', 'set_medium_priority', 'set_low_priority']
    
    def tags_preview(self, obj):
        if obj.tags:
            tags_list = obj.tags.split(',')[:3]  # Show first 3 tags
            return format_html('<span style="background: #e5e7eb; padding: 2px 8px; border-radius: 12px; font-size: 11px; margin: 1px;">{}</span>', 
                             '</span> <span style="background: #e5e7eb; padding: 2px 8px; border-radius: 12px; font-size: 11px; margin: 1px;">'.join(tags_list))
        return "No tags"
    tags_preview.short_description = "Tags"
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px; border-radius: 5px; border: 1px solid #ddd;" />', obj.image.url)
        return format_html('<div style="width: 150px; height: 100px; background: #f3f4f6; border: 1px solid #ddd; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: #6b7280;">No Image</div>')
    preview_image.short_description = "Image Preview"
    
    # Bulk action methods
    def make_featured(self, request, queryset):
        updated = queryset.update(featured=True)
        self.message_user(request, f'{updated} project(s) marked as featured.')
    make_featured.short_description = "Mark selected projects as featured"
    
    def remove_featured(self, request, queryset):
        updated = queryset.update(featured=False)
        self.message_user(request, f'{updated} project(s) removed from featured.')
    remove_featured.short_description = "Remove selected projects from featured"
    
    def set_high_priority(self, request, queryset):
        updated = queryset.update(priority='High')
        self.message_user(request, f'{updated} project(s) set to high priority.')
    set_high_priority.short_description = "Set priority to High"
    
    def set_medium_priority(self, request, queryset):
        updated = queryset.update(priority='Medium')
        self.message_user(request, f'{updated} project(s) set to medium priority.')
    set_medium_priority.short_description = "Set priority to Medium"
    
    def set_low_priority(self, request, queryset):
        updated = queryset.update(priority='Low')
        self.message_user(request, f'{updated} project(s) set to low priority.')
    set_low_priority.short_description = "Set priority to Low"

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'issue_date', 'expiry_date', 'preview_certificate']
    list_filter = ['organization', 'issue_date']
    search_fields = ['title', 'organization', 'credential_id']
    date_hierarchy = 'issue_date'
    fieldsets = (
        ('Certification Details', {
            'fields': ('title', 'organization', 'description')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date')
        }),
        ('Verification', {
            'fields': ('credential_id', 'verification_url')
        }),
        ('Certificate Image', {
            'fields': ('certificate_image', 'preview_certificate')
        }),
    )
    readonly_fields = ['preview_certificate']
    
    def preview_certificate(self, obj):
        if obj.certificate_image:
            return format_html('<img src="{}" style="max-height: 150px; max-width: 200px; border-radius: 5px;" />', obj.certificate_image.url)
        return "No certificate image"
    preview_certificate.short_description = "Certificate Preview"

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sent_at', 'message_preview']
    list_filter = ['sent_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['sent_at']
    date_hierarchy = 'sent_at'
    
    def message_preview(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_preview.short_description = "Message Preview"

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'category', 'publish_date', 'read_time', 'preview_image']
    list_filter = ['status', 'featured', 'category', 'publish_date']
    search_fields = ['title', 'content', 'tags']
    list_editable = ['status', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_date'
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Media', {
            'fields': ('featured_image', 'preview_image')
        }),
        ('Classification', {
            'fields': ('category', 'tags', 'read_time')
        }),
        ('Publishing', {
            'fields': ('status', 'featured', 'author')
        }),
        ('Dates', {
            'fields': ('publish_date', 'updated_date')
        }),
    )
    readonly_fields = ['preview_image', 'publish_date', 'updated_date']
    
    def preview_image(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px; border-radius: 5px;" />', obj.featured_image.url)
        return "No featured image"
    preview_image.short_description = "Featured Image Preview"

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'experience_type', 'start_date', 'end_date', 'is_current', 'featured', 'priority', 'preview_logo']
    list_filter = ['experience_type', 'is_current', 'featured', 'start_date', 'company']
    search_fields = ['title', 'company', 'description', 'technologies', 'achievements']
    list_editable = ['featured', 'priority', 'is_current']
    ordering = ['-priority', '-start_date']
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'location', 'experience_type'),
            'classes': ('wide',)
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current'),
            'classes': ('wide',)
        }),
        ('Description & Achievements', {
            'fields': ('description', 'achievements'),
            'classes': ('wide',),
            'description': 'Describe your role, responsibilities, and key achievements'
        }),
        ('Technologies & Skills', {
            'fields': ('technologies',),
            'classes': ('wide',),
            'description': 'List the technologies, tools, and skills you used (one per line)'
        }),
        ('Company Details', {
            'fields': ('company_logo', 'preview_logo', 'company_website'),
            'classes': ('wide',)
        }),
        ('Display Settings', {
            'fields': ('featured', 'priority'),
            'classes': ('wide',),
            'description': 'Control how this experience is displayed on your portfolio'
        }),
    )
    
    readonly_fields = ['preview_logo']
    
    # Add actions for bulk operations
    actions = ['make_featured', 'remove_featured', 'set_high_priority', 'set_medium_priority', 'set_low_priority']
    
    def preview_logo(self, obj):
        if obj.company_logo:
            return format_html(
                '<img src="{}" style="max-height: 60px; max-width: 120px; border: 2px solid #e5e7eb; border-radius: 8px; padding: 5px; background: white;" />',
                obj.company_logo.url
            )
        return format_html(
            '<div style="width: 120px; height: 60px; border: 2px dashed #d1d5db; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #6b7280; font-size: 12px; background: #f9fafb;">No Logo</div>'
        )
    preview_logo.short_description = "Company Logo"
    
    def make_featured(self, request, queryset):
        queryset.update(featured=True)
        self.message_user(request, f"{queryset.count()} experience(s) marked as featured.")
    make_featured.short_description = "Mark selected experiences as featured"
    
    def remove_featured(self, request, queryset):
        queryset.update(featured=False)
        self.message_user(request, f"{queryset.count()} experience(s) removed from featured.")
    remove_featured.short_description = "Remove selected experiences from featured"
    
    def set_high_priority(self, request, queryset):
        queryset.update(priority=3)
        self.message_user(request, f"{queryset.count()} experience(s) set to high priority.")
    set_high_priority.short_description = "Set selected experiences to high priority"
    
    def set_medium_priority(self, request, queryset):
        queryset.update(priority=2)
        self.message_user(request, f"{queryset.count()} experience(s) set to medium priority.")
    set_medium_priority.short_description = "Set selected experiences to medium priority"
    
    def set_low_priority(self, request, queryset):
        queryset.update(priority=1)
        self.message_user(request, f"{queryset.count()} experience(s) set to low priority.")
    set_low_priority.short_description = "Set selected experiences to low priority"

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'last_updated', 'content_preview']
    readonly_fields = ['last_updated']
    
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle'),
            'classes': ('wide',),
            'description': 'Main title and subtitle for the about page'
        }),
        ('Journey Section', {
            'fields': ('journey_title', 'journey_content'),
            'classes': ('wide',),
            'description': 'Personal journey and background information'
        }),
        ('Quick Facts', {
            'fields': ('quick_facts_title', 'fact_1', 'fact_2', 'fact_3', 'fact_4'),
            'classes': ('wide',),
            'description': 'Key facts and highlights about yourself'
        }),
        ('Section Titles', {
            'fields': ('skills_title', 'experience_title'),
            'classes': ('wide',),
            'description': 'Titles for different sections on the about page'
        }),
        ('Meta Information', {
            'fields': ('last_updated',),
            'classes': ('collapse',),
            'description': 'Automatically updated timestamp'
        }),
    )
    
    def content_preview(self, obj):
        """Show a preview of the content"""
        return format_html(
            '<div style="max-width: 300px;"><strong>Hero:</strong> {}<br><strong>Journey:</strong> {}...</div>',
            obj.hero_title,
            obj.journey_content[:50]
        )
    content_preview.short_description = "Content Preview"
    
    def has_add_permission(self, request):
        """Only allow one about page instance"""
        return not AboutPage.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of the about page"""
        return False

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'is_current', 'featured', 'priority', 'profile_preview']
    list_filter = ['degree_type', 'is_current', 'featured', 'start_date', 'institution']
    search_fields = ['degree', 'institution', 'description', 'achievements']
    list_editable = ['featured', 'priority', 'is_current']
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('profile', 'degree', 'institution', 'location', 'degree_type')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('description', 'gpa', 'achievements')
        }),
        ('Display Options', {
            'fields': ('featured', 'priority'),
            'classes': ('collapse',)
        }),
    )
    
    def profile_preview(self, obj):
        if obj.profile:
            return format_html('<span style="color: #666;">{}</span>', obj.profile.name)
        return "No Profile"
    profile_preview.short_description = "Profile"


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'featured', 'priority', 'profile_preview']
    list_filter = ['proficiency', 'featured']
    search_fields = ['name', 'description']
    list_editable = ['featured', 'priority', 'proficiency']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('profile', 'name', 'proficiency')
        }),
        ('Details', {
            'fields': ('description',)
        }),
        ('Display Options', {
            'fields': ('featured', 'priority'),
            'classes': ('collapse',)
        }),
    )
    
    def profile_preview(self, obj):
        if obj.profile:
            return format_html('<span style="color: #666;">{}</span>', obj.profile.name)
        return "No Profile"
    profile_preview.short_description = "Profile"


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'achievement_type', 'organization', 'date', 'featured', 'priority', 'profile_preview']
    list_filter = ['achievement_type', 'featured', 'date', 'organization']
    search_fields = ['title', 'description', 'organization']
    list_editable = ['featured', 'priority']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('profile', 'title', 'achievement_type', 'organization', 'date')
        }),
        ('Details', {
            'fields': ('description', 'url')
        }),
        ('Media', {
            'fields': ('certificate_image',),
            'classes': ('collapse',)
        }),
        ('Display Options', {
            'fields': ('featured', 'priority'),
            'classes': ('collapse',)
        }),
    )
    
    def profile_preview(self, obj):
        if obj.profile:
            return format_html('<span style="color: #666;">{}</span>', obj.profile.name)
        return "No Profile"
    profile_preview.short_description = "Profile"
