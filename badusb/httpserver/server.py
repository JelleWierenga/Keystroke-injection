from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.data.decode("utf-8")
    with open("collected_data.txt", "a") as f:
        f.write(data + "\n")
    return "Data ontvangen", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
