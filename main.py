import json
import time
import random
import sys
from datetime import date
from pathlib import Path

import pygame
from mutagen.mp3 import MP3

args = sys.argv[1:]

voice_dir = Path.cwd() / "voice"
call_path = voice_dir / "se" / "chakusin.mp3"
config_dir = Path.cwd() / "config"

today = date.today()
config_file = config_dir / f"{today.year}-{str(today.month).zfill(2)}.json"
with open(str(config_file), "r", encoding="utf-8") as f:
    himekuri_voice_path_dict = json.load(f)
himekuri_voice_path = himekuri_voice_path_dict[str(today.day).zfill(2)]
if args[0] == "r":
    himekuri_voice_path = random.choice(list(himekuri_voice_path_dict.values()))

pygame.mixer.init()
pygame.mixer.music.load(str(call_path))
pygame.mixer.music.set_volume(0.2)
call_len = MP3(str(call_path)).info.length
pygame.mixer.music.play(10)
enter = input("enter")
pygame.mixer.music.stop()

pygame.mixer.init()
pygame.mixer.music.load(str(himekuri_voice_path))
pygame.mixer.music.set_volume(0.8)
himekuri_len = MP3(str(himekuri_voice_path)).info.length
pygame.mixer.music.play(1)
time.sleep(himekuri_len + 0.25)
pygame.mixer.music.stop()