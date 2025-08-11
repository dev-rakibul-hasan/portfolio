// Typewriter Animation
function typewriter(text, elementId, speed = 100) {
    const element = document.getElementById(elementId);
    const cursor = document.getElementById('typewriter-cursor');
    let i = 0;
    
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        } else {
            // Hide cursor after typing is complete
            setTimeout(() => {
                if (cursor) {
                    cursor.style.opacity = '0';
                }
            }, 1000);
        }
    }
    
    // Start typing after a small delay
    setTimeout(type, 500);
}

// Scroll-based Profile Image Movement
function handleScroll() {
    const heroProfile = document.getElementById('hero-profile');
    const headerProfile = document.getElementById('header-profile');
    const headerProfileMobile = document.getElementById('header-profile-mobile');
    const headerProfileImage = document.getElementById('header-profile-image');
    const headerProfileImageMobile = document.getElementById('header-profile-image-mobile');
    const profileImage = document.getElementById('profile-image');
    
    if (!heroProfile || !profileImage) {
        return;
    }
    
    const scrollY = window.scrollY;
    const heroSection = heroProfile.getBoundingClientRect();
    const profileImageSrc = profileImage.src;
    
    // Update header profile image sources
    if (headerProfileImage && headerProfileImage.src !== profileImageSrc) {
        headerProfileImage.src = profileImageSrc;
    }
    if (headerProfileImageMobile && headerProfileImageMobile.src !== profileImageSrc) {
        headerProfileImageMobile.src = profileImageSrc;
    }
    
    // Show header profile based on scroll position (once shown, stays visible)
    const shouldShow = scrollY > 100 || heroSection.bottom < window.innerHeight * 0.8;
    
    // Desktop header profile
    if (headerProfile && shouldShow && headerProfile.classList.contains('hidden')) {
        headerProfile.classList.remove('hidden');
        headerProfile.classList.add('animate-slide-in-right');
        setTimeout(() => {
            headerProfile.classList.add('animate-bounce-in');
        }, 300);
    }
    
    // Mobile header profile
    if (headerProfileMobile && shouldShow && headerProfileMobile.classList.contains('hidden')) {
        headerProfileMobile.classList.remove('hidden');
        headerProfileMobile.classList.add('animate-slide-in-right');
    }
}

// Smooth scroll to top when header profile is clicked
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Scroll-triggered animations for elements (faster trigger)
function animateOnScroll() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    const windowHeight = window.innerHeight;
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 50; // Reduced from 150 to 50 for faster trigger
        
        if (elementTop < windowHeight - elementVisible) {
            element.classList.add('animate-visible');
        }
    });
}

// Parallax effect for floating elements
function parallaxEffect() {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.parallax-element');
    
    parallaxElements.forEach((element, index) => {
        const speed = 0.5 + (index * 0.1);
        const yPos = -(scrolled * speed);
        element.style.transform = `translate3d(0, ${yPos}px, 0)`;
    });
}

// Smooth scroll for navigation links
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"], a[href^="/"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Handle anchor links
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}

// Header background animation on scroll + FORCE FIXED POSITION
function animateHeader() {
    const header = document.querySelector('nav');
    const scrollY = window.scrollY;
    
    if (header) {
        // FORCE header to stay fixed - override any changes
        header.style.setProperty('position', 'fixed', 'important');
        header.style.setProperty('top', '0', 'important');
        header.style.setProperty('left', '0', 'important');
        header.style.setProperty('right', '0', 'important');
        header.style.setProperty('width', '100%', 'important');
        header.style.setProperty('z-index', '99999', 'important');
        header.style.setProperty('transform', 'translateY(0)', 'important');
        header.style.setProperty('opacity', '1', 'important');
        header.style.setProperty('visibility', 'visible', 'important');
        header.style.setProperty('display', 'block', 'important');
        
        // Remove any hiding classes/attributes
        header.classList.remove('hidden', 'invisible');
        header.removeAttribute('hidden');
        
        // Scroll background effect
        if (scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
}

// Enhanced scroll handler with multiple effects
function enhancedScrollHandler() {
    handleScroll(); // Original profile animation
    animateOnScroll(); // Element animations
    parallaxEffect(); // Parallax effects
    animateHeader(); // Header animations
    
    // Add scroll progress indicator
    updateScrollProgress();
}

// Scroll progress indicator
function updateScrollProgress() {
    const scrollTop = window.pageYOffset;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    
    let progressBar = document.getElementById('scroll-progress');
    if (!progressBar) {
        progressBar = document.createElement('div');
        progressBar.id = 'scroll-progress';
        progressBar.className = 'scroll-progress';
        document.body.appendChild(progressBar);
    }
    
    progressBar.style.width = scrollPercent + '%';
}

// Original typewriter animation
function typewriter(text, elementId, speed = 100) {
    const element = document.getElementById(elementId);
    const cursor = document.getElementById('typewriter-cursor');
    let i = 0;
    
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        } else {
            // Hide cursor after typing is complete
            setTimeout(() => {
                if (cursor) {
                    cursor.style.opacity = '0';
                }
            }, 1000);
        }
    }
    
    // Start typing after a small delay
    setTimeout(type, 500);
}

// Force header fixed immediately
function forceHeaderFixed() {
    const header = document.querySelector('nav');
    if (header) {
        header.style.setProperty('position', 'fixed', 'important');
        header.style.setProperty('top', '0', 'important');
        header.style.setProperty('left', '0', 'important');
        header.style.setProperty('right', '0', 'important');
        header.style.setProperty('width', '100%', 'important');
        header.style.setProperty('z-index', '99999', 'important');
        header.style.setProperty('transform', 'translateY(0)', 'important');
        header.style.setProperty('opacity', '1', 'important');
        header.style.setProperty('visibility', 'visible', 'important');
        header.style.setProperty('display', 'block', 'important');
        header.classList.remove('hidden', 'invisible');
        header.removeAttribute('hidden');
    }
}

// Initialize animations when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // IMMEDIATELY force header to be fixed
    forceHeaderFixed();
    
    // Get the name from the template (fallback if no profile)
    const nameElement = document.querySelector('h1 span#typewriter-text');
    if (nameElement) {
        // Try to get profile name from a hidden element or use default
        const profileName = window.profileName || 'Md. Rakibul Hasan';
        typewriter(profileName, 'typewriter-text', 50); // Faster typing speed (50ms instead of 80ms)
    }
    
    // Add enhanced scroll event listener
    window.addEventListener('scroll', enhancedScrollHandler);
    
    // Initialize smooth scroll
    initSmoothScroll();
    
    // Add scroll animation classes to existing elements and show immediately if in viewport
    const elementsToAnimate = document.querySelectorAll('.space-y-6, .grid, .bg-white, .bg-gray-50');
    elementsToAnimate.forEach(el => {
        el.classList.add('animate-on-scroll');
        
        // Show immediately if already in viewport
        const elementTop = el.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (elementTop < windowHeight) {
            el.classList.add('animate-visible');
        }
    });
    
    // Add click events to header profiles
    const headerProfile = document.getElementById('header-profile');
    const headerProfileMobile = document.getElementById('header-profile-mobile');
    
    if (headerProfile) {
        headerProfile.addEventListener('click', scrollToTop);
        headerProfile.style.cursor = 'pointer';
    }
    
    if (headerProfileMobile) {
        headerProfileMobile.addEventListener('click', scrollToTop);
        headerProfileMobile.style.cursor = 'pointer';
    }
    
    // Initial scroll check
    enhancedScrollHandler();
});

// Additional CSS animations via JavaScript
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideInRight {
        from { 
            opacity: 0; 
            transform: translateX(30px) scale(0.8); 
        }
        to { 
            opacity: 1; 
            transform: translateX(0) scale(1); 
        }
    }
    
    @keyframes bounceIn {
        0% { transform: scale(1); }
        50% { transform: scale(1.15); }
        100% { transform: scale(1); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .animate-fade-in {
        animation: fadeIn 0.3s ease-out;
    }
    
    .animate-slide-in-right {
        animation: slideInRight 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .animate-bounce-in {
        animation: bounceIn 0.6s ease-out;
    }
    
    #typewriter-cursor {
        color: #3b82f6;
        font-weight: normal;
    }
    
    #header-profile, #header-profile-mobile {
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    #header-profile:hover, #header-profile-mobile:hover {
        transform: scale(1.1) rotate(5deg);
        animation: pulse 2s infinite;
    }
    
    #header-profile img, #header-profile-mobile img {
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
        border: 3px solid transparent;
        background: linear-gradient(45deg, #3b82f6, #8b5cf6) border-box;
    }
    
    #header-profile:hover img, #header-profile-mobile:hover img {
        box-shadow: 0 12px 35px rgba(59, 130, 246, 0.7);
        transform: scale(1.05);
        border-color: #60a5fa;
        filter: brightness(1.1) saturate(1.2);
    }
    
    #header-profile img:active, #header-profile-mobile img:active {
        transform: scale(0.95);
    }
    
    /* Scroll Progress Bar */
    .scroll-progress {
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
        z-index: 9999;
        transition: width 0.1s ease-out;
        box-shadow: 0 2px 10px rgba(59, 130, 246, 0.5);
    }
    
    /* Header always visible - never hide */
    nav {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        transform: translateY(0) !important;
        opacity: 1 !important;
        visibility: visible !important;
        display: block !important;
        z-index: 9999 !important;
        transition: background-color 0.3s ease, box-shadow 0.3s ease !important;
    }
    
    /* Prevent any hiding animations */
    nav * {
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    /* Header scroll effect */
    nav.scrolled {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(20px) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1) !important;
        border-color: rgba(0, 0, 0, 0.1) !important;
    }
    
    .dark nav.scrolled {
        background: rgba(17, 24, 39, 0.95) !important;
        border-color: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Scroll-triggered animations - Faster and more immediate */
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(20px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .animate-on-scroll.animate-visible {
        opacity: 1;
        transform: translateY(0);
    }
    
    /* Reduced staggered animation delays */
    .animate-on-scroll:nth-child(1) { transition-delay: 0s; }
    .animate-on-scroll:nth-child(2) { transition-delay: 0.05s; }
    .animate-on-scroll:nth-child(3) { transition-delay: 0.1s; }
    .animate-on-scroll:nth-child(4) { transition-delay: 0.15s; }
    .animate-on-scroll:nth-child(5) { transition-delay: 0.2s; }
    
    /* Parallax elements */
    .parallax-element {
        will-change: transform;
    }
    
    /* Enhanced smooth scrolling */
    html {
        scroll-behavior: smooth;
    }
    
    /* Card hover animations */
    .bg-white, .bg-gray-50, .dark\\:bg-gray-800, .dark\\:bg-gray-900 {
        transition: all 0.3s ease;
    }
    
    .bg-white:hover, .bg-gray-50:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    }
    
    .dark .dark\\:bg-gray-800:hover, .dark .dark\\:bg-gray-900:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    
    /* Floating animation for decorative elements */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    .animate-float {
        animation: float 6s ease-in-out infinite;
    }
    
    .animate-float:nth-child(2) {
        animation-delay: 2s;
    }
    
    .animate-float:nth-child(3) {
        animation-delay: 4s;
    }
    
    /* Text reveal animation */
    @keyframes textReveal {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .text-reveal {
        animation: textReveal 1s ease-out;
    }
    
    /* Button hover enhancements */
    .hover\\:scale-105:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2) !important;
    }
    
    /* Performance optimizations */
    * {
        will-change: auto;
    }
    
    .animate-on-scroll, 
    .parallax-element,
    #header-profile,
    #header-profile-mobile {
        will-change: transform, opacity;
    }
`;
document.head.appendChild(style);
