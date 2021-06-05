# Project: GamseeAI

### Devpost Link: https://devpost.com/software/gamseeai-ah5o14

### What is GamseeAI?

**GameseeAI** is surveillance application that can be used to look after your belongings that you leave in a public space. It uses the webcam on the users device to keep track of the items with in its field of view and saves a recording of it. If the application detects any kinds of motions it takes a picture of what it saw and sends a notification to the user about the suspicious movements in its field of view. 

### Preview
[GamseeAI Demonstration Video](https://youtu.be/wV2nfF89Wwk)

### How to use

1. Go to the [Project Website](https://jjangsta.github.io/GamseeAI/) download the GamseeAI.exe
2. Run the GamseeAI.exe file
3. After running the executable file, enter a valid email to recieve notifications
4. Let the program run for as long as you want to

### How we built it

We primarily used Python and its various modules to develop GamseeAI. As we had just learned Python at UTSC from CSCA08, we had absolutely no past experience with these modules. GamseeAI uses the OpenCV module which helps us to identify any motion proximal to the device, and take a photo of the activity. Furthermore, we used the smtplib module to send an email notification to the user of the device alarming him about the suspicious activity by attaching the image taken by the app before.

### Credit and Contact

- @jjangsta (Peter)
- @ShawnGeorge03 (Shawn)
- @shashwat-doshi (Shashwat)
- @tapasrastogi2411 (Tapas)
