from pathlib import Path
import re
from pydub import AudioSegment
from pydub.silence import split_on_silence

INPUT_AUDIO = "geiriau.wav"
WORD_LIST = "geiriau.txt"
OUTPUT_DIR = Path("geiriau_unigol")

MIN_SILENCE_LEN = 900
SILENCE_THRESH = -48
KEEP_SILENCE = 400

def slugify(text):
    text = text.lower().strip()
    replacements = {
        "â": "a", "ê": "e", "î": "i", "ô": "o", "û": "u", "ŵ": "w", "ŷ": "y",
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ï": "i",
        "'": "",
        "’": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

audio = AudioSegment.from_wav(INPUT_AUDIO)

words = [
    line.strip()
    for line in Path(WORD_LIST).read_text(encoding="utf-8").splitlines()
    if line.strip()
]

clips = split_on_silence(
    audio,
    min_silence_len=MIN_SILENCE_LEN,
    silence_thresh=SILENCE_THRESH,
    keep_silence=KEEP_SILENCE
)

OUTPUT_DIR.mkdir(exist_ok=True)

print(f"Geiriau mewn rhestr: {len(words)}")
print(f"Clipiau wedi'u canfod: {len(clips)}")

if len(words) != len(clips):
    print("RHYBUDD: Mae nifer y geiriau yn wahanol i nifer y clipiau!")
    print("Efallai bydd angen i ti addasu MIN_SILENCE_LEN neu SILENCE_THRESH.")
    print("Yn allforio gyda enwau ffeiliau rhifog i'w gwirio...")

for i, clip in enumerate(clips, start=1):
    if i <= len(words):
        name = slugify(words[i - 1])
        filename = f"{i:03d}-{name}.wav"
    else:
        filename = f"{i:03d}-ychwanegol.wav"

    clip.export(OUTPUT_DIR / filename, format="wav")
    print(filename)