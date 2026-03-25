import json
import os

DATA_DIR = "data"
USER_FILE = os.path.join(DATA_DIR, "users.json")
CHAT_FILE = os.path.join(DATA_DIR, "chats.json")

# Ensure data folder exists
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize files if not present
for file in [USER_FILE, CHAT_FILE]:
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump({}, f)


# 🔄 Load JSON safely
def load(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


# 💾 Save JSON safely
def save(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# 🔐 Register user
def register(username, password):
    users = load(USER_FILE)

    if username in users:
        return False

    users[username] = {
        "password": password  # (simple for now)
    }

    save(USER_FILE, users)
    return True


# 🔓 Login user
def login(username, password):
    users = load(USER_FILE)

    return (
        username in users and
        users[username]["password"] == password
    )


# 💬 Save chat
def save_chat(user, question, answer):
    chats = load(CHAT_FILE)

    if user not in chats:
        chats[user] = []

    chats[user].append({
        "q": question,
        "a": answer
    })

    save(CHAT_FILE, chats)


# 📜 Get chat history
def get_chat(user):
    chats = load(CHAT_FILE)
    return chats.get(user, [])