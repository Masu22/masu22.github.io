# Ripping Guide

Sure. Here's a summarized and translated version of the guide in English:

---

**How to Rip Models and Textures from Sketchfab – Summary**

**Model Ripping – Requirements:**

* Python 2.6.6
* Blender 2.49
* A custom Python import script

**Steps:**

1. **Install Python 2.6.6** and add these to the `PythonPath` environment variable:
   `C:\Python26; C:\Python26\DLLs; C:\Python26\Lib; C:\Python26\Lib\lib-tk`

2. **Find your model on Sketchfab** and inspect the webpage using the browser's developer tools (Network tab). Refresh the page and locate files such as:

   * `file.osgjs.gz`
   * `model_file.bin.gz`
   * `model_file_wireframe.bin.gz`
     Download these files.

3. **Open Blender 2.49**:
   Drag `Blender249.blend` onto `blender.exe`.
   Press `Alt + P`, navigate to the downloaded `.gz` file, and import it.

4. **Optional:** You can save the project and open it in newer Blender versions or export the model.

**Note:** If you’ve set the `PythonPath` variable, remove it before using newer Blender versions.

---

**Texture Ripping – Requirements:**

* NinjaRipper
* Firefox version 49.0b2

**Steps:**

1. **Install Firefox 49.0b2** and copy the path to `firefox.exe`.

2. **Open NinjaRipper** (32-bit version). Add the Firefox path and select the “D3D9 wrapper”.

3. **Launch Firefox through NinjaRipper**, go to the Sketchfab model page, and add `/embed` at the end of the URL.

4. **Click Play, go fullscreen**, rotate the model to fully load it, and press `F9`.

5. After Firefox becomes responsive again, close everything. The textures will be saved in the NinjaRipper output folder.

---

**Note:** The original guide includes download links and a VirusTotal scan link.

---

Let me know if you need this reformatted or adapted for a specific use (e.g., presentation, PDF, etc.).

---
---
