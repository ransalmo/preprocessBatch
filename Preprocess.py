import cv2
import numpy
import os

class Preprocess(object):
    def __init__(self, source, destiny):
        self.sourcePath = source
        self.destinyPath = destiny

    def __getImageFiles(self):
        files = os.listdir(self.sourcePath)
        files = [os.path.join(self.sourcePath,f) for f in files if os.isfile(os.path.join(self.sourcePath, f)) and (f.upper().endswith('JPG') or (f.upper().endswith('PNG')))]
        return files

    def equalizeHistory(self):
        files = self.__getImageFiles(self.sourcePath)
        if not os.path.exists(self.destinyPath):
            os.makedirs(self.destinyPath)
        for imagePath in files:
            img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
            equ = cv2.equalizeHist(img)
            newFile = os.join(self.destinyPath, os.path.basename(imagePath))
            cv2.imwrite(newFile, equ)

    def setDestinyPath(self, path):
        self.destinyPath = path

    def setSourcePath(self, path):
        self.sourcePath = path
