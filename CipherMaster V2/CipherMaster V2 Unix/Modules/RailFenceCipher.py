name = "Rail Fence"
info = "Writes text in a zigzag pattern and reads it row by row."
command = "rai"

def encrypt(text):
    rails = int(input("Enter Rails amount: "))
    fences = ["" for _ in range(rails)]
    step = 1
    current_rail = 0
    
    for char in text:
        fences[current_rail] += char
        current_rail += step
        if current_rail == 0 or current_rail == rails - 1:
            step = -step
    
    return "".join(fences)

def decrypt(ciphertext):
    rails = int(input("Enter Rails amount: "))
    grid = [[None] * len(ciphertext) for _ in range(rails)]
    row = 0
    direction = 1

    for col in range(len(ciphertext)):
        grid[row][col] = '*'
        row += direction
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if grid[r][c] == '*' and index < len(ciphertext):
                grid[r][c] = ciphertext[index]
                index += 1
    result = []
    row = 0
    direction = 1

    for col in range(len(ciphertext)):
        result.append(grid[row][col])
        row += direction
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

    return "".join(result)