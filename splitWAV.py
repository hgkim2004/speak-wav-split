import os
import srt
from pydub import AudioSegment

def read_audio(audio_path):
    return AudioSegment.from_file(audio_path)


f = open("test.srt", encoding="utf-8")

subtitle_g = srt.parse(f)

subtitles = list(subtitle_g)

audio_path = "jtbc-20190926.wav"
filename = os.path.basename(audio_path).split('.', 1)[0]
audio = read_audio(audio_path)
out_ext = "wav"

for idx in range(2, len(subtitles)):
    start_idx = int(subtitles[idx].start.seconds*1000 + subtitles[idx].start.microseconds/1000)
    end_idx = int(subtitles[idx].end.seconds*1000 + subtitles[idx].end.microseconds/1000)

    target_audio_path = "{}.{:04d}.{}".format(
                #os.path.dirname(audio_path), filename, idx, out_ext)
                filename, idx-1, out_ext)
    audio[start_idx:end_idx].export(target_audio_path, out_ext)
