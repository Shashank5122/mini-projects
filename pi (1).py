import cv2

# Read image
im = cv2.imread("2.jpg")

ds = cv2.bilateralFilter ( im,9,100, 70, 200 )
ds = cv2.edgePreservingFilter(ds, flags=2, sigma_s=80, sigma_r=0.4)
cv2.imshow("filter", ds)
cv2.waitKey(0)
cv2.destroyAllWindows()
