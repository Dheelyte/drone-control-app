# Tello Drone Control Application

<p align="center">
  <img width="100%" src="https://github.com/Dheelyte/drone-control-app/blob/master/CameraFeed/Images/drone1.jpg?raw=true">
  <img width="100%" src="https://thedronestop.com/wp-content/uploads/2022/08/ryze-tello-1.webp">
</p>

## Demo
Watch a video of me controlling a Tello Drone with the Tello Drone Control Application:

[Watch Video](https://twitter.com/Unilag_Design/status/1621471823610134529?t=3eHWWmMV9S67K3w30pzeug&s=19)

## Installation
Install the project dependencies.
Make sure you have Python and pip installed. It is advisable to install the requirements file in a virtual environment

```pip install -r requirements.txt```

## Usage
First connect to the Tello drone then run the Drone control application

```python app.py```

## App objectives
The objective of this app was to design, develop and deploy the Tello Drone Control application, a cross-platform software for connecting and controlling the Tello Drone in real-time. This included development of requirement specifications for the app, prototype design, and field testing.
Prototype design was central to this project, as the goal of this application was to provide a tangible software deliverable that is close to being deployment ready. The field testing was important for demonstrating the app in a live and demanding environment.

## App Development Process
The Tello Drone Control Application was made with:
- Python, a popular high-level, general purpose programming language.
- Tkinter, a Python library used for Developing Desktop applications.

I followed a modular design approach to enable seamless future expansion of the app.
The Tello Drone Control Application consists of three main modules, as shown in Figure 1.0: frontend and backend. The frontend module allows users to connect and interact with the app via a graphical user interface (GUI). The frontend also contains a video frame to view the surveillance feed from the drone’s mounted camera right in the application. A variety of layouts and user interface elements, including Buttons, frame, grids and Labels, were used to improve the user friendliness of the frontend module.
The backend module is responsible for connecting and sending various movement signals to the drone.
On the frontend, the application contains the following drone control buttons:
-	`Takeoff`: This is used to make the drone take off.
-	`Forward`: This is used for the drone’s forward movement
-	`Backward`: This is used for the drone’s backward movement
-	`Left`: This is clicked to make the drone move left (without rotating)
-	`Right`: This is clicked to make the drone move right (without rotating)
-	`Rotate Left`: This is clicked to make the drone rotate left.
-	`Rotate Right`: This is clicked to make the drone rotate right.
-	`Upward`:  This is clicked to make the drone move upward.
-	`Downward`: This is clicked to make the drone move upward.
-	`Land`: This is clicked to make the drone land.

## Key Outcomes
The outcome of this project is a fully-functioning cross-platform application for controlling the Tello Drone. The application is enabled with functionalities for managing the signals sent to the drone in real-time.
The application supports the following drone movements: take off, forward movement, backward movement, left movement, right movement, left rotation movement, right rotation movement, upward movement, downward movement, and the landing.
Users of the application can also view live surveillance feed from the drone right in the application. This makes the drone easier to control when it is out of sight.
The key components of the application is shown in the screenshot below.


## User-friendliness
To evaluate the Tello Drone Control application’s user-friendliness, I surveyed a number of students with some knowledge about drone control. Each user was first briefed on the purpose of the app and then allowed to navigate the app without any further assistance from me (the app developer).
After the survey was completed, five users out of five users were able to control the drone the application without any assistance. This shows that the components and buttons of the app were easy to use and intuitive.
The real-time surveillance feed from the drone made the controlling of the drone even easier because a user does not have to look at the drone while controlling it but could just look at the surveillance feed from the camera through the application.

## Recommendations and Limitations
One of the key bottlenecks I encountered while designing the Drone Control application was the Drone’s reliance on Wireless Fidelity (WiFi) as its only means of connecting to the drone. I flagged this as a limitation because I noticed some devices don’t have WiFi installed on them (for some reason). Therefore such devices would not be able to use the application I developed.
Another limitation I faced during the development of the application was the time the compiler had to take in order to compile and build the application due to some computer hardware limitations on my end.

## Scalability
To evaluate the scalability of the app, I monitored the latency between the time a user clicks a button that signals drone movement and the time taken for the drone to receive the signal and make the movement.
It was noticed that the latency observed increased as the distance between the drone and the ground station increased. It is important to note that these latencies could be due to WiFi speed of the ground station, which the application had no control over.
A high-performance ground station could be used to reduce latencies and thereby increase the scalability of the app.

## Contributor
[Delight Gbolahan Olu-Olagbuji](https://github.com/Dheelyte)

## Connect with me
<a href="https://twitter.com/DelightGbolahan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="Delight on Twitter" width="50" /></a>
<a href="https://linkedin.com/in/delight-olu-olagbuji-84051b193" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Delight on LinkedIn" width="50" height="40" /></a>
<a href="mailto:olagbujidelight@gmail.com" target="blank"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/512px-Gmail_icon_%282020%29.svg.png?20221017173631" alt="Delight on LinkedIn" width="50" /></a>
<a href="https://delighto.hashnode.dev" target="blank"><img align="center" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1611902473383/CDyAuTy75.png?auto=compress" alt="Delight on LinkedIn" width="50" /></a>
