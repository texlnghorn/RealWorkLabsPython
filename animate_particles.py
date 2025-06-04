#
# Converts a 2D array of particles into a string representation.
# If any sub-array contains 'R' (Right) or 'L' (Left) particles, it's represented as 'X'.
# Otherwise, it's represented as '.'.
#
# @param input_arr A 2D array where each sub-array contains particle directions ('R', 'L', or empty).
# @returns A string representing the particle layout (e.g., "X.X.X").
#
def particle_string(input_arr):
    output = ""
    for sub_arr in input_arr:
        if "R" in sub_arr or "L" in sub_arr:
            output += "X"
        else:
            output += "."
    return output


#
# Simulates the animation of particles moving left or right across a chamber.
# Particles move at a given speed, and their positions are recorded at each step.
#
# @param initialPosition A string representing the initial position of particles in a chamber and the direction they
# travel in the chamber. 'R' for right-moving, 'L' for left-moving, or an empty string/placeholder if no particle.
# @param speed The number of positions a particle moves per step.
# @returns A string array, where each string represents the particle layout at a specific step of the animation.
#
def animate(initial_position, speed):
    # A string array to store the steps of the particle animation.
    steps = []

    # current position is a 2-dimensional array of particle positions in the chamber.
    # Each inner array represents all the particles at a single position in the chamber.
    # Example: [['R'], [], ['L', 'R']] means 'R' at index 0, no particles at index 1, 'L' and 'R' at index 2.
    current_position = []

    # Initialize currentPosition based on initialPosition.
    # Each element of initialPosition becomes a sub-array in currentPosition.
    # If initialPosition[i] is 'R', then currentPosition[i] becomes ['R'].
    # If initialPosition[i] is 'L', then currentPosition[i] becomes ['L'].
    # If initialPosition[i] is '', then currentPosition[i] becomes [''].
    for direction in initial_position:
        current_position.append([direction])

    # Convert the initial 2D position array to a particle string representation.
    particle_str = particle_string(current_position)

    # Continue to evaluate the particle positions until all particles have exited the chamber.
    # 'X' in particle_str indicates there are still active particles in the chamber.
    while "X" in particle_str:
        # Add the current particle string to the steps array.
        steps.append(particle_str)

        # Initialize a new 2D array to store the particle positions for the next step.
        # It's pre-filled with empty arrays for each potential position.
        next_position = []
        for i in range(len(initial_position)):
            next_position.append([])

        # Iterate through the current particle positions to determine their next positions.
        for i, particles in enumerate(current_position):
            for particle in particles:
                # If the particle is moving Right, calculate its next index.
                if particle == "R":
                    # Check if the particle stays within the bounds of the chamber.
                    if i + speed <= len(initial_position) - 1:
                        next_position[i + speed].append("R")
                # If the particle is moving Left, calculate its next index.
                elif particle == "L":
                    # Check if the particle stays within the bounds of the chamber.
                    if i - speed >= 0:
                        next_position[i - speed].append("L")
                # Particles that have moved out of bounds are naturally excluded from nextPosition.

        # Reset the current position to be the calculated next position for the next iteration.
        current_position = next_position
        # Update the particle string representation for the new current position.
        particle_str = particle_string(current_position)
    steps.append(particle_str)
    return steps
