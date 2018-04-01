# classifiers
Machine learning classifiers
This model will predict the song's genre based on current activity of user.
Currently the model can predict 'rock', 'jazz', 'classical' or 'pop' genre.
This can be expanded easily by enriching the dataset.

Running command- 
python moodDetection.py

This will start the server on your machine and will listen on port 8000.

Sample queries if server is running on local machine:
http://localhost:8000/detectMood?heartRate=medium&gender=male&location=home&time=morning&age=21-30

Update the path in the python file for trainingX.txt and trainingY.txt
The training dataset can be expanded by taking various other samples.
We have collected the initial sample by the survey.
