#Task 3
db_config = {
"connection": {
"host": "production-db.internal",
"port": 5432,
"user": "postgres"
    }
}
if db_config.get("connection").get("ssl_settings"):
    ssl_mode = db_config.get("connection").get("ssl_settings")
else:
    ssl_mode = "verify-full"
print(f'SSL Mode: {ssl_mode}\nПараметры соединения:')
for k, v in db_config["connection"].items():
    print(f'* {k}: {v}')
