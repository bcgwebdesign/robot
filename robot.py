from flask import Flask, request, render_template
from multiprocessing import Process
import easing
import sys, getopt
from time import sleep
from adafruit_servokit import ServoKit

DEBUG = False
SYNC_MOVES = True #ie synced moves take the same time
EASING = False

servo_count = 6
servo_speed = 1.0 # ie 1s to go 0 to 180 degrees
servo_step = 1
servo_range = 180

base = 90
shoulder = 180
elbow = 90
wrist = 90
grip_rotation = 20
gripper = 50

base_servo = 0
shoulder_servo = 1
elbow_servo = 2
wrist_servo = 3
grip_rotation_servo = 4
gripper_servo = 5



app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	global base,shoulder,elbow,wrist,grip_rotation,gripper
	
	if request.method == 'POST':
		new_base = int(request.form['base'])
		new_shoulder = int(request.form['shoulder'])
		new_elbow = int(request.form['elbow'])
		new_wrist = int(request.form['wrist'])
		new_grip_rotation = int(request.form['grip_rotation'])
		new_gripper = int(request.form['gripper'])
		target_array = [
			[base_servo, base, new_base],
			[shoulder_servo, shoulder,new_shoulder],
			[elbow_servo, elbow, new_elbow],
			[wrist_servo, wrist, new_wrist],
			[grip_rotation_servo, grip_rotation, new_grip_rotation],
			[gripper_servo, gripper, new_gripper]
		]
		moveto(target_array)

		base = new_base
		shoulder = new_shoulder
		elbow = new_elbow
		wrist = new_wrist
		grip_rotation = new_grip_rotation
		gripper = new_gripper

	return render_template('index.html', 
		base=base, 
		shoulder = shoulder,
		elbow = elbow,
		wrist = wrist,
		grip_rotation = grip_rotation,
		gripper = gripper
		)

@app.route('/hello', methods=['POST', 'GET'])
def hello_world():
	targets_first = [[0,45,135]]
	targets_second = [[0,135,45]]
	moveto(targets_first)
	moveto(targets_second)
	return "<p>Hello, World</p>"

@app.route('/inputs', methods=['POST', 'GET'])
def input_testing():
	servo = request.form['servo']
	return  servo + " was selected"


version = '1.0'
servo=0
angle=0

# 5 108 open 45 closed

targets_initial = [ 
	[5, 108, 108],
	[4, 10 , 10],
	[3, 150 , 150],
	[2, 160 , 180],
	[1, 140 , 180],
	[0, 90 , 90]
	]
targets_first = [ 
	[5, 50, 110],
	[4, 20 , 20],
	[3, 90 , 90],
	[2, 90 , 90],
	[1, 180 , 180],
	[0, 90 , 90]
	]
targets_second = [ 
	[5, 110, 50],
	[4, 20, 20],
	[3, 90 , 90],
	[2, 90 , 90],
	[1, 180 , 180],
	[0, 90 , 90]
	]

# command line options not always used for development
options, remainder = getopt.getopt(sys.argv[1:],'s:a:v', ['servo=', 'verbose', 'version=', 'angle=', ])
for opt, arg in options:
	if opt in('-s', '--servo'):
		servo = int(arg)
	elif opt in ('-a', '--angle'):
		angle = int(arg)
	elif opt =='--version':
		version = arg

def servomove(servo,start,finish):
	if SYNC_MOVES:
		linear_eta = servo_speed
	else:
		linear_eta = abs((finish - start) / servo_range * servo_speed )

	steps = abs((finish - start)/servo_step)

	print("ETA ",linear_eta) if DEBUG else None
	print("STEPS ",steps) if DEBUG else None

	if start>finish:
		print("BACKWARDS") if DEBUG else None
		loop_start = start - servo_step
		loop_finish = finish - servo_step
		loop_step = -1 * servo_step
	else:
		print("FORWARDS") if DEBUG else None
		loop_start = start + servo_step
		loop_finish = finish + servo_step
		loop_step = servo_step

	print("LOOP START ",loop_start) if DEBUG else None
	print("LOOP FINISH ",loop_finish) if DEBUG else None
	print("LOOP STEP ", loop_step) if DEBUG else None
	
	step = 1

	for i in range(loop_start, loop_finish, loop_step):
		
		sleep_time = linear_eta/steps
	
		eased = easing.easeInOutExpo(step,start, finish - start, steps, 6)

		# print(step, ' of ',steps,i, sleep_time, eased) if DEBUG else None

		if EASING: 
			newangle = eased 
		else:
			newangle = i
		
		kit.servo[servo].angle = newangle

		sleep(sleep_time)
		step+=1



### Servo setup
offset = 600
kit = ServoKit(channels=16)
for i in range(servo_count):
	kit.servo[i].actuation_range = servo_range
	kit.servo[i].set_pulse_width_range(1000-offset, 2000+offset)

kit.servo[1].actuation_range = 270


def main():
	print("do main?")

def moveto(target_array):
	proc=[]
	for target in target_array:
		p = Process(target=servomove,args=(target))
		proc.append(p)
	for p in proc:
		p.start()
	for p in proc:
		p.join()


if __name__ == '__main__':
	main()
	