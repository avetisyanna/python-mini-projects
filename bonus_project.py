user_input = input("Enter seconds: ")

try:
    seconds = int(user_input)
    
    if seconds < 0:
        print("Please enter a positive number!")
    else:
        print(f"Starting timer for {seconds} seconds...")
        
        # --- ADD THIS PART BELOW ---
        while seconds >= 0:
            mins = seconds // 60
            secs = seconds % 60
            print(f"Time left: {mins:02}:{secs:02}", end="\r")
            
            # The busy-wait delay (since we aren't using import time)
            counter = 0
            while counter < 10000000: # Adjust this number if it's too fast/slow
                counter += 1
                
            seconds -= 1
        
        print("\nTime is up! 🔔")

except ValueError:
    print("Error: That wasn't a valid whole number!")