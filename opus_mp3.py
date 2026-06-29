from pathlib import Path
import subprocess

input_dir = Path("geiriau_unigol")
opus_dir = Path("opus")
mp3_dir = Path("mp3")

opus_dir.mkdir(exist_ok=True)
mp3_dir.mkdir(exist_ok=True)

for file in input_dir.glob("*.wav"):
    base = file.stem

    subprocess.run([
        "ffmpeg",
        "-i", str(file),
        "-ac", "1",
        "-ar", "48000",
        "-c:a", "libopus",
        "-b:a", "24k",
        str(opus_dir / f"{base}.opus")
    ], check=True)

    subprocess.run([
        "ffmpeg",
        "-i", str(file),
        "-ac", "1",
        "-ar", "44100",
        "-c:a", "libmp3lame",
        "-b:a", "48k",
        str(mp3_dir / f"{base}.mp3")
    ], check=True)