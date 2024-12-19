from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max size

@app.route('/upload', methods=['POST'])
def upload_document():
    """
    Upload a Document
    ---
    tags:
      - File Upload
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: The file to upload
    responses:
      200:
        description: File uploaded successfully
        schema:
          type: object
          properties:
            message:
              type: string
            filename:
              type: string
            file_path:
              type: string
      400:
        description: Invalid request or no file provided
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    return jsonify({
        "message": "File uploaded successfully",
        "filename": filename,
        "file_path": file_path
    }), 200

@app.route('/uploaded-files', methods=['GET'])
def list_uploaded_files():
    """
    List all uploaded files
    ---
    responses:
      200:
        description: List of uploaded files
        schema:
          type: array
          items:
            type: string
    """
    files = os.listdir(app.config['UPLOAD_FOLDER']) 
    return jsonify(files), 200

if __name__ == '__main__':
    app.run(debug=True)



