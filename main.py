import subprocess
from flask import Flask, request

app = Flask(__name__)

# A simple password to prevent others from using your console
SECRET_KEY = "onrender@123"

@app.route('/exec')
def run_command():
    key = request.args.get('key')
    cmd = request.args.get('cmd')
    
    if key != SECRET_KEY:
        return "Unauthorized", 401
    
    try:
        # Runs the command and captures the text output
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return f"<pre>{output}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>Error:\n{e.output}</pre>", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
