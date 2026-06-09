from flask import Flask, jsonify, render_template_string
import socket
import sys
import datetime
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Health Dashboard</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 600px; width: 100%; }
        h1 { color: #1F4E79; margin-bottom: 20px; font-size: 1.8rem; }
        .card {
            background: white;
            border-radius: 10px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .row { display: flex; justify-content: space-between; padding: 8px 0;
               border-bottom: 1px solid #f0f0f0; }
        .row:last-child { border-bottom: none; }
        .label { color: #666; font-size: 0.9rem; }
        .value { font-weight: bold; color: #1F4E79; }
        .status-badge {
            display: inline-block;
            background: #d4edda;
            color: #155724;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: bold;
        }
        .api-link { color: #1F4E79; text-decoration: none; }
        .api-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>&#128640; DevOps Health Dashboard</h1>
        <div class="card">
            <div class="row">
                <span class="label">Status</span>
                <span class="status-badge">&#10003; Healthy</span>
            </div>
            <div class="row">
                <span class="label">Hostname</span>
                <span class="value">{{ hostname }}</span>
            </div>
            <div class="row">
                <span class="label">Python Version</span>
                <span class="value">{{ python_version }}</span>
            </div>
            <div class="row">
                <span class="label">Environment</span>
                <span class="value">{{ env }}</span>
            </div>
            <div class="row">
                <span class="label">Server Time (UTC)</span>
                <span class="value">{{ server_time }}</span>
            </div>
        </div>
        <div class="card">
            <p style="color:#666; font-size:0.9rem;">
                API endpoint: <a class="api-link" href="/api/health">/api/health</a>
            </p>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=socket.gethostname(),
        python_version=sys.version.split()[0],
        env=os.environ.get("APP_ENV", "development"),
        server_time=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    )

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "python_version": sys.version.split()[0],
        "environment": os.environ.get("APP_ENV", "development"),
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
