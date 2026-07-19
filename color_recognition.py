import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# دالة لاكتشاف اللون
def detect_color(frame, hsv, lower, upper, color_name, box_color):

    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 1000:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)

            cv2.putText(
                frame,
                color_name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                box_color,
                2
            )


while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Green
    detect_color(
        frame,
        hsv,
        np.array([40, 50, 50]),
        np.array([80, 255, 255]),
        "Green",
        (0, 255, 0)
    )

    # Blue
    detect_color(
        frame,
        hsv,
        np.array([100, 150, 50]),
        np.array([140, 255, 255]),
        "Blue",
        (255, 0, 0)
    )

    # Yellow
    detect_color(
        frame,
        hsv,
        np.array([20, 100, 100]),
        np.array([35, 255, 255]),
        "Yellow",
        (0, 255, 255)
    )

    # Red (النطاق الأول)
    detect_color(
        frame,
        hsv,
        np.array([0, 120, 70]),
        np.array([10, 255, 255]),
        "Red",
        (0, 0, 255)
    )

    # Red (النطاق الثاني)
    detect_color(
        frame,
        hsv,
        np.array([170, 120, 70]),
        np.array([180, 255, 255]),
        "Red",
        (0, 0, 255)
    )

    cv2.imshow("Color Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()