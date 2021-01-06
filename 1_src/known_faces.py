  # -*- coding: utf-8 -*-
"""
Created on Mon 20 April 09:24:36 2020

@author: Marcus Suresh
COMP5425 Multimedia Retreival Homework 2

"""

import cv2
import face_recognition
import os

# Load training images of G20 world leaders and use face encoder to vectorise.
test_person_image = face_recognition.load_image_file(r'2_data\g20_leaders\test_person.jpg')
test_person_face_encoding = face_recognition.face_encodings(test_person_image)[0]

Donald_Trump_image = face_recognition.load_image_file(r'2_data\g20_leaders\trump.jpg')
Donald_Trump_face_encoding = face_recognition.face_encodings(Donald_Trump_image)[0]

Shinzo_Abe_image = face_recognition.load_image_file(r'2_data\g20_leaders\shinzo.jpg')
Shinzo_Abe_face_encoding = face_recognition.face_encodings(Shinzo_Abe_image)[0]

Emmanuel_Macron_image = face_recognition.load_image_file(r'2_data\g20_leaders\macron.jpg')
Emmanuel_Macron_face_encoding = face_recognition.face_encodings(Emmanuel_Macron_image)[0]

Xi_Jinping_image = face_recognition.load_image_file(r'2_data\g20_leaders\xi.jpg')
xi_Jinping_face_encoding = face_recognition.face_encodings(Xi_Jinping_image)[0]

Bin_Salman_image = face_recognition.load_image_file(r'2_data\g20_leaders\bin_salman.jpg')
Bin_Salman_face_encoding = face_recognition.face_encodings(Bin_Salman_image)[0]

Justin_Trudeau_image = face_recognition.load_image_file(r'2_data\g20_leaders\justin.jpg')
Justin_Trudeau_face_encoding = face_recognition.face_encodings(Justin_Trudeau_image)[0]

Scott_Morrison_image = face_recognition.load_image_file(r'2_data\g20_leaders\morrison.jpg')
Scott_Morrison_face_encoding = face_recognition.face_encodings(Scott_Morrison_image)[0]

Vladamir_Putin_image = face_recognition.load_image_file(r'2_data\g20_leaders\putin.jpg')
Vladamir_Putin_face_encoding = face_recognition.face_encodings(Vladamir_Putin_image)[0]

Lee_Loong_image = face_recognition.load_image_file(r'2_data\g20_leaders\lee_loong.jpg')
Lee_Loong_face_encoding = face_recognition.face_encodings(Lee_Loong_image)[0]
