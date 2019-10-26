#General
def General(file_path):
    general = {}
    temp = {}

    File = open(file_path, "r", encoding="utf-8")
    for line in File:
        if(line == "[General]\n"):
            for tier2 in File:
                tier2 = tier2[:-1]
                tier2 = tier2.split(": ")
                try:
                    temp[tier2[0]] = tier2[1]
                except:
                    general[line[:-1]] = temp
                    break

    File.close()
    return general
    

#Editor
def Editor(file_path):
    editor = {}
    temp = {}

    File = open(file_path, "r", encoding="utf-8")
    for line in File:
        if(line == "[Editor]\n"):
            for tier2 in File:
                tier2 = tier2[:-1]
                tier2 = tier2.split(": ")
                if(tier2[0] == "Bookmarks"):
                    temp[tier2[0]] = tier2[1].split(",")
                    continue
                try:
                    temp[tier2[0]] = tier2[1]
                except:
                    editor[line[:-1]] = temp
                    break

    File.close()
    return editor

#Metadata
def Metadata(file_path):
    metadata = {}
    temp = {}

    File = open("test.osu", "r", encoding="utf-8")
    for line in File:
        if(line == "[Metadata]\n"):
            for tier2 in File:
                tier2 = tier2[:-1]
                tier2 = tier2.split(":")
                try:
                    temp[tier2[0]] = tier2[1]
                except:
                    metadata[line[:-1]] = temp
                    break
                
    File.close()
    return metadata

#Difficulty
def Difficulty(file_path):
    diff = {}
    temp = {}

    File = open(file_path, "r", encoding="utf-8")
    for line in File:
        if(line == "[Difficulty]\n"):
            for tier2 in File:
                tier2 = tier2[:-1]
                tier2 = tier2.split(":")
                try:
                    temp[tier2[0]] = tier2[1]
                except:
                    diff[line[:-1]] = temp
                    break
                
    File.close()
    return diff

#TimingPoints
def TimingPoints(file_name):
    tp = {}
    temp = []

    File = open(file_name, "r", encoding="utf-8")
    for line in File:
        if(line == "[TimingPoints]\n"):
            for tier2 in File:
                if(tier2[0] == "\n"):
                    tp[line[:-1]] = temp
                    break
                temp.append(tier2[:-1])

    File.close()
    return tp

#Colours
def Colours(file_name):
    colours = {}
    temp = {}

    File = open(file_name, "r", encoding="utf-8")
    for line in File:
        if(line == "[Colours]\n"):
            for tier2 in File:
                tier2 = tier2[:-1]
                tier2 = tier2.split(" : ")
                try:
                    temp[tier2[0]] = tier2[1]
                except:
                    colours[line[:-1]] = temp
                    break

    File.close()
    return colours

#HitObjects
def HitObjects(file_name):
    tp = {}
    temp = []

    File = open(file_name, "r", encoding="utf-8")
    for line in File:
        if(line == "[HitObjects]\n"):
            for tier2 in File:
                tier2 = tier2[:-1].split("|")
                tier2[0] = tier2[0].split(",")
                temp.append(tier2)
            tp[line[:-1]] = temp

    File.close()
    return tp