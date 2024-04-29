import math
print("PROJECTILE MOTION")
def find_initial_velocity_and_angle(range_, max_height):
    g = 9.81  # acceleration due to gravity (m/s^2)

    # Solving for launch angle (theta) using the equation for max height
    theta = math.atan((4 * max_height) / range_)

    # Solving for initial velocity (u) using the launch angle
    u = math.sqrt((range_ * g) / math.sin(2 * theta))

    # Converting angle from radians to degrees
    theta_deg = math.degrees(theta)

    return u, theta_deg

# Example usage
range_input = float(input("Enter the horizontal range (meters): "))
max_height_input = float(input("Enter the maximum height (meters): "))

initial_velocity, launch_angle = find_initial_velocity_and_angle(range_input, max_height_input)

print("Initial velocity:", initial_velocity, "m/s")
print("Launch angle:", launch_angle, "degrees")


