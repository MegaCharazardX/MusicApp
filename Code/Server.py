from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/E:\Dhejus\PythonPractice\XII_Practical\XII_Practical/")

def server_file(filename):
    return send_from_directory("Shared", filename)

if __name__ == "main":
    app.run(
        host="192.168.67.69",
        port=5000
    )