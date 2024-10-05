import cv2
import mediapipe as mp

# Initialize Mediapipe Hands
hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

# Finger tip landmarks
tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    # Convert image and process hand landmarks
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)

            fingers_up = [1 if handLms.landmark[tip].y < handLms.landmark[tip - 2].y else 0 for tip in tips]
            fingers_up.append(1 if handLms.landmark[4].x < handLms.landmark[3].x else 0)  # Thumb

            total_fingers = sum(fingers_up)
            cv2.putText(img, f'Fingers: {total_fingers}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Finger Count", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
