  # -*- coding: utf-8 -*-
"""
Created on Mon 20 April 09:24:36 2020

@author: Marcus Suresh
COMP5425 Multimedia Retreival Homework 2

"""
import cv2
import face_recognition
import os

import known_faces #custom facial recognition dataset using vectorised facial encodings

# Ingest input_movie and capture frames
input_movie = cv2.VideoCapture( r'2_data\g20_video\trump_morrison_2.mp4',0)
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file with facial recognition
# Compile output movie at 640*360 resolution
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter(r'3_output\output.avi', fourcc, 29.97, (640, 360))

# ENTER YOUR SEARCH TERM HERE
#Select two faces that you want to search for in the input movie

searched_faces = [
    known_faces.Donald_Trump_face_encoding,
    #known_faces.Vladamir_Putin_face_encoding,
    #known_faces.Shinzo_Abe_face_encoding,
    #known_faces.Emmanual_Macron_face_encoding,
    #known_faces.Xi_Jinping_face_encoding,
    known_faces.Scott_Morrison_face_encoding,
    #known_faces.Bin_Salman_face_encoding
]

# Initialise variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    # Extract a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Terminate when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color to RGB color to make openCV compatible with Facial Recognition library
    rgb_frame = frame[:, :, ::-1]

    # Search all faces and face encodings present in the frame. 
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # Check the facial encodings in known_face.py for the face names.
        # Setting the tolerance limit. Higher limit means more erroneous match
        match = face_recognition.compare_faces(searched_faces, face_encoding, tolerance=0.60)

        name = None
        if match[0]:
            name = "Donald Trump"
        elif match[1]:
            name = "Scott Morrison"

        face_names.append(name)

    # Designing a system to label the identified results from known_faces.py
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the identified face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw label with the name of the identified face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Re-write image into frames with red box around identifeid face.
    print("Writing identified face to new frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

# Release input video and close windows
# New avi video saved to working directory
input_movie.release()
cv2.destroyAllWindows()