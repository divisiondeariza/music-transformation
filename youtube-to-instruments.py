"""Naval Fate.

Usage:
  youtube-to-instruments.py --name <name> --url <youtube-url>

Options:
  --name name of the song
  --url url of the youtube video.

"""
from docopt import docopt
import os

arguments = docopt(__doc__, version='Youtube to instruments 0.0.1')


if __name__ == '__main__':
    name = arguments["--name"]
    url = arguments["--url"]

    os.system("mkdir -p {name}/instruments".format(name = name))
    os.system("youtube-dl --extract-audio --audio-format wav -o {name}/{name}.wav {url}".format(name = name, url = url))
    os.system("spleeter separate -i {name}/{name}.wav -p spleeter:5stems -o {name}/instruments".format(name = name))


    print(arguments)
