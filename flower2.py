import os
import time
import random

def clear_screen():
    """Clear the console screen."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def display_flower(size=1):
    """Display a beautiful flower with stem and leaves using ASCII characters."""
    # Flower parts (using only standard characters)
    flower_center = "@"
    petal = "*"
    stem = "|"
    left_leaf = "\\"
    right_leaf = "/"
    
    height = 25
    width = 60
    center_x, center_y = width // 2, height // 5
    
    # Full flower display
    flower_display = []
    
    for y in range(height):
        line = ""
        for x in range(width):
            # Calculate distance from center for the flower head
            distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            
            # Flower center
            if distance < 2:
                line += flower_center
            # Flower petals
            elif 2 <= distance < 7:
                # Create a more realistic petal pattern
                angle = ((x - center_x) / max(1, distance)) + ((y - center_y) / max(1, distance))
                if (int(angle * 5) % 2 == 0 and distance < 6) or distance < 5:
                    line += petal
                else:
                    line += " "
            # Stem
            elif abs(x - center_x) < 1 and y > center_y:
                line += stem
            # Left leaf
            elif (center_y + 5) < y < (center_y + 10) and (center_x - 12) < x < center_x:
                leaf_y = y - (center_y + 5)
                leaf_x = x - (center_x - 12)
                if leaf_x <= leaf_y * 1.2 and leaf_x >= leaf_y * 0.8:
                    line += left_leaf
                else:
                    line += " "
            # Right leaf
            elif (center_y + 8) < y < (center_y + 15) and center_x < x < (center_x + 12):
                leaf_y = y - (center_y + 8)
                leaf_x = x - center_x
                if leaf_x >= leaf_y * 0.8 and leaf_x <= leaf_y * 1.2:
                    line += right_leaf
                else:
                    line += " "
            else:
                line += " "
        flower_display.append(line)
    
    # Add a flower pot at the bottom
    pot_position = center_y + 18
    if pot_position < height:
        pot_width = 9
        pot_left = center_x - pot_width // 2
        pot_right = center_x + pot_width // 2
        
        # Draw the top of the pot
        if pot_position < height:
            flower_display[pot_position] = flower_display[pot_position][:pot_left] + "_" * pot_width + flower_display[pot_position][pot_right+1:]
        
        # Draw the pot body
        for i in range(1, 4):
            if pot_position + i < height:
                pot_line = flower_display[pot_position + i]
                pot_line = pot_line[:pot_left-1] + "/" + " " * pot_width + "\\" + pot_line[pot_right+2:]
                flower_display[pot_position + i] = pot_line
        
        # Draw pot base
        if pot_position + 4 < height:
            pot_line = flower_display[pot_position + 4]
            pot_line = pot_line[:pot_left-1] + "‾" * (pot_width + 2) + pot_line[pot_right+2:]
            flower_display[pot_position + 4] = pot_line
    
    # Print the entire flower
    for line in flower_display:
        print(line)
        
def animate_butterfly(flower_display):
    """Add a small animated butterfly near the flower."""
    butterfly_frames = ["Ƹ̵̡Ӝ̵̨̄Ʒ", ">Ƹ̵̡Ӝ̵̨̄Ʒ", ">>Ƹ̵̡Ӝ̵̨̄Ʒ", ">>>Ƹ̵̡Ӝ̵̨̄Ʒ"]
    
    for frame in butterfly_frames:
        clear_screen()
        print("\n\n    A beautiful flower for you:\n")
        print(flower_display)
        print("\n" + " " * 40 + frame)
        time.sleep(0.3)

def animate_growth():
    """Show a simple animation of the flower growing."""
    stages = [
        # Stage 1: Just the soil with a small sprout
        """
                              |
                              |
           __________________|__________________
          /                                     \\
         /                                       \\
        |_______________________________________|
        """,
        
        # Stage 2: Small stem with tiny bud
        """
                             .
                             |
                             |
                             |
                             |
                             |
           __________________|__________________
          /                                     \\
         /                                       \\
        |_______________________________________|
        """,
        
        # Stage 3: Growing stem with leaf
        """
                             .
                             |
                             |
                          \\  |
                           \\ |
                             |
                             |
           __________________|__________________
          /                                     \\
         /                                       \\
        |_______________________________________|
        """
    ]
    
    for stage in stages:
        clear_screen()
        print("\nWatching the flower grow...\n")
        print(stage)
        time.sleep(1)

def main():
    try:
        clear_screen()
        print("Welcome to the Flower Generator!")
        print("Growing a beautiful flower for you...")
        time.sleep(1)
        
        # Show growth animation
        animate_growth()
        
        # Show full flower
        clear_screen()
        print("\n\n    Your beautiful flower is in full bloom!\n")
        display_flower()
        
        # Add inspirational message
        print("\n    A beautiful flower to brighten your day!")
        print("    Remember, like this flower, you too can bloom where you're planted.\n")
        
    except KeyboardInterrupt:
        clear_screen()
        print("\nFlower growing interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()