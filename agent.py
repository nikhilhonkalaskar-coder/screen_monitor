import mss
import mss.tools
import time
import requests
import socket

# --- CONFIGURATION ---
# IMPORTANT: Replace with YOUR PC's local IP address
SERVER_URL = "http://192.168.1.126:5000/api/upload"
CAPTURE_INTERVAL = 5  # Capture every 5 seconds

# Get a unique ID for this computer
EMPLOYEE_ID = socket.gethostname()

def capture_and_send_screen():
    """
    Captures the screen, compresses it, and sends it to the server.
    """
    try:
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)

            # Convert to a Pillow Image for compression
            from PIL import Image
            img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)

            # Save the image to an in-memory buffer as a JPEG
            buffer = mss.tools.to_png(sct_img.rgb, sct_img.size)
            
            # Prepare the file and data for sending
            files = {'screenshot': (f'{EMPLOYEE_ID}.png', buffer, 'image/png')}
            data = {'employee_id': EMPLOYEE_ID}

            print(f"[{EMPLOYEE_ID}] Sending screenshot...")
            response = requests.post(SERVER_URL, files=files, data=data, timeout=10)
            response.raise_for_status()
            print(f"[{EMPLOYEE_ID}] Success! Server responded with status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[{EMPLOYEE_ID}] Error sending screenshot: {e}")
    except Exception as e:
        print(f"[{EMPLOYEE_ID}] An error occurred: {e}")

if __name__ == "__main__":
    print(f"Starting agent for '{EMPLOYEE_ID}'...")
    print(f"Connecting to server at {SERVER_URL}")
    print(f"Capturing screen every {CAPTURE_INTERVAL} seconds. Press Ctrl+C to stop.")
    
    try:
        while True:
            capture_and_send_screen()
            time.sleep(CAPTURE_INTERVAL)
    except KeyboardInterrupt:
        print("\nAgent stopped.")