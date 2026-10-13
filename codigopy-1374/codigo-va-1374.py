# Cristopher Lopez NC= 1374

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
carpeta_proyecto = Path(__file__).resolve().parent.parent

ruta_original = (
    carpeta_proyecto
    / "img-original-1374"
    / "img-gorila-1374.JPG"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-1374"
)

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img1374 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img1374 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_1374img1374 = cv2.rotate(
    img1374, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img1374.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_1374img1374 = cv2.warpAffine(
    img1374,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho
# y 500 píxeles de alto
img600x500_1374img1374 = cv2.resize(
    img1374, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200
# píxeles sobre una copia de la imagen original
img_rojo_1374img1374 = img1374.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_1374img1374,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("gorila original 1374", img1374)

cv2.imshow("gorila 90 1374", img90_1374img1374)

cv2.imshow("gorila 45 1374", img45_1374img1374)

cv2.imshow(
    "gorila 600x500 1374",
    img600x500_1374img1374
)

cv2.imshow("gorila rojo 1374", img_rojo_1374img1374)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-gorila1-1374.JPG"),
    img90_1374img1374
)

cv2.imwrite(
    str(carpeta_resultados / "img-gorila2-1374.JPG"),
    img45_1374img1374
)

cv2.imwrite(
    str(carpeta_resultados / "img-gorila3-1374.JPG"),
    img600x500_1374img1374
)

cv2.imwrite(
    str(carpeta_resultados / "img-gorila4-1374.JPG"),
    img_rojo_1374img1374
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()