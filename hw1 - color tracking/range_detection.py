import cv2

def callback(value):
    pass

def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars")
    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in range_filter:
            cv2.createTrackbar(
                f"{j}_{i}", "Trackbars", v, 255, callback
            )

def get_trackbar_values(range_filter):
    values = []
    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos(f"{j}_{i}", "Trackbars")
            values.append(v)
    return values

def main():
    range_filter = ["H", "S", "V"]
    cap = cv2.VideoCapture(0)
    setup_trackbars(range_filter)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_to_thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)
        thresh = cv2.inRange(
            frame_to_thresh,
            (v1_min, v2_min, v3_min),
            (v1_max, v2_max, v3_max)
        )

        cv2.imshow("Original", frame)
        cv2.imshow("Thresh", thresh)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()