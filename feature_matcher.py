import cv2

img1 = cv2.imread('sample_totem.jpg', 0)
img2 = cv2.imread('IMG_20200917_115302 (copy).jpg', 0)

orb = cv2.ORB_create(nfeatures=500)
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# matcher takes normType, which is set to cv2.NORM_L2 for SIFT and SURF, cv2.NORM_HAMMING for ORB, FAST and BRIEF
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
print(matches)
# draw first 50 matches
match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)
match_img = cv2.resize(match_img,(1200,600))
cv2.imwrite("feature_match_ouytput.jpg", match_img)
cv2.imshow('Matches', match_img)
cv2.waitKey(5)