
<h1>Gesture Control Application</h1>
<p>Welcome to the Gesture Control Application! This application uses a Keras model to recognize gestures from your webcam feed and perform actions based on those gestures. You can dynamically load the Keras model and labels file using the application's graphical interface. Can be used for who are blind and don't have access to assitive technology but still need to use desktops/computers.</p>

<h2>Features</h2>
<ul>
  <li><strong>Dynamic Model and Labels Loading</strong>: Select the <code>.h5</code> model file and <code>labels.txt</code> file through the graphical interface.</li>
  <li><strong>Gesture Recognition</strong>: The application recognizes gestures and performs corresponding actions like play/pause video, rewind, skip, and adjust volume.</li>
  <li><strong>Real-time Camera Feed</strong>: View the real-time feed from your webcam and see the recognized gestures.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>Required Python packages: <code>cv2</code>, <code>numpy</code>, <code>pyautogui</code>, <code>tkinter</code>, <code>PIL</code>, <code>keras</code></li>
  <li>A trained Keras model saved in <code>.h5</code> format</li>
  <li>A <code>labels.txt</code> file with gesture labels</li>
</ul>

<h2>Installation</h2>
<ol>
  <li><strong>Clone the repository:</strong>
      <pre><code>git clone https://github.com/yourusername/gesture-control-app.git
cd gesture-control-app</code></pre>
  </li>
  <li><strong>Install required packages:</strong>
      <p>Create a virtual environment (optional but recommended):</p>
      <pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</code></pre>
      <p>Install the dependencies:</p>
      <pre><code>pip install opencv-python-headless numpy pyautogui pillow keras</code></pre>
  </li>
</ol>

<h2>Usage</h2>
<ol>
  <li><strong>Run the application:</strong>
      <pre><code>python app.py</code></pre>
  </li>
  <li><strong>Load Model and Labels:</strong>
      <ul>
          <li>Click the "Load Keras Model" button to select your <code>.h5</code> model file.</li>
          <li>Click the "Load Labels File" button to select your <code>labels.txt</code> file.</li>
          <li>The application will start processing the webcam feed and perform actions based on recognized gestures.</li>
      </ul>
  </li>
</ol>

<h2>File Structure</h2>
<ul>
  <li><code>app.py</code>: Main application script.</li>
  <li><code>labels.txt</code>: File containing gesture labels.</li>
  <li><code>keras_model.h5</code>: Trained Keras model (replace with your model file if you want).</li>
</ul>

<h2>Example</h2>
<p>Below is an example of how to use the application:</p>
<ol>
  <li>*Please be patient and wait for the application to open and load everything, it may take time*</li>
  <li>Click "Load Keras Model" and select your model file. (should happen on application start)</li>
  <li>Click "Load Labels File" and select your labels file. (should happen on application start)</li>
  <li>The application will display the camera feed and recognize gestures.</li>
</ol>

<h2>Screenshots</h2>
*Application Demo (this would skip a video forward)
<p><img src="https://github.com/user-attachments/assets/c6453263-6509-4992-a6a4-d584bf4883c1" alt="Example Screenshot" width="600"/></p>

*Terminal Output
<p><img src="https://github.com/user-attachments/assets/98dfa423-36c7-4d50-897f-fb206723761d" alt="Example Screenshot" width="600"/></p>


<h2>Troubleshooting</h2>
<ul>
  <li><strong>Model Not Loading</strong>: Ensure the file is a valid <code>.h5</code> model file.</li>
  <li><strong>Labels Not Loading</strong>: Ensure the <code>labels.txt</code> file is correctly formatted.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork the repository and submit pull requests. For significant changes, please open an issue to discuss them first.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License</p>

<h2>Contact</h2>
<p>For any questions or feedback, please reach out to <a href="mailto:ad@adamdalloul.com">ad@adamdalloul.com</a>.</p>

<hr/>

<p>Thank you for using the Gesture Control Application!</p>

