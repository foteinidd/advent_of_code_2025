def find_password_part1(filename):
    """
    Simulate the dial rotations and count how many times it points at 0.
    The dial has positions 0-99 in a circle.
    """
    position = 50  # Starting position
    count_zeros = 0

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                # Parse the rotation
                direction = line[0]  # 'L' or 'R'
                distance = int(line[1:])

                # Apply rotation
                if direction == 'L':
                    position = (position - distance) % 100
                else:  # direction == 'R'
                    position = (position + distance) % 100

                # Check if we're at 0
                if position == 0:
                    count_zeros += 1

        return count_zeros

    except FileNotFoundError:
        print(f"File {filename} not found. Make sure your input is in input.txt")
        return None


def find_password_part2(filename):
    """
    Count every time the dial points at 0 during rotations.
    This includes both the end positions and all positions crossed during rotation.
    """
    position = 50  # Starting position
    count_zeros = 0

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                # Parse the rotation
                direction = line[0]  # 'L' or 'R'
                distance = int(line[1:])

                # Count how many times we pass through 0 during this rotation
                if direction == 'L':
                    # Rotating left (subtracting)
                    for _ in range(distance):
                        position = (position - 1) % 100
                        if position == 0:
                            count_zeros += 1
                else:  # direction == 'R'
                    # Rotating right (adding)
                    for _ in range(distance):
                        position = (position + 1) % 100
                        if position == 0:
                            count_zeros += 1

        return count_zeros

    except FileNotFoundError:
        print(f"File {filename} not found. Make sure your input is in input.txt")
        return None


if __name__ == "__main__":
    result_part1 = find_password_part1("input.txt")
    if result_part1 is not None:
        print(f"Part 1 - The password is: {result_part1}")
    
    result_part2 = find_password_part2("input.txt")
    if result_part2 is not None:
        print(f"Part 2 - The password is: {result_part2}") 
