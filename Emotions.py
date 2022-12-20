# Importando bibliotecas:
from deepface import DeepFace
import cv2
import mediapipe as mp

# Declarando detecção do rosto:
detros = mp.solutions.face_detection
rostos = detros.FaceDetection(min_detection_confidence= 0.8, model_selection=0)
# Desenho
dibujorostro = mp.solutions.drawing_utils

#webcam
cap = cv2.VideoCapture(0)

# começo
while True:
    # capituras de frame
    ret, frame = cap.read()
    # Lendo imagem
    img =cv2.imread("img.png")
    img = cv2.resize(img, (0, 0), None, 0.18, 0.18)
    ani, ali, c = img.shape

    # Correccion de color
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesamos
    resrostos = rostos.process(rgb)

    # Deteccion
    if resrostos.detections is not None:
        # Registramos
        for rosto in resrostos.detections:

            al, an, c = frame.shape
            box = rosto.location_data.relative_bounding_box
            xi, yi, w, h = int(box.xmin * an), int(box.ymin * al), int(box.width * an), int(box.height * al)
            xf, yf = xi + w, yi + h

            
            cv2.rectangle(frame, (xi, yi), (xf, yf), (255, 255, 0), 1)
            frame[10:ani + 10, 10:ali+10] = img

            # Informação
            info = DeepFace.analyze(rgb, actions=['gender', 'emotion'], enforce_detection= False)


            # Emoções
            emociones = info['dominant_emotion']

            # Genero
            gen = info['gender']
            #print(str(gen) + " de " + str(edad) + " años de edad, con estado de animo " + str(emociones) + " de etnia " + str(race))

            # Traduzindo
            if gen == 'Man':
                gen = 'Homem'

                # Emociones
                if emotions == 'angry':
                    emotions = 'nervoso'
                if emotions == 'disgust':
                    emotions = 'desgosto'
                if emotions == 'fear':
                    emotions = 'assustado'
                if emotions == 'happy':
                    emotions = 'feliz'
                if emotions == 'sad':
                    emotions = 'triste'
                if emotions == 'surprise':
                    emotions = 'surpreso'
                if emotions== 'neutral':
                    emotions = 'neutro'


            elif gen == 'Woman':
                gen = 'Mulher'

                # Emoçoes
                if emotions == 'angry':
                    emotions = 'nervoso'
                if emotions == 'disgust':
                    emotions = 'desgosto'
                if emotions == 'fear':
                    emotions = 'assustado'
                if emotions == 'happy':
                    emotions = 'feliz'
                if emotions == 'sad':
                    emotions = 'triste'
                if emotions == 'surprise':
                    emotions = 'surpreso'
                if emotions== 'neutral':
                   emotions = 'neutro'

                

            # Mostramos info
            cv2.putText(frame, str(gen), (65, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            cv2.putText(frame, str(emotions), (75, 135), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Mostrando Frames:
    cv2.imshow(" Deteção: ", frame)

    # tecla ESC
    t = cv2.waitKey(2)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()
