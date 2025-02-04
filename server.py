from jinja2 import Environment, FileSystemLoader
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from app import app

# Get the absolute path to the templates directory
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'templates')

# Set up Jinja environment
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

class TemplateHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Remove leading slash and get template name
        template_name = self.path.lstrip('/')

        # if no template specified, use index.html
        if not template_name:
            template_name = 'index.html'  # Default template
        # Handle both cases: with and without .html extension
        if not template_name.endswith('.html'):
            template_name += '.html'
        
        try:
            # Get the template
            template = env.get_template(template_name)

            marker_data = []
            # Example data (replace with your actual logic to populate this list)
            lat = 34.0522
            lon = -118.2437
            price = 500000
            address = '123 Main St'
            address2 = 'Suite 100'
            zipcode = '90012'
            county = 'Los Angeles'
            state = 'CA'

            # Append data to marker_data
            marker_data.append({
                'lat': lat,
                'lon': lon,
                'price': price,
                'address': address,
                'address2': address2,
                'zipcode': zipcode,
                'county': county,
                'state': state
            })
            # Render the template (add your context data here)
            content = template.render(
                marker_data=marker_data
            )
            
            # Send headers
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Send content
            self.wfile.write(content.encode())
    
            
        except Exception as e:
            print(f"Error loading template {template_name}: {str(e)}")
            self.send_error(404, f"Template not found: {str(e)}")

    def render_template(template_name, **context):
        """
        Renders a template with the given context.
        
        :param template_name: Name of the template file (e.g., 'map.html')
        :param context: Dictionary of variables to pass to the template
        :return: Rendered HTML string
        """
        template = env.get_template(template_name)
        return template.render(**context)   

if __name__ == '__main__':
    # Set up server
    server_address = ('', 8000)  # Empty string means localhost
    httpd = HTTPServer(server_address, TemplateHandler)
    print(f"Server running at http://localhost:8000")
    print(f"Template directory: {TEMPLATE_DIR}")
    httpd.serve_forever()
    app.run(debug=True)  # You can specify host and port if needed