import cv2

img = cv2.imread("images\ear.png")
print(type(img))

cv2.imshow('WHAT!?', img)
cv2.waitKey(0)

print(img.shape)

# Rectangle
cv2.rectangle(img, (10,0), (182,192), (255,0,0), 5)
cv2.imshow('WHAT rectangle!?',img)
cv2.waitKey(0)

# Text
cv2.putText(img, 'EAR!', (50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
cv2.imshow('That ear', img)
cv2.waitKey(0)

# Circle
cv2.circle(img, (75,75), 50, (0,255,255), 5)
cv2.imshow('Circle Ear', img)
cv2.waitKey(0)

# Save the progress
cv2.imwrite('images\ear_processed.png', img)
