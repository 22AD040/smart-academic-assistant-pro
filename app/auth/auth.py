import json
import os

USER_FILE = "data/users.json"
CHAT_FILE = "data/chats.json"


os.makedirs("data", exist_ok=True)

if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        f.write("{}")

if not os.path.exists(CHAT_FILE):
    with open(CHAT_FILE, "w") as f:
        f.write("{}")


def load(file):
    if not os.path.exists(file):
        return {}

    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return {}


def save(file, data):
    os.makedirs("data", exist_ok=True)
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def register(username, password):
    users = load(USER_FILE)

    if username in users:
        return False

    users[username] = {"password": password}
    save(USER_FILE, users)
    return True


def login(username, password):
    users = load(USER_FILE)
    return username in users and users[username]["password"] == password


def save_chat(user, q, a):
    chats = load(CHAT_FILE)

    if user not in chats:
        chats[user] = []

    chats[user].append({"q": q, "a": a})
    save(CHAT_FILE, chats)


def get_chat(user):
    return load(CHAT_FILE).get(user, [])