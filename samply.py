from PIL import Image
import os
from os.path import splitext

def getDictOfFoldersAndImages(inputFolderPaths)->dict():
    returnDict = {}
    for folder in inputFolderPaths:
        key = folder.split('\\')[-1]
        if key not in returnDict.keys():
            returnDict[key] = None
        returnDict[key] = (os.listdir(folder))
    return returnDict

def convertAllFilesToPNG(path, files_dict):
    def convertImageToPNG(imageToConvert)->None:
        root, extension = splitext(imageToConvert)
        if extension != '.png':
            try:
                im = Image.open(root + extension)
                im.save(root + '.png')
            except OSError:
                print('Cannot convert ' + root + extension)

    for category, items in files_dict.items():
        for item in items:
            convertImageToPNG(path + category + '\\' + item)

def getImageSize(templateSelected):
    # Sizes in Pixels
    templates = {
        'CryptoPunks': (336,336),
        'BoredApeYatchClub': (631, 631),
        'NFTuxedoCats': (1000, 1300)
    }
    if templateSelected in templates.keys():
        return templates[templateSelected]
    else:
        return (0,0)

def reziseAllImages(path, files_dict, imageSize):
    def resizeImage(imageToResize, newSize):
        # AntiAlias used to improve quality of reduced size images
        return imageToResize.resize(newSize, Image.ANTIALIAS)

    for category, items in files_dict.items():
        for item in items:
            old_image = Image.open(path + category + '\\' + item)
            new_image = resizeImage(old_image, imageSize)
            new_image.save(path + category + '\\' + item)

def removeNonPNGFromFiles(files_dict):
    for folder, files in files_dict.items():
        for fi in files:
            if not fi.endswith('.png'):
                files_dict[folder].remove(fi)

def overlayImages(path, image_list):


def main():
    path = os.path.dirname(__file__) + '\\img\\'
    folders = [path + folder for folder in ['backgrounds', 'clothes', 'hats', 'base']]
    files = getDictOfFoldersAndImages(folders)

    # If images are stored in different image formats than PNG:
    # convertAllFilesToPNG(path, files)

    removeNonPNGFromFiles(files)

    # If images need to be resized:
    # images_size = getImageSize('BoredApeYatchClub')
    # reziseAllImages(path, files, images_size)

    

if __name__ == "__main__":
    main()

