import cv2
import numpy as np

# Load the images
cactus_big = cv2.imread('images\cactus_big.png', cv2.IMREAD_UNCHANGED)
cactus_sml = cv2.imread('images\cactus_small1.png', cv2.IMREAD_UNCHANGED)
dino_game  = cv2.imread('images\dino_game.png', cv2.IMREAD_UNCHANGED)

# Show main game image
# cv2.imshow('Game', dino_game)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Show search images
# cv2.imshow('Needle', cactus_sml)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Template Matching
# There are 6 comparison methods to choose from:
# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
# You can see the differences at a glance here:
# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
# Get results
result = cv2.matchTemplate(dino_game, cactus_sml, cv2.TM_CCOEFF_NORMED)
# cv2.imshow("Result", result)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Show values for results
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_loc)
print(max_val)

# Paint a square on the game (where the small cactus is)
# First get the width and height of the cactus
w = cactus_sml.shape[1]
h = cactus_sml.shape[0]
# cv2.rectangle(dino_game, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,0), 2)
# cv2.imshow('Rectangle on game', dino_game)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Play around with the threshold
# (It can find all 3 small cacti with one sample image)
threshold = .7
yloc, xloc = np.where(result >= threshold)
# See how many cacti it found
print(len(xloc))

for (x, y) in zip(xloc, yloc):
    cv2.rectangle(dino_game, (x, y), (x + w, y + h), (0,255,0), 2)

cv2.imshow('All rectangles', dino_game)
cv2.waitKey()
cv2.destroyAllWindows()

# Add rectangles to a matrix (So I can take out overlapping ones)
rectangles = []
for (x,y) in zip(xloc, yloc):
    rectangles.append([int(x),int(y),int(w),int(h)])
    rectangles.append([int(x),int(y),int(w),int(h)])

print(len(rectangles))

# Remove overlapping rectangles
rectangles, weights = cv2.groupRectangles(rectangles, 1, .2)
# Only 3 should remain
print(len(rectangles))
