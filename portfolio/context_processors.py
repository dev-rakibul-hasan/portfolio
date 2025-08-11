from .models import Profile

def profile_processor(request):
    """Make profile data available globally in all templates"""
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    
    return {
        'profile': profile,
    }
