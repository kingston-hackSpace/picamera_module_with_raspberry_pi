#How to create an video feed using a pycamera module#

The pycamera can be connected to the raspberry pi board to allow inputs from the camera to be processed either as stills, or video footage. 

Hardware set up

Attach the camera to the raspberry pi board. The way to do this is detailed [here](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera?srsltid=AYCX9vIAeBAo3CVJufbke1-dF4icUpzVUu_WT819QYSwjU-tvcTHY6SA)

Connect the power supply and the monitor to the board.

Power on the raspberry pi and load up the terminal.

Set up a virtual environment and install the relevant libraries for help with this follow this link.

Load the python script above into the terminal. Either download or copy and paste into a script editor such as nano or py.

To run the script type

```python3 camera_test_2.py```

You should see the camera input displayed on the screen as a real time updated image.

How the script works.

The picam object referenced in the script returns a rectangle of pixel data as two dimensional array. This data is then sent to a window which is declared, where the pixel data is drawn to the screen. This process happens every cycle so the image updates and a the input from the camera updates in real time.
