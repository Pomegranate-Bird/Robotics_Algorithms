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
    



def main():
    simulation("racecar/racecar")

if __name__ == "__main__":
    main()
