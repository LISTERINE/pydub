import subprocess
from tempfile import NamedTemporaryFile
from .utils import get_player_name, get_startup_info

PLAYER = get_player_name()
STARTUP_INFO = get_startup_info()



def play(audio_segment, headless=True):
    with NamedTemporaryFile("w+b", suffix=".wav") as f:
        audio_segment.export(f.name, "wav")
        command = [PLAYER, "-nodisp", "-autoexit", f.name]
        if not headless:
            subprocess.call(command)
        else:
            proc = subprocess.Popen(command, startupinfo=STARTUP_INFO)


def play_file(file_name, headless=True):
    command = [PLAYER, "-nodisp", "-autoexit", file_name]
    if not headless:
        subprocess.call(command)
    else:
        proc = subprocess.Popen(command, startupinfo=STARTUP_INFO)
