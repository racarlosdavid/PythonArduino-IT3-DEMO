import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import serial

#initialize serial port
ser = serial.Serial()
ser.port = 'COM3' #Arduino serial port
ser.baudrate = 9600
ser.timeout = 10 #specify timeout when using readline()
ser.open()

# Create figure for plotting
fig = plt.figure("IT3 G10 - Python Demo")
ax = fig.add_subplot(1, 1, 1)
xs = [] #time between data capture
ys = [] #store hart rate

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    #Aquire and parse data from serial port
    arduino_data = ser.readline()
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split(',') 
    i = int(list_values[0])
    relProb_float = float(list_values[1])
	
	# Add x and y to lists
    xs.append(i)
    ys.append(relProb_float)
 
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label="Heart Rate")

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Time')
    plt.ylabel('BPM')
    plt.legend()
    plt.axis([1, None, 0, 200]) #Use for arbitrary number of trials

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()