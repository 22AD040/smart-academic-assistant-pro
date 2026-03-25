import json
import os

DATA_DIR = "data"
USER_FILE = os.path.join(DATA_DIR, "users.json")
CHAT_FILE = os.path.join(DATA_DIR, "chats.json")


os.makedirs(DATA_DIR, exist_ok=True)


for file in [USER_FILE, CHAT_FILE]:
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump({}, f)



def load(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}



def save(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)



def register(username, password):
    users = load(USER_FILE)

    if username in users:
        return False

    users[username] = {
        "password": password  
    }

    save(USER_FILE, users)
    return True



def login(username, password):
    users = load(USER_FILE)

    return (
        username in users and
        users[username]["password"] == password
    )



def save_chat(user, question, answer):
    chats = load(CHAT_FILE)

    if user not in chats:
        chats[user] = []

    chats[user].append({
        "q": question,
        "a": answer
    })

    save(CHAT_FILE, chats)



def get_chat(user):
    chats = load(CHAT_FILE)
    return chats.get(user, [])