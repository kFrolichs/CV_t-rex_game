import cv2

# Importing an image into cv2
img = cv2.imread('images/banana.png')
print(img)

# Looking at the size and type of imported image
print(type(img))
print(img.shape)

# Showing the image with cv2
# cv2.imshow("Original", img)
# cv2.waitKey(0) # Waits until keypress

# Resizing the image
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# cv2.imshow("Small Image", small)
# cv2.waitKey(0)
print(small.shape)

# Take a look at the first pixel
print(small[0,0])
small[0,0] = (255,255,255)
# cv2.imshow("Small Image", small)
# cv2.waitKey(0)
print(small[0,0])

# Change first 90 rows and 10 columns to red
small[0:90,0:10] = (0, 0, 255)
# cv2.imshow("Small Image", small)
# cv2.waitKey(0)

# Grayscale an image
gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
print(gray.shape)

cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Saving the image
cv2.imwrite("images\gray.png", gray)
