import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import *

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass
        return (resource, id)


    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {} #default response
        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        # Your new console.log() that outputs to the terminal
        print(self.path)

        # It's an if..else statement
        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)

            else:
                response = get_all_metals()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)

            else:
                response = get_all_sizes()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)

            else:
                response = get_all_orders()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)

            else:
                response = get_all_styles()
        
       


        # Send a JSON formatted string as a response
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new metal
        new_item = None

        # Add a new metal to the list. Don't worry about
        # the orange squiggle, you'll define the create_metal
        # function next.
        if resource == "metals":
            new_item = create_metal(post_body)
        elif resource == "sizes":
            new_item = create_size(post_body)
        elif resource == "styles":
            new_item = create_style(post_body)
        elif resource == "orders":
            new_item = create_order(post_body)

        # Encode the new metal and send in response
        self.wfile.write(json.dumps(new_item).encode())

    # A method that handles any PUT request.
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single metal from the list
        if resource == "metals":
          update_metal(id, post_body)
        elif resource == "sizes":
          update_size(id, post_body)
        elif resource == "orders":
          update_order(id, post_body)
        elif resource == "styles":
          update_style(id, post_body)

    # Encode the new metal and send in response
        self.wfile.write("".encode())

            
    def do_DELETE(self):
    # Set a 204 response code
        self._set_headers(204)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single metal from the list
        if resource == "metals":
            delete_metal(id)
        elif resource == "sizes":
            delete_size(id)
        elif resource == "orders":
            delete_order(id)
        elif resource == "styles":
            delete_style(id)

    # Encode the new metal and send in response
        self.wfile.write("".encode())
            
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/metals/1", the resulting list will
        # have "" at index 0, "metals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /metals
        except ValueError:
            pass  # Request had trailing slash: /metals/

        return (resource, id)  # This is a tuple




# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
