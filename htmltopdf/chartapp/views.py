# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import pdfkit
from django.template.loader import get_template

def chart_view(request):
    return render(request, 'google_chart_template.html', {})

class generate_pdf(View):
    def post(self, request, *args, **kwargs):
        # Get the combined SVG data from the POST request
        combined_svg = request.POST.get('combinedSvg', '')
        template = get_template('google_chart_template.html')

        # Convert combined SVG to HTML string
        html_content = template.render() + f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Generated PDF</title>
        </head>
        <body>
            {combined_svg}
        </body>
        </html>
        """

        # Generate PDF using pdfkit
        pdf_data = pdfkit.from_string(html_content, False)

        # Create HttpResponse with PDF content
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        response.write(pdf_data)

        return response
