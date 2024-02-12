# chartapp/views.py

from django.http import HttpResponse
import pdfkit


# chartapp/views.py

from django.shortcuts import render

def google_chart_to_pdf(request):
    return render(request, 'google_chart_template.html')

# chartapp/views.py
# chartapp/views.py

# chartapp/views.py
# chartapp/views.py
# chartapp/views.py
import subprocess
from django.http import HttpResponse
from django.shortcuts import render

def generate_pdf(request):
    command = r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe'
    options = {
        'quiet': '',
        'no-images': '',
        'margin-top': '10mm',
        'margin-right': '10mm',
        'margin-bottom': '10mm',
        'margin-left': '10mm',
    }

    # Render the template
    template_name = 'google_chart_template.html'
    context = {}  # Add any context data needed for rendering
    html_content = render(request, template_name, context).content

    # Check if html_content is None
    if html_content is None:
        return HttpResponse("Error: Unable to retrieve HTML content from the template.")

    html_content = html_content.decode('utf-8')

    try:
        # Execute the command
        subprocess.run([command, '--'] + list(options.keys()), input=html_content.encode('utf-8'), check=True)
    except subprocess.CalledProcessError as e:
        # Capture and print any errors
        print("Command returned non-zero exit status:", e.returncode)
        print("Output:", e.output.decode('utf-8'))

    return HttpResponse("PDF generated successfully.")
