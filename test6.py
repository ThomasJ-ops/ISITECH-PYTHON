import json



data = {
    "serveur": "web-01",
    "ip": "192.168.1.10",
    "metriques": {
        "cpu": 45,
        "ram": 60,
        "actif": True
    },
    "tags": ["production", "web", "nginx"]
}

# JSON vers Python
with open("config.json", "r") as f:
    loaded = json.load(f)


print(loaded)

# Depuis string
data2 = json.loads('{"nom": "test", "value": 42}')
print(data2)