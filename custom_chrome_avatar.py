import tkinter as tk
from tkinter import filedialog
import os
import sys

appdata = os.getenv('LOCALAPPDATA')
avatar_path = os.path.join(appdata, "Google/Chrome/User Data/Avatars")

root = tk.Tk()
root.withdraw()


def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png")])
    return file_path


if __name__ == "__main__":
    if not os.path.exists(avatar_path):
        sys.exit("Chrome not found.")

    avatars = [file for file in os.listdir(
        avatar_path) if file.endswith(".png")]

    i = 0
    for avatar in avatars:
        print(str(i) + " - " + avatar.replace(".png", "").replace("avatar_", ""))
        i += 1

    avatar = os.path.join(avatar_path, avatars[int(
        input("\nWhich avatar do you want to modify? ").strip())])

    input("\nHit enter to choose new avatar. Recommended size - 256x256.")
    new_avatar = choose_file()

    if len(new_avatar) == 0:
        sys.exit("Avatar not selected.")

    image_data = open(new_avatar, "rb").read()

    with open(avatar, "wb") as f:
        f.write(image_data)

    input("\nDone. Restart chrome.")
