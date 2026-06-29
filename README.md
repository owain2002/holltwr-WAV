# WAV file splitter
I was recently tasked with creating a 300-entry dictionary with a pronounciation file for each headword. Rather than create 300 individual files, I created this script to do the work for me.
## What is does
The script takes a WAV file in which each word is read aloud, along with a TXT file containing the corresponding word list. Using `pydub`, it splits the WAV file at the boundaries between words and creates a separate WAV file for each individual word.
## How to use
1. Create a WAV file with your list of words, leaving around 1-2 seconds of silence between each word.
2. Save this in a folder with a TXT file which contains each of the words / phrases spoken in the WAV file *in the exact order they were spoken.*
3. Change the default filenames in the script (`geiriau.wav` and `geiriau.txt`) then save and run.
## Optional extra!
Use `opus_mp3.py` to convert each split file into small, web-optimised OPUS and MP3 files, ready for uploading.
