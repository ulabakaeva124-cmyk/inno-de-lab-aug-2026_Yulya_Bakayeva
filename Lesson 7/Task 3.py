#Task 3
db_config = {
"connection": {
"host": "production-db.internal",
"port": 5432,
"user": "postgres"
    }
}
conn = db_config.get("connection", {})
ssl_mode = conn.get("ssl_settings", {}).get("ssl_mode", "verify-full")
host = conn.get("host", {})
port = conn.get("port", {})
conn["user"] = "admin"
conn["max_connections"] = 100
print(f'SSL Mode: {ssl_mode}\nПараметры соединения:')
for k, v in db_config["connection"].items():
    print(f'* {k}: {v}')

