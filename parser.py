class Parser(object):
    #General
    def General(self, path):
        general = {}
        temp = {}

        File = open(path, "r", encoding="utf-8")
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
    def Editor(self, path):
        editor = {}
        temp = {}

        File = open(path, "r", encoding="utf-8")
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
    def Metadata(self, path):
        metadata = {}
        temp = {}

        File = open(path, "r", encoding="utf-8")
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
    def Difficulty(self, path):
        diff = {}
        temp = {}

        File = open(path, "r", encoding="utf-8")
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
    def TimingPoints(self, path):
        tp = {}
        temp = []

        File = open(path, "r", encoding="utf-8")
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
    def Colours(self, path):
        colours = {}
        temp = {}

        File = open(path, "r", encoding="utf-8")
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
    def HitObjects(self, path):
        tp = {}
        temp = []

        File = open(path, "r", encoding="utf-8")
        for line in File:
            if(line == "[HitObjects]\n"):
                for tier2 in File:
                    tier2 = tier2[:-1].split("|")
                    tier2[0] = tier2[0].split(",")
                    temp.append(tier2)
                tp[line[:-1]] = temp

        File.close()
        return tp

    def WholeFile(self, path):
        general = self.General(path)
        editor = self.Editor(path)
        md = self.Metadata(path)
        diff = self.Difficulty(path)
        tp = self.TimingPoints(path)
        cols = self.Colours(path)
        ho = self.HitObjects(path)

        return dict(general, **editor, **md, **diff, **tp, **cols, **ho)