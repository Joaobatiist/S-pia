import cv2
import numpy as np
import threading

def aplicar_sepia(frame):
    kernel_sepia = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
    ])
    sepia = cv2.transform(frame, kernel_sepia)
    return np.clip(sepia, 0, 255).astype(np.uint8)


def processar_sepia():
    global frame, rodando
    while rodando:
        if frame is not None:
            sepia = aplicar_sepia(frame)
            cv2.imshow("Sepia ", sepia)
        if cv2.waitKey(1) & 0xFF == 27:  
            rodando = False
            break

cap = cv2.VideoCapture(0)
rodando = True
frame = None


thread = threading.Thread(target=processar_sepia)
thread.start()

while rodando and cap.isOpened():
    ret, frame_atual = cap.read()
    if not ret:
        break
    frame = frame_atual.copy()
    cv2.imshow("Original", frame)

    if cv2.waitKey(1) & 0xFF == 27: 
        rodando = False
        break

cap.release()
cv2.destroyAllWindows()
