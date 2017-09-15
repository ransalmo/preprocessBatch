import cv2
import numpy
import os
import uuid

class Preprocess(object):
    def __init__(self, source, destiny):
        self.sourcePath = source
        self.destinyPath = destiny

    def __getImageFiles(self, sourcePath):
        files = os.listdir(sourcePath)
        files = [os.path.join(sourcePath,f) for f in files if os.path.isfile(os.path.join(sourcePath, f)) and (f.upper().endswith('JPG') or (f.upper().endswith('PNG')))]
        return files

    def equalizeHistory(self):
        files = self.__getImageFiles(self.sourcePath)
        finalDestinyPath = self.destinyPath
        if not os.path.exists(self.destinyPath):
            finalDestinyPath = self.destinyPath+str(uuid.uuid4().hex)+'_equalized'
            os.makedirs(finalDestinyPath)
        for imagePath in files:
            img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
            equ = cv2.equalizeHist(img)
            newFile = os.path.join(finalDestinyPath, os.path.basename(imagePath))
            cv2.imwrite(newFile, equ)

    def setDestinyPath(self, path):
        self.destinyPath = path

    def setSourcePath(self, path):
        self.sourcePath = path
