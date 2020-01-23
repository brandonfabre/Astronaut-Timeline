import face_recognition as fr
import os
import cv2
import numpy as np
from FileIO import appendToFile, fileContains

def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./astronautFaces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("astronautFaces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("astronautFaces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding

def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]
 
    face_locations = fr.face_locations(img)
    unknown_face_encodings = fr.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = fr.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = fr.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        astronautsNames = "astronautNames.txt"
        if name != "Unknown":
            face_names.append(name)
            if not fileContains("astronautPictures/" + name + ".txt", im):
                appendToFile("astronautPictures/" + name + ".txt", im)
            if not fileContains(astronautsNames, name):
                appendToFile(astronautsNames, name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 1)


    # Display the resulting image
    # while True:
    #     cv2.imshow('Image', img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         return face_names

images = [#"issPictures/1.jpg", "issPictures/2.jpg", "issPictures/3.jpg", "issPictures/4.jpg",
          "issPictures/5.jpg", "issPictures/6.jpg", "issPictures/7.jpg", "issPictures/8.jpg",
          "issPictures/9.jpg", "issPictures/10.jpg", "issPictures/11.jpg", "issPictures/12.jpg",
          "issPictures/13.jpg", "issPictures/14.jpg", "issPictures/15.jpg", "issPictures/16.jpg",
          "issPictures/17.jpg", "issPictures/18.jpg", "issPictures/19.jpg", "issPictures/20.jpg",
          "issPictures/21.jpg", "issPictures/22.jpg"]

for image in images:
    print(classify_face(image))