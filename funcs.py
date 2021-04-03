def get_metadata(osz):
    file = open(osz, 'r')
    try:
        text = file.read()

    except UnicodeDecodeError:
        # catches if the file is in UTF-8 encoding instead of CP1252
        file = open(osz, encoding="utf8")
        text = file.read()
    metadatas = ["AudioFilename", "Title", "Artist"]
    gaming = {"AudioFilename": '',
              "Title": '',
              "Artist": ''
              }
    for i in text.splitlines():
        for data in metadatas:
            if i.startswith(data) and not i.startswith("ArtistUnicode"):
                index_listed = i.split(":")
                metadata_k = index_listed[1]
                metadata = ''
                meowing = True
                while meowing:
                    if metadata_k.startswith(" "):
                        idk = 0

                        for char in metadata_k:
                            idk += 1
                            if char == ' ' and idk == 1:
                                char = ''
                            metadata += char
                        meowing = False
                    else:
                        metadata = metadata_k
                        meowing = False
                gaming[data] = metadata
    return gaming


def filter_illegals(string):
    illegals = ['\\', '/', ':', '*', '?', '\"', '<', '>', '|', "\'", "λ"]

    new_value = ''
    for i in string:
        if i in illegals:
            i = ''
        new_value += i
    string = new_value

    return string

