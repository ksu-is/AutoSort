#File Sorter by Mahesh Sawant 

import os,shutil

s=os.chdir("Downloads")
current = os.getcwd()

files=os.listdir(current)

images=[".jpeg",".png",".jpg",".gif"] #extensions for images
text=[".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"] #extensions for text files
videos=[".mp4",".mkv"] #extensions for videos
sounds=[".mp3",".wav",".m4a"] #extensions for sounds
applications=[".exe",".lnk"] #extensions for applications
codes = [".c",".py",".java",".cpp",".js",".html",".css",".php"] #extensions for codes
answer1 = input("Do you want files in one folder or separate? Type one or separate")
if answer1 == "one":
    print("Sorting the files...")

    for file in files:
        dest = ""
        for ex in images:
            if file.endswith(ex):
                dest='../all'
                shutil.move(file,dest)
                break

        for ex in text:
            if file.endswith(ex):
                dest='../all'
                shutil.move(file,dest)
                break

        for ex in sounds:
            if file.endswith(ex):
                dest='../all'
                shutil.move(file,dest)
                break

        for ex in videos:
            if file.endswith(ex):
                dest='../all'
                shutil.move(file,dest)
                break

        for ex in applications:
            if file.endswith(ex):
                dest= '../all'
                shutil.move(file,dest)
                break

        for ex in codes:
            if file.endswith(ex):
                dest= '../all'
                shutil.move(file,dest)
                break

        if dest == "":
            shutil.move(file,'../all')
elif answer1 == 'separate':
    answer2 = input("Would you like to separate further? Yes or No.")
    if answer2 == 'yes':
        answer3 = input("Which would you like to separate? Images,Text, Videos,etc...")
        if answer3 == 'images':
            for file in files:
                dest = ""
                for ex in images:
                    if file.endswith(ex):
                        dest='../Images'
                        shutil.move(file,dest)
                        break
        elif answer3 == 'text':
            for file in files:
                dest = ""
                for ex in images:
                    if file.endswith(ex):
                        dest='../Text'
                        shutil.move(file,dest)
                        break

    print("Sorting the files...")

    for file in files:
        dest = ""
        for ex in images:
            if file.endswith(ex):
                dest='../Images'
                shutil.move(file,dest)
                break

        for ex in text:
            if file.endswith(ex):
                dest='../Text'
                shutil.move(file,dest)
                break

        for ex in sounds:
            if file.endswith(ex):
                dest='../Sounds'
                shutil.move(file,dest)
                break

        for ex in videos:
            if file.endswith(ex):
                dest='../Videos'
                shutil.move(file,dest)
                break

        for ex in applications:
            if file.endswith(ex):
                dest= '../Applications'
                shutil.move(file,dest)
                break

        for ex in codes:
            if file.endswith(ex):
                dest= '../Codes'
                shutil.move(file,dest)
                break

        if dest == "":
            shutil.move(file,'../Others')

    print("Sorting Completed...")