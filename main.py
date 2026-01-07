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
    "```ansi\n"
    "\u001b[1;36m⚡ FREAKY NATION — COMMAND CENTER\u001b[0m\n"
    "\u001b[2;36m[ SYSTEM CORE ONLINE ]\u001b[0m\n\n"
    "\u001b[1;37m▣ WELCOME TO THE BATTLEFIELD\u001b[0m\n\n"
    "\u001b[1;33m👑 COMMANDER      \u001b[0mfreaky Pookie\n"
    "\u001b[1;34m🛡 ADMIN CORE     \u001b[0mDepressed Admin\n"
    "\u001b[1;31m⚔ ELITE OPERATORS \u001b[0mDepressed freak\n\n"
    "\u001b[1;32mMODE  \u001b[0m: Hardcore Gamer\n"
    "\u001b[1;35mSTYLE \u001b[0m: Anime × Freak\n"
    "\u001b[1;36mSTATUS\u001b[0m: LIVE\n\n"
    "\u001b[2;36mNeural grid synchronized...\u001b[0m\n"
    "\u001b[2;36mBattle authority confirmed.\u001b[0m\n"
    "\u001b[2;36mReality interface engaged.\u001b[0m\n"
    "```\n"
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
