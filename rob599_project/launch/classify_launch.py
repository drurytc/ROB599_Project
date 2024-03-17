import launch
import launch_ros.actions

def generate_launch_description():
    # Define actions for launching nodes
    sensor_node = launch_ros.actions.Node(
        package='rob599_project',
        executable='sensor_data',
        name='sensor_data'
    )

    classify_node = launch_ros.actions.Node(
        package='rob599_project',
        executable='classify',
        name='classify'
    )

    servo_node = launch_ros.actions.Node(
        package='rob599_project',
        executable='servo_control',
        name='servo_control'
    )

    # Create the launch description
    ld = launch.LaunchDescription()

    # Add nodes to the launch description
    ld.add_action(sensor_node)
    ld.add_action(classify_node)
    ld.add_action(servo_node)

    return ld
