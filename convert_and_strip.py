from wand.image import Image
import os, datetime
import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% [{iteration}/{total}] {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

sourceDir = os.path.join(os.getcwd(), 'input')
exportDir = os.path.join(os.getcwd(), 'output',datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
originalsDir = os.path.join(os.getcwd(), 'originals',datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(exportDir)
os.makedirs(originalsDir)

filesConverted = 0

sourceFiles = os.listdir(sourceDir)
numSourceFiles = len(sourceFiles)
print(f"Copying and Converting [{str(numSourceFiles)}] Files")
printProgressBar(0, numSourceFiles, prefix = 'Progress:', suffix = 'Converted', length = 36)

for index, file in enumerate(sourceFiles):
    sourceFile=sourceDir + "/" + file
    originalCopyFile=originalsDir + "/" + file
    targetFile=exportDir + "/" + file.replace(".HEIC",".JPG").replace(".webp",".JPG").replace(".jpeg",".JPG").replace(".jpg",".JPG").replace(".png",".JPG").replace(".gif",".JPG").replace(".tiff",".JPG").replace(".tif",".JPG").replace(".heic",".JPG").replace(".heif",".JPG").replace(".heic",".JPG").replace(".GIF",".JPG").replace(".TIF",".JPG").replace(".TIFF",".JPG").replace(".PNG",".JPG").replace(".BMP",".JPG")

    img=Image(filename=sourceFile)
    img.save(filename=originalCopyFile)
    img.format='jpg'
    img.strip()
    img.save(filename=targetFile)
    img.close()
    filesConverted += 1
    time.sleep(0.1)
    printProgressBar(index + 1, numSourceFiles, prefix = 'Progress:', suffix = 'Converted', length = 36)

print(f"Removing [{str(numSourceFiles)}] Original Files")
printProgressBar(0, numSourceFiles, prefix = 'Progress:', suffix = 'Removed', length = 50)
for index, file in enumerate(sourceFiles):
    os.remove(os.path.join(sourceDir, file))
    printProgressBar(index + 1, numSourceFiles, prefix = 'Progress:', suffix = 'Removed', length = 50)