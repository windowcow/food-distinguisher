# path
import os
from typing import List
import foodchecker
import shutil

ROOT = "/Users/kang/Downloads/food-distinguisher/"
IMAGE_FOLDER_DIRECTORY = ROOT + "이미지/"
SORTED_FOOD_IMAGE_FOLDER_DIRECTORY = ROOT + "sortedimgs/food/"
SORTED_NON_FOOD_IMAGE_FOLDER_DIRECTORY = ROOT + "sortedimgs/nonfood/"
ERROR_FOLDER_DIRECTORY = ROOT + "sortedimgs/error/"
RESTAURANT_NAME_LIST : List[str] = os.listdir(IMAGE_FOLDER_DIRECTORY)


# # 폴더 만들기 위한 코드
# os.mkdir(ERROR_FOLDER_DIRECTORY)

# for restaurantName in RESTAURANT_NAME_LIST:
#     os.mkdir(ERROR_FOLDER_DIRECTORY + restaurantName)
# #     os.mkdir(SORTED_NON_FOOD_IMAGE_FOLDER_DIRECTORY + restaurantName)

# 
def imgFiles(restaurantFolderDir : str) -> List[str] :
    """_summary_

    Args:
        restaurantFolderDir (str): 디렉토리 경로

    Returns:
        List[str]: 단순히 디렉토리 내 파일 이름이 들은 리스트만 반환한다
    """
    result = []
    for imgFile in os.listdir(restaurantFolderDir):
        result.append(imgFile)
    return result

# def restaurantFolderPathsInRoot() :
#     restaurantFolderDirs = [IMAGE_FOLDER_DIRECTORY + restaurant + '/' for restaurant in RESTAURANT_NAME_LIST]
#     return restaurantFolderDirs


    





# for restaurantFolderDir in restaurantFolderDirs:
#    imgDirs = imgsInRestaurantFolder(restaurantFolderDir)
#    for imgDir in imgDirs:
#      print(imgDir)

if __name__ == "__main__":
    for restaurant in RESTAURANT_NAME_LIST:
        restaurantInImageFolder = IMAGE_FOLDER_DIRECTORY + restaurant + '/'
        restaurantInSortedFoodFolder = SORTED_FOOD_IMAGE_FOLDER_DIRECTORY + restaurant + '/'
        restaurantInSortedNonFoodFolder = SORTED_NON_FOOD_IMAGE_FOLDER_DIRECTORY + restaurant + '/'
        errorFolder = ERROR_FOLDER_DIRECTORY + restaurant + '/'
        
        imgListForSpecificRestaurant = imgFiles(restaurantInImageFolder)
        
        for i in range(len(imgListForSpecificRestaurant)):
            try:
                isFood = foodchecker.isItFood(restaurantInImageFolder + imgListForSpecificRestaurant[i]) == True
            except:
                shutil.copy(restaurantInImageFolder + imgListForSpecificRestaurant[i], errorFolder + imgListForSpecificRestaurant[i])
                continue
            
            if isFood:
                shutil.copy(restaurantInImageFolder + imgListForSpecificRestaurant[i], restaurantInSortedFoodFolder + imgListForSpecificRestaurant[i])
            else:
                shutil.copy(restaurantInImageFolder + imgListForSpecificRestaurant[i], restaurantInSortedNonFoodFolder + imgListForSpecificRestaurant[i])