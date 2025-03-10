# 📷 Video Conference Using Fisheye  

---

## ⚙️ **Setup and Run Instructions**

### ⚠️ Important Notes:  
- **Make sure to perform all environment setup steps using Conda Terminal (Anaconda Prompt).**  
- **If you are using PyCharm, ensure that the Conda environment is set up properly before running the program.**  

---

## A. 🚀 Clone This Repository  

To download the code to your local machine, use the following command:  

```bash
git clone https://github.com/perseverance-tech-tw/video-conference-using-fisheye.git
```

This will create a copy of the repository on your local machine, allowing you to access and modify the code.  


### B. 🏗️ Set Up Conda Virtual Environment  

Follow these steps to set up a **Conda environment** using Python 3.9 with all required dependencies:  

#### 1. Create a New Conda Environment  

```bash
conda create -n gtk39-env python=3.9 --solver=classic
```

#### 2. Activate the Environment  

```bash
conda activate gtk39-env
```

---

### C. 📦 Install Required Packages  

#### 3. Install GTK3 and Related Dependencies  

```bash
conda install pygobject gtk3 pango gobject-introspection
```

#### 4. Install OpenCV and NumPy  

```bash
conda install opencv numpy
```

#### 5. Install PyGrabber  

```bash
pip install pygrabber
```

---

### D. ✅ Run the Program  

Once all dependencies are installed, you can run the program using:  

```bash
python main.py
```

---

## 3. 🧑‍💻 Set Up and Run via PyCharm  

You can also use **PyCharm IDE** to develop or run this project. Make sure you **finish all environment setup steps in Conda Terminal first**.  

### Steps to Open and Run in PyCharm:  

1. **Open PyCharm IDE.**  
2. Select **"Open"** from the main menu.  
3. Navigate to the directory where you cloned the `video-conference-using-fisheye` repository.  
4. Select the **root directory** and click **"Open"** to load the project.  
5. Set up the Python interpreter:  
   - Go to **File > Settings > Project: [Your Project] > Python Interpreter**.  
   - Click **"Add Interpreter"** and choose **"Conda Environment"** > **"Existing Environment"**.  
   - Browse and select the Python interpreter from the **gtk39-env** you created.  
6. Once the environment is selected, you can **run `main.py` directly from PyCharm**.  

---

## 🎉 You're Ready to Go!

After following the steps above, you should be able to run the **Video Conference Using Fisheye** project both from the command line and from within PyCharm.  

When the program runs successfully, you will see the fisheye camera view as intended.  

---

## 📚 References & Tools  

- [Anaconda / Conda](https://www.anaconda.com/products/individual)  
- [PyGObject](https://pygobject.readthedocs.io/en/latest/)  
- [GTK3](https://www.gtk.org/)  
- [OpenCV](https://opencv.org/)  
- [NumPy](https://numpy.org/)  
- [PyGrabber](https://pypi.org/project/pygrabber/)  
- [PyCharm](https://www.jetbrains.com/pycharm/)  
