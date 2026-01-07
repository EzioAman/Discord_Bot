import os
import subprocess
import requests

WEBHOOK = os.getenv("WEBHOOK_URL")
VIDEO = "assets/Freaky_nation_GIF.mov"
GIF_OUT = "freaky.gif"

def convert_video_to_gif():
    subprocess.run([
        "ffmpeg", "-y", "-i", VIDEO,
        "-vf", "scale=900:-1:flags=lanczos",
        "-r", "12",
        GIF_OUT
    ], check=True)

def post_to_discord():
    message = (
        "🧠 **FREAKY SYSTEM ONLINE**\n\n"
        "⚡ **FREAKY NATION — COMMAND CENTER**\n"
        "`[ SYSTEM CORE ONLINE ]`\n\n"
        "▣ **WELCOME TO THE BATTLEFIELD**\n\n"
        "👑 **COMMANDER** → freaky Pookie\n"
        "🛡 **ADMIN CORE** → Depressed Admin\n"
        "⚔ **ELITE OPERATORS** → Depressed freak\n\n"
        "**MODE** : Hardcore Gamer\n"
        "**STYLE** : Anime × Freak\n"
        "**STATUS** : LIVE\n\n"
        "🌀 *The system watches every move...*\n"
        "**FREAKY SYSTEM • NEURAL INTERFACE ACTIVE**"
    )

    with open(GIF_OUT, "rb") as f:
        requests.post(
            WEBHOOK,
            data={"content": message},
            files={"file": ("freaky.gif", f)}
        )

if __name__ == "__main__":
    convert_video_to_gif()
    post_to_discord()
