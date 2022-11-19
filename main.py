import cv2

circle = cv2.imread('circle.png')
star = cv2.imread('star.png')

same_image = cv2.subtract(circle, circle)

cv2.imshow('same_image', same_image)

def_image = cv2.subtract(star, circle)

cv2.imshow('def_image', def_image)
# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
