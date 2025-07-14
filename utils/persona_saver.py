import os

def save_persona_to_file(username: str, persona_text: str):
    os.makedirs("output", exist_ok=True)
    filename = f"output/user_persona_{username}.txt"
    with open(filename, "w") as f:
        f.write(persona_text)
