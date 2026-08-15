import os
import re

files = ["index.html", "about.html", "projects.html", "contact.html", "products.html"]

nav_pattern = r'<nav class="nav-menu" id="navMenu">.*?</nav>'
footer_nav_pattern = r'<div class="footer-links-list">.*?</div>'

new_nav = '''<nav class="nav-menu" id="navMenu">
                <a href="index.html" class="nav-link">Home</a>
                <a href="about.html" class="nav-link">About</a>
                <a href="products.html" class="nav-link">Products</a>
                <a href="services.html" class="nav-link">Services</a>
                <a href="projects.html" class="nav-link">Projects</a>
                <a href="contact.html" class="nav-link">Contact</a>
            </nav>'''

new_footer_nav = '''<div class="footer-links-list">
                    <a href="index.html">Home</a>
                    <a href="about.html">About Us</a>
                    <a href="products.html">Products</a>
                    <a href="services.html">Services</a>
                    <a href="projects.html">Our Projects</a>
                    <a href="contact.html">Contact</a>
                </div>'''

for file in files:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
        
        content = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)
        content = re.sub(footer_nav_pattern, new_footer_nav, content, flags=re.DOTALL)
        
        # Also remove active class if present and add to the correct page
        # Note: Active class handling can be done but for simplicity we'll just update the links.
        # Let's write the updated content
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
