from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dynamic')
def dynamic():
    return render_template('dynamic.html')

@app.route('/navigation')
def navigation():
    return render_template('navigation.html')

@app.route('/responsive')
def responsive():
    return render_template('responsive.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/drag_drop')
def drag_drop():
    return render_template('drag_drop.html')

@app.route('/form_elements')
def form_elements():
    return render_template('form_elements.html')

@app.route('/button_tests')
def button_tests():
    return render_template('button_tests.html')

@app.route('/tabs')
def tabs():
    return render_template('tabs.html')

@app.route('/modal')
def modal():
    return render_template('modal.html')

@app.route('/form_fill')
def form_fill():
    return render_template('form_fill.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simüle edilmiş API gecikmesi
    time.sleep(2)
    
    # Örnek veri
    data = [
        {"id": 1, "name": "Öğe 1", "description": "Bu birinci öğenin açıklamasıdır."},
        {"id": 2, "name": "Öğe 2", "description": "Bu ikinci öğenin açıklamasıdır."},
        {"id": 3, "name": "Öğe 3", "description": "Bu üçüncü öğenin açıklamasıdır."}
    ]
    
    return jsonify(data)

@app.route('/api/users', methods=['GET'])
def get_users():
    # Kullanıcı verileri
    users = [
        {"id": 1, "name": "Ahmet Yılmaz", "email": "ahmet@example.com", "role": "Admin"},
        {"id": 2, "name": "Ayşe Demir", "email": "ayse@example.com", "role": "User"},
        {"id": 3, "name": "Mehmet Kaya", "email": "mehmet@example.com", "role": "Editor"},
        {"id": 4, "name": "Fatma Şahin", "email": "fatma@example.com", "role": "User"},
        {"id": 5, "name": "Ali Öztürk", "email": "ali@example.com", "role": "User"}
    ]
    
    return jsonify(users)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # Dosya yükleme simülasyonu
    time.sleep(2)
    return jsonify({"status": "success", "message": "Dosya başarıyla yüklendi"})

if __name__ == '__main__':
    app.run(debug=True, port=5001) 