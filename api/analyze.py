from flask import Flask, jsonify
import socket

app = Flask(__name__)

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect(('127.0.0.1', port))
        s.close()
        return True
    except:
        return False

@app.route('/analyze')
def analyze():
    ports_to_check = [22, 80, 443, 3306, 8080]  # common ports
    results = {}

    for port in ports_to_check:
        is_open = check_port(port)
        vulnerability = None
        if is_open:
            if port == 22:
                vulnerability = 'SSH open - check for weak passwords or outdated software'
            elif port == 80:
                vulnerability = 'HTTP open - check for unpatched web servers'
            elif port == 443:
                vulnerability = 'HTTPS open - ensure SSL certs are valid'
            elif port == 3306:
                vulnerability = 'MySQL open - secure database access'
            elif port == 8080:
                vulnerability = 'Alternate HTTP port open - check services'

        results[port] = {
            'open': is_open,
            'vulnerability': vulnerability
        }

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
