from funcs import *
import os
import shutil
import eyed3

directory = input('input your OSU directory: ')
out_directory = input('input the directory the songs will be exported to')
# directory = "H:\\Games\\osu!"
directory += "\\Songs"
# out_directory = "H:\\stuff\\my osz exporter"

found_audio = []
# log = open("log.txt", 'w+')
# initial loop for finding all the beatmap directories
for i in os.listdir(directory):
    # print('meow')

    beatmap_files = os.listdir(f'{directory}\\{i}')

    # loop for finding all files in each beatmap directory
    for file in beatmap_files:
        file_list = file.split('.')

        if len(file_list) != 0:
            if file_list[len(file_list) - 1] == 'osu' and i not in found_audio:
                found_audio.append(i)
                metadata = get_metadata(directory + '\\' + i + '\\' + file)
                metadata["SongDirectory"] = directory + '\\' + i

                # metadata will contain the keys: AudioFilename, Title, Artist, SongDirectory

                audio_ext_str = metadata["AudioFilename"]
                audio_ext_list = audio_ext_str.split('.')
                audio_ext = audio_ext_list[len(audio_ext_list) - 1]
                metadata["Title"] = filter_illegals(metadata["Title"])
                metadata["Artist"] = filter_illegals(metadata["Artist"])
                # print(metadata["Title"])
                mp3_input = f"{metadata['SongDirectory']}\\{metadata['AudioFilename']}"
                mp3_output = f"{out_directory}\\{metadata['Artist']} - {metadata['Title']}.{audio_ext}"
                print(f"{metadata['SongDirectory']}\\{metadata['AudioFilename']}")
                shutil.copy2(mp3_input, mp3_output)

                # audio_file = eyed3.load(f"{out_directory}\\{metadata['Artist']} - {metadata['Title']}.{audio_ext}")
                # audio_file.tag.artist = metadata['Artist']
                # audio_file.tag.title = metadata['Title']
                # audio_file.tag.save()
