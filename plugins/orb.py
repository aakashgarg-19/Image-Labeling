from email.mime import image
from Helpers.person_extraction import PersonExtraction

import cv2
class ORB:
    def __init__(self,model_path,threshold):
        # self.pe = PersonExtraction(model_path=model_path)
        self.threshold=threshold
        pass

    def _extract_person(self,img_path):
        # racket,person,racket_mid,person_mid = self.pe.extract(img_path,0.75)
        # # cv2.imshow("person",person)
        # # cv2.waitKey()
        # return person
        pass
    def __detection(self,imageA,imageB):
        detect = cv2.ORB_create()
        keypointsA, descriptorA = detect.detectAndCompute(imageA,None)
        keypointsB, descriptorB = detect.detectAndCompute(imageB,None)
        return (keypointsA,descriptorA,keypointsB,descriptorB)
    
    def __Bf_mathcer(self, descA,descB):
        matcher=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
        no_of_matches=matcher.match(descA,descB)
        most_similar_regions=[i for i in no_of_matches if i.distance<50]
        return most_similar_regions,len(most_similar_regions)/len(no_of_matches)

    def __display_output(self,pic1,kpt1,pic2,kpt2,best_match):
        output_image = cv2.drawMatches(pic1,kpt1,pic2,kpt2,best_match[:],None,flags=2)
        cv2.imshow(output_image)
    
    def compare_images(self, imageA, imageB):
        # cv2.imshow(imageA)
        # cv2.imshow(imageB)
        # imgA=cv2.imread(imageA)
        # imgB=cv2.imread(imageB)
    
        key_ptA,descA,key_ptB,descB=self.__detection(imageA,imageB)
        no_of_matches ,orb_score = self.__Bf_mathcer(descA,descB)

        # self.__display_output(imageA,key_ptA,imageB,key_ptB,no_of_matches)

        return orb_score 

if __name__=='__main__':
    orb=ORB('../',50)
    p=orb.compare_images(cv2.imread('D:/image_labelling/ref_images/tennis/backhand/1.png'),cv2.imread('D:/image_labelling/ref_images/tennis/backhand/1.png'))
    print(p)

