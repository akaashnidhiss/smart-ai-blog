# Speakly - A speech based note taking web app

### A brief summary of it's working:
- Converts Audio Signals to Digital output using the Fourier Transformation Algorithm
- Trains a pre trained image classifier CNN (Google's EfficentNetB7) on an expansive corpus of spectrogram data in order to transcribe our resultant spectrogram data with a very high level of accuracy
- Stores the transcribed text in a note taking app consisting of a Node.js Server using Express Framework and MongoDB and clean and user friendly UI/UX for the frontend

### Working with the following technologies:
- Tensorflow
- Librosa
- Keras
- Node.js and Express.js
- Mongoose and MongoDB
- Passport's authentication
- EJS's templates