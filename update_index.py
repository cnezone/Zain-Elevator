import re

with open('index.html', 'r') as f:
    content = f.read()

# Update Products Section Header
products_pattern = r'<span class="section-tag">Premium Lifts</span>.*?<h2>Our Elevator Products</h2>.*?<p>We provide a comprehensive range of imported and semi-imported elevators tailored for home, hospital, commercial, and industrial needs.</p>'
new_products_header = '''<span class="section-tag">Featured Products</span>
                <h2>Our Premium Elevators</h2>
                <p>We provide a comprehensive range of imported and semi-imported elevators tailored for home, hospital, commercial, and industrial needs.</p>
                <div style="margin-top: 15px;">
                    <a href="products.html" class="btn btn-outline" style="border-radius: 100px; padding: 8px 24px;">View All Products <i class="fas fa-arrow-right"></i></a>
                </div>'''
content = re.sub(products_pattern, new_products_header, content, flags=re.DOTALL)

# Update Services Button link
services_btn_pattern = r'<a href="https://wa.me/923318880539" target="_blank" class="btn btn-primary mt-4">Consult Our Engineers</a>'
new_services_btn = '''<a href="services.html" class="btn btn-primary" style="margin-top: 24px;">View All Services</a>
                    <a href="https://wa.me/923318880539" target="_blank" class="btn btn-outline" style="margin-top: 24px; margin-left: 10px;">Consult Engineers</a>'''
content = re.sub(services_btn_pattern, new_services_btn, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print("Index updated successfully")
