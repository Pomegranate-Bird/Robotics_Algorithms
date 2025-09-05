import numpy as np
import pybullet as p
import time
import pybullet_data


def simulation(robot_name: str):
    # Connect to graphical interface
    physics_client = p.connect(p.GUI)

    # Set search path for URDFs
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    # Set gravity in simulation
    p.setGravity(0, 0, -9.8)

    # Load ground plane
    plane_init_pos = [0, 0, 0]
    plane_orientation = p.getQuaternionFromEuler([0, 0, 0])
    plane_id = p.loadURDF("plane.urdf", plane_init_pos, plane_orientation)

    # Load robot
    robot_init_pos = [0, 0, 0]  # Slight elevation to avoid intersection
    robot_init_orientation = p.getQuaternionFromEuler([0, 0, 0])
    robot_id = p.loadURDF(robot_name + ".urdf", robot_init_pos, robot_init_orientation)

   #print_joint_information(robot_id)

    start_time = time.time()

    # Main simulation loop
    while True:
        #The Controller must be ran within the loop for continous updating
        t = time.time() - start_time
        p_controller(robot_id, t)
        p.stepSimulation()
        time.sleep(1 / 240)


def get_pose(robot_id): # Gives me the position of the robot within the Python Enviorment 
    pose = p.getBasePositionAndOrientation(robot_id)
    position = pose[0]
    orientation = pose[1]
    return position, orientation

def print_joint_information(robot_id):
    number_of_joints = p.getNumJoints(robot_id)
    print(f"The numnber of Joints: {number_of_joints}\n")

    for joint_index in range(number_of_joints):
        joint_info = p.getJointInfo(robot_id, joint_index)
        print(f" Printing joint information ({joint_info}, {joint_index})")
    

def circle_figure(t): # I just want to throw trajectories into the controller so I can make different ones and throw it into the same p-controller
    """Computes a circle trajectory with velocity and acceleration.
    
    Args:
        t (float): Time parameter.
        N (float, optional): Scaling factor for speed.
    
    Returns:
        tuple: (x_des, y_des, z_des, phi_d)
            - x_des, y_des, z_des: NumPy arrays containing position, velocity, and acceleration.
            - phi_d: Desired yaw angle.
    """
    N = 5 # Representing the radius of the circle 
    # Position 
    x_d = np.cos(t) * N 
    y_d = np.sin(t) * N
    


    # Velocity, I could possibly use the velocity when I actually have a working p_controller anbd trajectory 
    x_dot = -np.sin(t) * N
    y_dot = -np.cos(t) * N
    

    #Acceleration
    x_dd = -np.cos(t) * N
    y_dd = -np.sin(t) * N 
    
    

    position_desired = np.array([x_d, y_d])
    velocity_desired = np.array([x_dot,y_dot])
    acceleration_desired = np.array([x_dd,y_dd])

    # Desired yaw (phi_d) from velocity vector
    yaw_desired = np.arctan2(y_dot, x_dot)

    return position_desired, velocity_desired, acceleration_desired, yaw_desired


def gather_trajectory_data():

    # Creating some arrays for storing path information on Trajectory, Velocity and Error for plotting
    trajectory = []

    error = []

    velocity = []
    ...


def p_controller(robot_id, t):

    current_position, current_orientation  = get_pose(robot_id) # Getting the robot's position

    # Front wheel indexes 
    front_wheels = [2, 3]
    # Back wheel indexes 
    rear_wheels = [4, 5]

    steering_joints = [5, 7]

    euler = p.getEulerFromQuaternion(current_orientation)

    yaw_curr = euler[2]


    # Creating a time object that passes in the real time of the simulation 
    # Our trajectory is parametric in nature so we should follow the simulation time 
    
    

    position_desired, velocity_desired, acceleration_desired, yaw_desired = circle_figure(t)

    pos = np.array(current_position[:2])

    trajectory_error = position_desired - pos

    heading_error = yaw_desired - yaw_curr

    distance_error = np.linalg.norm(trajectory_error) # Getting Scalar Value from the trajectory error 

    tolerance = 1

    if(distance_error < tolerance):

        # Breaking of the robot
        p.setJointMotorControlArray(
                bodyUniqueId=robot_id,
                jointIndices=rear_wheels,
                controlMode=p.VELOCITY_CONTROL,
                targetVelocities=[0, 0])
        return


    k_v = 3  # Controller gain, to adjust changes in velocity error
    k_s = 10 # Controller gaim, to adjust the changes in the steering error

    velocity = k_v * distance_error 

    steering_angle = k_s * heading_error

    steering_angle = np.clip(steering_angle, -0.5, 0.5) # Restrict the steering of the robot 


    # Steering of the Robot from made from the two front wheels 
    p.setJointMotorControlArray(
        bodyUniqueId=robot_id,
        jointIndices = steering_joints,
        controlMode = p.POSITION_CONTROL,
        targetPositions= [steering_angle] * 2)
    
    # Setting wheel velocities on wheel joints 
    p.setJointMotorControlArray(
            bodyUniqueId = robot_id,
            jointIndices = rear_wheels,
            controlMode = p.VELOCITY_CONTROL,
            targetVelocities = [velocity] * 2)

    # Set the wheel velocities
    p.setJointMotorControlArray(
            bodyUniqueId = robot_id,
            jointIndices = front_wheels,
            controlMode = p.VELOCITY_CONTROL,
            targetVelocities = [velocity] * 2)




def main():
    simulation("racecar/racecar")

if __name__ == "__main__":
    main()
