# path
import os
from typing import List

ROOT = "/Users/kang/Downloads/food-distinguisher/"
IMAGE_FOLDER_DIRECTORY = ROOT + "이미지/"

# restaurantFolderDirList[0] = '/content/drive/Shareddrives/coco 앱개발 대회/이미지/56.스노브/'


def restaurantFoldersInRoot() :
    restaurantFolderDirs = [IMAGE_FOLDER_DIRECTORY + folder + '/' for folder in os.listdir(IMAGE_FOLDER_DIRECTORY)]
    return restaurantFolderDirs
    

# 
def imgsInRestaurantFolder(restaurantFolderDirs : str) -> List[str] :
  result = []
  for imgFile in os.listdir(restaurantFolderDirs):
    result.append(restaurantFolderDirs + imgFile)
  return result



# for restaurantFolderDir in restaurantFolderDirs:
#    imgDirs = imgsInRestaurantFolder(restaurantFolderDir)
#    for imgDir in imgDirs:
#      print(imgDir)

if __name__ == "__main__":
    restaurantFolderDirs = restaurantFoldersInRoot()
    print(restaurantFolderDirs[0], end= '\n\n')
    imgFileDirs = imgsInRestaurantFolder(restaurantFolderDirs[0])
    print(imgFileDirs)