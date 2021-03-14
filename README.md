# Speakly - A speech based note taking web app

### A brief summary of it's working:
- Converts Audio Signals to Digital output using the Fourier Transformation Algorithm
![alt text](https://miro.medium.com/max/3000/1*8e2saE05k0QxnAKqMBmhTA.png)
- Trains a pre trained image classifier CNN (Google's EfficentNetB7) on an expansive corpus of spectrogram data in order to transcribe our resultant spectrogram data with a very high level of accuracy
![alt text](https://miro.medium.com/max/3000/1*V2mgZ7y0ngd3q4DZ01xkEQ.png)
- Stores the transcribed text in a note taking app consisting of a Node.js Server using Express Framework and MongoDB and clean and user friendly UI/UX for the frontend

### Working with the following technologies:
- Tensorflow
![alt text](https://miro.medium.com/max/4112/1*YrvMKrWMhi3HomoiTLPsfw.png)
- Librosa
- Keras
![alt text](https://keras.io/img/logo.png)
- Node.js and Express.js
- Mongoose and MongoDB
- Passport's authentication
- EJS's templates

