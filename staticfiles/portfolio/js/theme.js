function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.classList.contains('dark') ? 'dark' : 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    if (newTheme === 'dark') {
        html.classList.add('dark');
    } else {
        html.classList.remove('dark');
    }
    
    localStorage.setItem('theme', newTheme);
    
    // Update both desktop and mobile theme icons
    const themeIcon = document.getElementById('theme-icon');
    const mobileThemeButton = document.querySelector('#theme-toggle-mobile span');
    
    const iconText = newTheme === 'dark' ? '☀️' : '🌙';
    
    if (themeIcon) themeIcon.textContent = iconText;
    if (mobileThemeButton) mobileThemeButton.textContent = iconText;
}

window.onload = function() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    const html = document.documentElement;
    
    if (savedTheme === 'dark') {
        html.classList.add('dark');
    } else {
        html.classList.remove('dark');
    }
    
    // Update both desktop and mobile theme icons
    const themeIcon = document.getElementById('theme-icon');
    const mobileThemeButton = document.querySelector('#theme-toggle-mobile span');
    
    const iconText = savedTheme === 'dark' ? '☀️' : '🌙';
    
    if (themeIcon) themeIcon.textContent = iconText;
    if (mobileThemeButton) mobileThemeButton.textContent = iconText;
};