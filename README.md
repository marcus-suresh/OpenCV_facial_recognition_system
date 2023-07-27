# 👁️ OpenCV Facial Recognition System 👥

Facial Recognition System uses OpenCV - a facial recognition application in Windows Subsystem for Linux 2.

## 🎯 Aim
The Facial Recognition System aims to detect trained faces in a given video file.

## 🧪 Solution
To achieve this aim, we have developed a Facial Recognition System that uses OpenCV's facial recognition functions to identify G20 World Leaders as they appear in various video clips. The rationale for this system is that, at various G20 World Leaders meetings, it can be challenging to know who is present in the video and bounded within specific frames. The solution includes a search system that can retrieve the name of the specific world leader as they prominently appear in a specific .mp4 file.

### 🪜 Implementation Steps
1. Build a Python virtual environment with Python 3.6.10.
2. Import OpenCV and other necessary dependency packages.
3. Build a database of known faces.
4. Import this database of known faces into the main program.
5. Ingest the input movie from the video sub-directory.
6. Split the input movie (.mp4) into individual frames.
7. Identify faces using OpenCV's facial recognition functions for each frame.
8. Compare the identified faces against the database of vectorized known faces.
9. If a match is found above a 0.5 tolerance level, draw a red box around the face's boundary with the name of the person appended to the box.
10. Repeat the process for all frames in the input movie.
11. Compile the new frames into a new video containing a box around the matched face, helping the user understand who is prominently featured.

## 📁 Files
There are two .py files included in this repository:
1. `**main_facial_recognition.py**`: This is the main facial recognition Python script responsible for detecting faces in the input video and drawing bounding boxes with names for identified world leaders.
2. `**g20_leaders_faces.py**`: This file contains a small database of vectorized faces belonging to various G20 world leaders. The main script uses this database for face comparison during the recognition process.

## 🚀 Getting Started
To use the Facial Recognition System, follow these steps:
1. Clone this repository to your local machine.
2. Ensure you have Python 3.6.10 installed on your system.
3. Create a virtual environment using Python 3.6.10 to avoid dependency conflicts.
4. Install the required OpenCV package and requisite dependencies using the following command:
  `pip install opencv-python` 

5. Place the input video (.mp4) you want to process in the "video" sub-directory.
6. Run the `main_facial_recognition.py` script to start the facial recognition process.

## ℹ️ Note
Please note that the accuracy of facial recognition may vary based on the quality of the input video and the completeness of the database of known faces. Additionally, the tolerance level of 0.5 for face matching can be adjusted to suit your specific use case.

Feel free to contribute to this project by expanding the database of known faces or by enhancing the recognition algorithm.

## 📄 License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

If you have any questions or suggestions, please feel free to contact us or open an issue.

Happy facial recognition! 😄👍
