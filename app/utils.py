from django.template.loader import render_to_string
import os

def create_category_html(category):
    # Generate the HTML content for the category
    html_content = render_to_string('category_detail.html', {'category': category})

    # Create the file path for the new HTML file
    file_path = os.path.join('categories', f'{category.slug}.html')

    # Save the HTML content to the new file
    with open(file_path, 'w') as f:
        f.write(html_content)
