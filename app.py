from pushbullet import Pushbullet

API_KEY = "o.PjiOdgZCAGzcqnpdvSpVi6X6YaAiEmF6"
msg = "message.txt"

with open(msg) as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note("Coding Is My Life", text)
