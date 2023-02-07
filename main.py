from  pydub import AudioSegment
import os
import argparse

options = argparse.ArgumentParser()
options.add_argument("-m","--manually",action="store_true",help="Manually select the audio volume in dB")
args = options.parse_args()

def volume_changer(volume):
    try:
        os.mkdir("new_audio")
    except FileExistsError:
        pass

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            title=file
            print(f"Generating new {title}")
            sound=AudioSegment.from_mp3(title)
            new_vol = volume - sound.dBFS
            newsound=sound.apply_gain(new_vol)
            new_name = os.path.join("./new_audio/",title)
            newsound.export(new_name,format="mp3")
    print("Done")

for file in os.listdir("./"):
    if file.endswith(".mp3"):
        title=file
        sound=AudioSegment.from_mp3(title)
        volume=sound.dBFS
        print(f"Volume of {title}: ",volume)
print("")

if args.manually:
    try:
        volume = input("Insert the volume level (in dB): ")
        volume_changer(float(volume))
    except ValueError:
        print("Invalid value")
else:
    name = input("Write the name of the audio file you want the others to take the volume level from (with .mp3 at the end): ")
    try:
        vol = AudioSegment.from_mp3(name)
        volume=vol.dBFS
        print("Volume selected (in dB): "+str(volume))
        volume_changer(volume)
    except FileNotFoundError:
        print("File not found")


