#from car import Car
import cv2
import numpy as np

frame = cv2.imread("lane_follow_test.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower = np.array([0, 0, 180])
upper = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lower, upper)

edges = cv2.Canny(mask, 200, 400)

roi = np.zeros_like(edges)
height, width = roi.shape
polygon = np.array([[
    (width, 0.25*height),
    (0, 0.25*height),
    (0, height),
    (width, height)
]], np.int32)
cv2.fillPoly(roi, polygon, 255)
cropped = cv2.bitwise_and(edges, roi)

segments = cv2.HoughLinesP(cropped, 1, np.pi/180, 10, np.array([]),
                           minLineLength=8, maxLineGap=8)

left = []
right = []
for segment in segments:
    x1, x2, y1, y2 = segment[0]
    fit = np.polyfit((x1,x2), (y1,y2), 1)
    slope, intercept = fit[0], fit[1]
    if slope < 0:
        left.append((slope, intercept))
    else:
        right.append((slope, intercept))
left_line = np.average(left, axis=0)
right_line = np.average(right, axis=0)

overlayed = np.copy(frame)
def draw_line(frame, slope, intercept, width, height):
    y1 = height
    y2 = y1 * 0.5
    x1 = max(-width, min(2*width, int((y1-intercept)/slope)))
    x2 = max(-width, min(2*width, int((y2-intercept)/slope)))
    cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 2)
draw_line(overlayed, left[0], right[1], width, height)
draw_line(overlayed, right[0], right[1], width, height)

cv2.imshow("Test Frame", overlayed)
cv2.waitKey(0)
cv2.destroyAllWindows()
