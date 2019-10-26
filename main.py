import tkinter as tk
from json import dump
from tkinter import filedialog
from parseFile import General, Editor, Metadata, Difficulty, TimingPoints, Colours, HitObjects
root = tk.Tk()
root.withdraw()

print("Please select .osu file you want to parse:")
FilePath = filedialog.askopenfilename()

general = General(FilePath)
editor = Editor(FilePath)
md = Metadata(FilePath)
diff = Difficulty(FilePath)
tp = TimingPoints(FilePath)
cols = Colours(FilePath)
ho = HitObjects(FilePath)

output = dict(general, **editor, **md, **diff, **tp, **cols, **ho)

with open("parse_file.json", 'w') as outfile:
    dump(output, outfile)


