"""Naval Fate.

Usage:
  youtube-to-instruments.py --name <name> --url <youtube-url> [--basepath <basepath>]

Options:
  --name        name of the song.
  --url         url of the youtube video.
  --basepath    basepath for extraction.
"""
from docopt import docopt
import os

arguments = docopt(__doc__, version='Youtube to instruments 0.0.1')


if __name__ == '__main__':
    name = arguments["<name>"]
    url = arguments["<youtube-url>"]
    basepath = os.path.abspath(arguments["<basepath>"] or os.getcwd())
    path = os.path.join(basepath, name)
    instruments_path = os.path.join(path, "instruments")
    wav_path = os.path.join(path, name + ".wav")

    os.system("mkdir -p {instruments_path}".format( instruments_path = instruments_path ))
    os.system("youtube-dl --extract-audio --audio-format wav -o {wav_path} {url}".format(wav_path = wav_path, url = url))
    os.system("spleeter separate -i {wav_path} -p spleeter:5stems -o {instruments_path}".format(instruments_path = instruments_path , wav_path = wav_path))
    os.system("mv {instruments_path}/{name}/*.wav {instruments_path}".format(instruments_path = instruments_path, name = name))
    os.system("rm -rf {instruments_path}/{name}/".format(instruments_path = instruments_path, name = name))
