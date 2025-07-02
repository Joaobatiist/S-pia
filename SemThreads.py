import cv2
import numpy as np
import time

def aplicar_sepia(imagem):
    kernel_sepia = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
    ])
    sepia = cv2.transform(imagem, kernel_sepia)
    return np.clip(sepia, 0, 255).astype(np.uint8)

imagem = cv2.imread("img/zebraColorida.jpg")

if imagem is None:
    print("Erro: imagem não encontrada.")
else:
    cv2.imshow("Imagem Original", imagem)
    print("Pressione ESC para aplicar o filtro sépia...")

    while True:
        key = cv2.waitKey(1)
        if key == 27:  
            cv2.destroyWindow("Imagem Original")
            break

    print("Aplicando filtro sépia...")
    inicio = time.time()
    imagem_sepia = aplicar_sepia(imagem)
    fim = time.time()
    print(f"Tempo sem thread: {fim - inicio:.4f} segundos")

    cv2.imshow("Imagem com Sépia (Sem Thread)", imagem_sepia)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
