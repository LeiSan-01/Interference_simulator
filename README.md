## Interference simulator
### Objective
The main purpose of this programming project is to make an application that works with a built in simulation that calculates the diffraction pattern created by the interference of light waves that pass through two slits, recreating the Young double slit experiment.

---

### Implementation
This program is based on Python as the main programming language. More specifically, the software uuse for the visual display is the python librery PyQT5, a binding of the set of cross-platform C++ libraries Qt that implements high-level APIs for accessing many aspects of modern desktop and mobile systems.

If your interested on how the physical simulation was built check out the **Documentation** section (not yet implemented but we'll update it at some point I promise lol).

---

### Dependencies
In this project we used the following dependencies to implement the simulation.

|Python libraries|Custom modules|Other|
|:---|:---:|
|python -v 3.14.0 <br>- os<br>- sys<br>- time<br>- PyQt5<br>- numpy<br>- matplotlib|(...)|

### Instructions of use
To use this program we provide the following altervatives:

1. Download the executable located in the **dist** directory. In that folder you'll find two types of executables: **.exe** for windows users and a **.bin** file for linux users.

2. Download directly the zip folder of this repository, unzip it and execute the **main.py** on terminal with the following command. It is recommended to use a python version equal or higher than v.3.7.0.

First, you'll need to have Python installed to run the program. Then open de terminal and run this line to change the directory to the location of **main.py**. If you download the repository in another location change the direction appropiately.

```
cd C:\Users\userName\Downloads\Interference-simulator
```

Then, run **main.py**.

```
python -m main.py
```

3. You can also compile the code yourself using the module **Nuitka** or other compiler of your preference.
