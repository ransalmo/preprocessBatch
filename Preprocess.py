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

    def __setupExceution(self, prefix):
        files = self.__getImageFiles(self.sourcePath)
        finalDestinyPath = self.destinyPath
        if not os.path.exists(self.destinyPath):
            finalDestinyPath = self.destinyPath + str(uuid.uuid4().hex) + prefix
            os.makedirs(finalDestinyPath)
        return [finalDestinyPath, files]

    def equalizeHistory(self):
        path, files = self.__setupExceution('equalize_hist')
        for imagePath in files:
            img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
            equ = cv2.equalizeHist(img)
            newFile = os.path.join(path, os.path.basename(imagePath))
            cv2.imwrite(newFile, equ)

    def claheEqualization(self):
        path, files = self.__setupExceution('clahe_grey')
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        for imagePath in files:
            img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
            cla = clahe.apply(img)
            newFile = os.path.join(path, os.path.basename(imagePath))
            cv2.imwrite(newFile, cla)

    def adaptiveThreshold(self):
        path, files = self.__setupExceution('adaptive_grey')
        for imagePath in files:
            img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
            th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.cv2.THRESH_BINARY)
            newFile = os.path.join(path, os.path.basename(imagePath))
            cv2.imwrite(newFile, th)


    def claheColor(self):
       path, files = self.__setupExceution('clahe_col')
       clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
       for index, imagePath in enumerate(files):
            print('Processing {0} from {1}'.format(index, len(files)))
            img = cv2.imread(imagePath, 1)
            labImg = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(labImg)
            cl = clahe.apply(l) #use clahe in the l channel
            merged = cv2.merge((cl, a, b))
            #back to rgb
            finalRGB = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)
            #write file
            newFile = os.path.join(path, os.path.basename(imagePath))
            cv2.imwrite(newFile, finalRGB)


    def setDestinyPath(self, path):
        self.destinyPath = path

    def setSourcePath(self, path):
        self.sourcePath = path
