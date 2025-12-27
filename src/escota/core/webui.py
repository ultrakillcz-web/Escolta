"""
Web interface module for Escota security system
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs, urlparse
from typing import Optional
import threading


class EscotaWebHandler(BaseHTTPRequestHandler):
    """HTTP request handler for Escota web interface"""

    # Class variable to store alert system reference
    alert_system = None
    database = None

    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == "/" or path == "/index.html":
            self._serve_index()
        elif path == "/api/alerts":
            self._serve_alerts_api()
        elif path == "/api/stats":
            self._serve_stats_api()
        else:
            self.send_error(404, "Not Found")

    def _serve_index(self):
        """Serve main index page"""
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>Escota Security System</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        .stat-value {
            font-size: 36px;
            font-weight: bold;
            margin: 10px 0;
        }
        .stat-label {
            font-size: 14px;
            opacity: 0.9;
        }
        .alerts-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .alerts-table th {
            background-color: #007bff;
            color: white;
            padding: 12px;
            text-align: left;
        }
        .alerts-table td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        .alerts-table tr:hover {
            background-color: #f5f5f5;
        }
        .alert-type {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }
        .alert-motion {
            background-color: #ffc107;
            color: #000;
        }
        .alert-intrusion {
            background-color: #dc3545;
            color: white;
        }
        .refresh-btn {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .refresh-btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔒 Escota Security System</h1>
        
        <button class="refresh-btn" onclick="loadData()">Refresh</button>
        
        <div class="stats" id="stats">
            <div class="stat-card">
                <div class="stat-label">Total Alerts</div>
                <div class="stat-value" id="total-alerts">0</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Motion Detected</div>
                <div class="stat-value" id="motion-alerts">0</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Intrusions</div>
                <div class="stat-value" id="intrusion-alerts">0</div>
            </div>
        </div>
        
        <h2>Recent Alerts</h2>
        <table class="alerts-table">
            <thead>
                <tr>
                    <th>Time</th>
                    <th>Type</th>
                    <th>Message</th>
                    <th>Details</th>
                </tr>
            </thead>
            <tbody id="alerts-body">
            </tbody>
        </table>
    </div>
    
    <script>
        function loadData() {
            // Load stats
            fetch('/api/stats')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('total-alerts').textContent = data.total;
                    document.getElementById('motion-alerts').textContent = data.motion;
                    document.getElementById('intrusion-alerts').textContent = data.intrusion;
                });
            
            // Load alerts
            fetch('/api/alerts')
                .then(response => response.json())
                .then(data => {
                    const tbody = document.getElementById('alerts-body');
                    tbody.innerHTML = '';
                    
                    data.alerts.forEach(alert => {
                        const row = document.createElement('tr');
                        const typeClass = 'alert-' + alert.type;
                        
                        let metadata = '';
                        if (alert.metadata && Object.keys(alert.metadata).length > 0) {
                            metadata = JSON.stringify(alert.metadata);
                        }
                        
                        row.innerHTML = `
                            <td>${new Date(alert.timestamp).toLocaleString()}</td>
                            <td><span class="alert-type ${typeClass}">${alert.type}</span></td>
                            <td>${alert.message}</td>
                            <td>${metadata}</td>
                        `;
                        tbody.appendChild(row);
                    });
                });
        }
        
        // Load data on page load
        loadData();
        
        // Auto-refresh every 5 seconds
        setInterval(loadData, 5000);
    </script>
</body>
</html>
"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def _serve_alerts_api(self):
        """Serve alerts API endpoint"""
        try:
            alerts = []

            # Try to get from database first
            if self.database:
                alerts = self.database.get_alerts(limit=50)
            elif self.alert_system:
                alerts = self.alert_system.get_alerts(limit=50)

            response = {"alerts": alerts, "count": len(alerts)}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_error(500, str(e))

    def _serve_stats_api(self):
        """Serve statistics API endpoint"""
        try:
            stats = {"total": 0, "motion": 0, "intrusion": 0}

            # Try to get from database first
            if self.database:
                stats["total"] = self.database.get_alert_count()
                stats["motion"] = self.database.get_alert_count("motion")
                stats["intrusion"] = self.database.get_alert_count("intrusion")
            elif self.alert_system:
                all_alerts = self.alert_system.get_alerts()
                stats["total"] = len(all_alerts)
                stats["motion"] = len([a for a in all_alerts if a["type"] == "motion"])
                stats["intrusion"] = len([a for a in all_alerts if a["type"] == "intrusion"])

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(stats).encode())

        except Exception as e:
            self.send_error(500, str(e))

    def log_message(self, format, *args):
        """Override to suppress request logging"""
        pass


class WebInterface:
    """Web interface server for Escota"""

    def __init__(
        self,
        alert_system=None,
        database=None,
        host: str = "localhost",
        port: int = 8080,
    ):
        """
        Initialize web interface

        Args:
            alert_system: AlertSystem instance
            database: AlertDatabase instance
            host: Server host
            port: Server port
        """
        self.host = host
        self.port = port
        self.server = None
        self.server_thread = None

        # Set class variables for handler
        EscotaWebHandler.alert_system = alert_system
        EscotaWebHandler.database = database

    def start(self):
        """Start web server in background thread"""
        self.server = HTTPServer((self.host, self.port), EscotaWebHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        print(f"Web interface started at http://{self.host}:{self.port}")

    def stop(self):
        """Stop web server"""
        if self.server:
            self.server.shutdown()
            self.server_thread.join()
            print("Web interface stopped")
