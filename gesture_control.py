import cv2
import numpy as np
import pyautogui
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from keras.models import load_model
import time

# Global variables to store the model and gesture labels
model = None
gesture_labels = {}

# Function to load the Keras model
def load_keras_model():
    global model
    file_path = filedialog.askopenfilename(filetypes=[("H5 files", "*.h5")])
    if file_path:
        model = load_model(file_path)
        print(f"Model loaded from {file_path}")

# Function to load the labels file
def load_labels_file():
    global gesture_labels
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, encoding='utf-8') as f:
            gesture_labels = {int(line.split()[0]): ' '.join(line.split()[1:]) for line in f}
        print(f"Labels loaded from {file_path}")

# Initialize camera
cap = cv2.VideoCapture(0)

# Create the main application window
root = tk.Tk()
root.title('Gesture Control Application')

# Dark mode toggle function
def toggle_dark_mode():
    if dark_mode_var.get():
        root.configure(bg='black')
        for button in action_buttons:
            button.configure(bg='black', fg='white')
    else:
        root.configure(bg='white')
        for button in action_buttons:
            button.configure(bg='white', fg='black')

# Dark mode toggle variable
dark_mode_var = tk.BooleanVar()
dark_mode_var.set(False)

# Dark mode toggle checkbox
dark_mode_check = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var)
dark_mode_check.pack()

# Bind the dark mode toggle to the trace
dark_mode_var.trace_add('write', lambda *args: toggle_dark_mode())

# Set the delay in seconds
ACTION_DELAY = 2  # Adjust as needed

# Keep track of the last action time
last_action_time = time.time()

# Function to perform action based on gesture label
def perform_action(gesture_label):
    global last_action_time
    
    # Check if enough time has passed since the last action
    current_time = time.time()
    if current_time - last_action_time >= ACTION_DELAY:
        if gesture_label == '✋🤚🖐Unpause/Pause Video':
            pyautogui.press('space')
        elif gesture_label == '👈Rewind Video Backward':
            pyautogui.press('left')
        elif gesture_label == '👉Skip Video Forward':
            pyautogui.press('right')
        elif gesture_label == '👆Volume Up':
            pyautogui.press('volumeup')  # Adjust as needed
        elif gesture_label == '👇Volume Down':
            pyautogui.press('volumedown')  # Adjust as needed
        
        # Update the last action time
        last_action_time = current_time 

# Placeholder for the preprocessing function (replace with actual preprocessing)
def preprocess(frame):
    resized_frame = cv2.resize(frame, (224, 224))
    normalized_frame = resized_frame / 255.0
    return normalized_frame

# Function to update camera feed on canvas
def update_camera_feed():
    global model, gesture_labels
    if model is None:
        # If no model is loaded, ask the user to select one
        load_keras_model()
        if model is None:
            # If user cancels model selection, terminate the application
            root.quit()
            return
    
    if not gesture_labels:
        # If no labels are loaded, ask the user to select a labels file
        load_labels_file()
        if not gesture_labels:
            # If user cancels labels file selection, terminate the application
            root.quit()
            return

    ret, frame = cap.read()
    
    # Preprocess the frame
    preprocessed_frame = preprocess(frame)
    
    # Perform inference using the loaded model
    preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)
    prediction = model.predict(preprocessed_frame)
    predicted_class = np.argmax(prediction)
    gesture_label = gesture_labels.get(predicted_class, 'Unknown Gesture')
    
    # Perform the associated action
    perform_action(gesture_label)
    
    # Update the predicted gesture label
    predicted_label.config(text=f'Predicted Gesture: {gesture_label}')

    # Display the frame on the canvas
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)
    
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img
    
    # Continue updating the camera feed
    canvas.after(10, update_camera_feed)

    # Print predicted gesture
    print("Predicted Gesture:", gesture_label)

# Create buttons for each gesture action (initially empty)
action_buttons = []

# Function to update the action buttons based on loaded labels
def update_action_buttons():
    global action_buttons, gesture_labels
    # Remove existing buttons
    for button in action_buttons:
        button.pack_forget()
    action_buttons = []
    
    # Create buttons for each gesture action
    for gesture_idx, gesture_label in gesture_labels.items():
        emoji_label = ' '.join([emo for emo in gesture_label.split()])
        button = tk.Button(root, text=emoji_label, command=lambda idx=gesture_idx: perform_action(gesture_labels[idx]))
        action_buttons.append(button)
        button.pack()

# Create a label to display predicted gesture
predicted_label = tk.Label(root, text='Predicted Gesture: N/A')
predicted_label.pack()

# Create image canvas to display camera feed
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Button to load the model file
load_model_button = tk.Button(root, text="Load Keras Model", command=load_keras_model)
load_model_button.pack()

# Button to load the labels file
load_labels_button = tk.Button(root, text="Load Labels File", command=load_labels_file)
load_labels_button.pack()

# Start updating the camera feed
update_camera_feed()

# Run the application
root.mainloop()

# Release resources
cap.release()
cv2.destroyAllWindows()
