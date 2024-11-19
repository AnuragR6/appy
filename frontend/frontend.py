import webview
import os
import sys
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import threading

# Get the correct path to the dist folder
if hasattr(sys, "_MEIPASS"):  # Running as a PyInstaller executable
    BUILD_DIR = os.path.join(sys._MEIPASS, "dist")
else:  # Running as a regular Python script
    BUILD_DIR = os.path.join(os.path.dirname(__file__), "dist")

# Verify the path to the dist folder
if not os.path.exists(BUILD_DIR):
    raise FileNotFoundError(f"React build folder not found at: {BUILD_DIR}")

# Function to serve the React build folder
def start_server():
    os.chdir(BUILD_DIR)  # Change working directory to dist
    handler = SimpleHTTPRequestHandler
    with TCPServer(("127.0.0.1", 8000), handler) as httpd:
        print("Serving React build at http://127.0.0.1:8000")
        httpd.serve_forever()

# Start the HTTP server in a separate thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Create a PyWebView window to display the app
webview.create_window("Item List App", "http://127.0.0.1:8000")
webview.start()
