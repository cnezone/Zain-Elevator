import re

# Update products.html
with open('products.html', 'r') as f:
    content = f.read()

# Change title & header in products.html
content = content.replace('<title>Products &amp; Services | Zain Engineering</title>', '<title>Products | Zain Engineering</title>')
content = content.replace('<h1 class="page-title">Products &amp; Services</h1>', '<h1 class="page-title">Our Products</h1>')
content = content.replace('<p class="page-desc">Comprehensive elevator solutions tailored for residential, commercial, and industrial requirements in Pakistan.</p>', '<p class="page-desc">Explore our premium range of imported and semi-imported elevators tailored for home, hospital, commercial, and industrial needs.</p>')

# Remove services section from products.html
services_pattern = r'<!-- ========== DETAILED SERVICES & SYSTEM ========== -->.*?(?=<!-- ========== CTA BAND ========== -->)'
content = re.sub(services_pattern, '', content, flags=re.DOTALL)

with open('products.html', 'w') as f:
    f.write(content)


# Update services.html
with open('services.html', 'r') as f:
    content = f.read()

# Change title & header in services.html
content = content.replace('<title>Products &amp; Services | Zain Engineering</title>', '<title>Services | Zain Engineering</title>')
content = content.replace('<h1 class="page-title">Products &amp; Services</h1>', '<h1 class="page-title">Our Services</h1>')
content = content.replace('<p class="page-desc">Comprehensive elevator solutions tailored for residential, commercial, and industrial requirements in Pakistan.</p>', '<p class="page-desc">End-to-end engineering services including supply, installation, modernization, and maintenance for your elevator systems.</p>')

# Remove products section from services.html
products_pattern = r'<!-- ========== DETAILED PRODUCTS ========== -->.*?(?=<!-- ========== DETAILED SERVICES & SYSTEM ========== -->)'
content = re.sub(products_pattern, '', content, flags=re.DOTALL)

with open('services.html', 'w') as f:
    f.write(content)

print("Split completed successfully")
