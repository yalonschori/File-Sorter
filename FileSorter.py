import os
import shutil

filetypes = {
    "RAR": ".rar",
    "JPG": ".jpg",
    "PNG": ".png",
    "Text Documents": ".txt",
    "PDF": ".pdf",
    "Sony Raw Camera Files": ".arw",
}


def SortFolders():
    path = "C:/Users/yalon/Desktop/Messy/"
    os.chdir(r"C:/Users/yalon/Desktop/Messy")

    messyItems = os.listdir(path)

    for i in filetypes:
        for item in messyItems:
            if item.endswith(filetypes[i]):
                if os.path.exists(path + i):
                    shutil.move(item, path + i)
                else:
                    os.mkdir(path + i)
                    shutil.move(item, path + i)


SortFolders()
