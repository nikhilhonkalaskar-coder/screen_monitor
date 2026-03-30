from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import datetime

app = Flask(__name__)

# Folders for storing images
UPLOAD_FOLDER = 'uploads'
LATEST_FOLDER = os.path.join(UPLOAD_FOLDER, 'latest')
if not os.path.exists(LATEST_FOLDER):
    os.makedirs(LATEST_FOLDER)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# This route displays the main dashboard
@app.route('/')
def dashboard():
    # Get a list of all employees who have sent a screenshot recently
    # For simplicity, we just list all files in the 'latest' folder
    try:
        employees = [f.split('.')[0] for f in os.listdir(LATEST_FOLDER) if f.endswith('.jpg')]
    except FileNotFoundError:
        employees = []
    return render_template('index.html', employees=employees)

# This route serves the latest screenshot for a specific employee
@app.route('/latest/<employee_id>.jpg')
def get_latest_screenshot(employee_id):
    filepath = os.path.join(LATEST_FOLDER, f'{employee_id}.jpg')
    if os.path.exists(filepath):
        return send_from_directory(LATEST_FOLDER, f'{employee_id}.jpg')
    else:
        # Return a 404 if the image doesn't exist yet
        return "Not Found", 404

# This is the endpoint the agent sends its screenshots to
@app.route('/api/upload_multi', methods=['POST'])
def upload_screenshot_multi():
    employee_id = request.form.get('employee_id')
    if not employee_id:
        return jsonify({"error": "employee_id is required"}), 400

    if 'screenshot' not in request.files:
        return jsonify({"error": "No screenshot part"}), 400
    
    file = request.files['screenshot']
    if file:
        # Save the latest image for the live view
        latest_filepath = os.path.join(LATEST_FOLDER, f'{employee_id}.jpg')
        file.save(latest_filepath)

        # Also, save a timestamped copy for the gallery
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        gallery_filename = f"screen_{employee_id}_{timestamp}.jpg"
        gallery_filepath = os.path.join(UPLOAD_FOLDER, gallery_filename)
        file.save(gallery_filepath)
        
        print(f"--- Received and saved screenshot for {employee_id} ---")
        
        return jsonify({"message": "Screenshot uploaded successfully"}), 200

# The gallery page remains the same
@app.route('/gallery')
def gallery():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files.sort(reverse=True)
    return render_template('gallery.html', images=files)

if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible from other computers on the network
    app.run(host='0.0.0.0', port=5000, debug=True)