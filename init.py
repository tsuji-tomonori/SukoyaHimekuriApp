from pathlib import Path
import json

voice_dir = Path("voice")
config_dir = Path("config")
dir_dict = dict(enumerate(voice_dir.iterdir()))
SUFFIX = [".mp3", ".wav"]

for k, v in dir_dict.items():
    print(f"index:{k} [{v}]")

idx = int(input("index:"))
year = input("year:")
month = input("month:")

choice_dir = dir_dict[idx]
files = [file for file in choice_dir.iterdir() if file.suffix in SUFFIX]
files.sort()
result = {str(day+1).zfill(2): str(file) for day, file in enumerate(files)}

result_file_name = str(config_dir / (year + "-" + month.zfill(2))) + ".json"
with open(result_file_name, "w", encoding='utf8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f"save as {result_file_name}")