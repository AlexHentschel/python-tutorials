# Installation of Python for Data Science

This tutorial gives a recommendation for installing and organizing a data-science python stack. 
In the tutorial I describe a system for organizing the different components. I found that 
this organization scheme scales particularly well when working on many different projects over time.
It allows for different python environments and version to be used for different projects.
However, this tutorial is merely a suggestion for one out of many different usefull alternatives.

Overview:
- The first section describes the fastest path
to getting a working python development environment set up for data science projects.
I will point out where you are taking shortcuts shortcuts.
- The second section suggests some alternatives to the shortcuts in the first section.


# Pythonic Data-Science Stack: fast route

### Install Anaconda Python

For data science in python Python, you need a python interpreter plus various numerical packages.
Continuum Analytics provides commercial images for various cloud platforms that include
Python distributions specifically for data science applications. Their *Anaconda Python* distribution is provided for free contains
all common packages you will need for data science.


**Installation** (for MacOS):

1. Download `Python 3`, `64-bit` version as the `Command-Line Installer`
   from the [Anaconda's download page](https://www.anaconda.com/download/).
   Examples below are for `Anaconda3-5.2.0-MacOSX-x86_64.sh`, which is [current version](https://repo.anaconda.com/archive/Anaconda3-5.2.0-MacOSX-x86_64.sh)
   of Anaconda (as of August 2018).
2. I recommend installing Python into a sub-folder in your home directory.
   (This prevents you from writing into system-owned folders, i.e. Python
   will be less intertwined with the OS, easier to update, remove, etc.)
   I collect everything software-development related in `/Users/alex/Development`.   
   Make a folder for all the different Python environments you
   will install over time, e.g.
   ```
   mkdir -p /Users/alex/Development/Python
   ```   
3. Make the shell script executable:
   ```
   chmod u+x Anaconda3-5.2.0-MacOSX-x86_64.sh
   ```
4. Execute the installer:
   - accept license agreement (`Enter`, press `q` for jumping to end of agreement, type `yes`)
   - The installer will promt you for a install location. Use a sub-directory with the
     type of the python distribution, e.g.
     ```
     /Users/alex/Development/Python/Python3.6-x64_Anaconda-5.2.0
     ```
     I recommend including Python version (3.6), hardware architecture (x64), distribution name (Anaconda) and version (5.2.0) in the folder name.

     By default, Anaconda will install into
     ```
     /Users/<your_username>/anaconda3
     ```
     Which is fine, iuf you only keep one distribution. However, at later points, you might want to have multiple 
     distributions in parallel, to be backwards compatible to execute your older code. Hence, my recommendation 
     to create a separate folder.
      
   - The installer asks if it should add the python version to your system `PATH`.
     Select according to your preferences.  
     In case you select `yes`, the installer will
     modify your `~/.bash_profile` and add the following line to it:
     ```
     export PATH="/Users/alex/Development/Python/Python3.6-x64_Anaconda-5.2.0/bin:$PATH"
     ```
     (you can also do this later manually). For this tutorial, we don't need
     Anaconda to modify your system `PATH`.
   - Last, you are asked if you want the `installation of Microsoft VSCode`.
     Select `no`. VSCode is a source code editor. I recommend using PyCharm instead (installation described next).

**Notes**
- Anaconda will serve as your root environment. While you can install additional
packages into the root environment, I do not recommend it. Various packages build on
top of others and require specific versions of these dependencies. Keeping the versions of
all packages consistent is non-trivial. Hence, I recommend sticking to the official Anaconda releases. If you need to install or update
packages, use `virtual environments` as explained in the second section.
- We have taken the following **shortcut** here:
  - We installed a gigantic distribution (~ 3GB hard drive space) with many
    packages you'll probably never use.
  - Once you start using virtual environments, you anyway install all dependencies you need
    from scratch (virtual environments start without any packages) into the various environments
    that you create for different projects.
  - Hence, installing a minimal root distribution can save you a lot of disk space.


#### Install Python IDE: PyCharm

PyCharm is my preferred python IDE. Alternatives include Eclipse, Spyder, Jupyter.
I recommend PyCharm because:
- Python debugger working out of the box (which is a substantial problems in many other Python IDEs).
- In-line display of function signatures and documentation (if available in code).
- Support for running projects in different python environments.
- Static code analysis.


**Installation** (for MacOS):
Get the latest PyCharm from [jetbrains](https://www.jetbrains.com/pycharm/).
   I found the `Community Edition` (free) to be fully sufficient.
   Installer is straight forward. If you are following my directory structure
   outlined above, you could install it in
   ```
   /Users/alex/Development/Python/pycharm
   ```

### Create a PyCharm Project

When PyCharm first opens, it presents you with a welcome screen
and prompts you create or open a project. In PyCharm, a project
is simply a configuration that tells PyCharm which python
packages and folders should be opened and what python environments to use to
execute what code. A project _points_ to python code, but
 the project configuration folder itself should _not contain_ python sources.
I generally create a new Project for each topic I am working on. In addition,
I keep a `sandbox` project for random little experiments.

As you might want to open some python sources in the context of several projects,
I recommend keeping the PyCharm Projects separate from the python source code.
While I check out all source code into `/Users/alex/Git/`,
my PyCharm project configurations live in `/Users/alex/Development/Python/IDE-Project-Configurations/`.   

**Creating the `sandbox` Project** (for MacOS):
1. On the welcome screen, select `Create New Project`. Alternatively,
   when closing the main window of the PyCharm IDE, it will go back to the
   welcome screen.  
2. Your project configuration could look something like this:
![project configuration](https://github.com/AlexHentschel/python-tutorials/blob/master/figures/Project_conf_1.png)
   - The project's name is implicitly determined by the tailing folder name. Hence,
     to create a project with the name `sandbox`, specify the `location`:
     ```
     /Users/alex/Development/Python/IDE-Project-Configurations/sandbox
     ```
   - Configure the default python interpreter that will be used to
     execute code in the project:
     - Select `Existing Interpreter` and lick on the `...` button on the right.
       (If you have previously already configured PyCharm to use Anaconda, it
       should be available in the drop-down menu).
     - In the window ![interpreter configuration](https://github.com/AlexHentschel/python-tutorials/blob/master/figures/Project_conf_2.png)
       choose `System Interpreter` (left) and use the `...` button to select an
       already installed python environment. You need to select the `python` executable,
       in our example:
       ```
       /Users/alex/Development/Python/Python3.6-x64_Anaconda-5.2.0/bin/python
       ```

### PyCharm in Action

In the following, I will use the [python-tutorials repository](https://github.com/AlexHentschel/python-tutorials) as an example.
I assume you already have cloned the repo so you can execute the provided examples.  In the following, 
lets assume the repository to be located in `/Users/alex/Git/python-tutorials`.

1. Open Pycharm and the `sandbox` project (`File` -> `Open Recent` lets you switch projects).
2. Now, we are going to _add_ the `python-tutorials` folder to PyCharm's `sandbox` project.
   (This merely instructs PyCharm to add the folder you choose to a list of displayed folders. 
   Files and code remain where they are.)
   - Go to `File` -> `Open` and select the folder `/Users/alex/Git/python-tutorials`.
   - Now `python-tutorials` should be listed in the left of the IDE with its location on your 
   hard disk next to it in grey print. 

### The iPython console

The iPython console allows you to _interactively_ execute code _while_ you are developing it.
I find this immensely useful, specifically for data science and machine learning projects. 

- Open (drouble click) the python script `python-tutorials/example_code/hello_world.py`
- Mark all lines of code and press `Control`+`Shift`+`e`. The `Python Console` will open
  and execute the selected code. 
- You can open _multiple_ iPython consoles and work with them in parallel.

### Interactive plotting

Similarly, iPython allows you to _interactively_ plot graphs. 

- An example is given in `python-tutorials/example_code/hello_plot.py`
- Again, execute all the lines of code using `Control`+`Shift`+`e`.
  Now try to edit the code while *keeping the plot open*.
  On mys system, the plot always stays in front covering up part of the
  PhCarm editor. I found this rather irritating and counterproductive. 
- Execute `python-tutorials/example_code/hello_plot2.py` in a _newly opened_ 
  Python Console. In this example, we use the `TKAgg` backend for `matplotlib`
  which fixed this behaviour for me.  
- You can make the backend change permanent by editing your 
 `~/.matplotlib/matplotlibrc` file. In its default configuration, your 
  `matplotlibrc` states for MacOS
  ```
  backend      : macosx
  ```
  Change this to 
  ```
  backend      : TKAgg
  ```
 (see [here](http://matplotlib.org/users/customizing.html#the-matplotlibrc-file) for 
  more details)  

# Pythonic Data-Science Stack: best practices

### Use Miniconda as root environment:

https://conda.io/miniconda.html

### Use Virtual Python Environment 

**Creation of virtual environments**:
- Python 3 already comes with everything to create a virtual environment. 
  Make sure you select the python executable for the distribution that should serve 
  as a root. In our example, execute in the command line:
  ```
  /Users/alex/Development/Python/Python3.6-x64_Anaconda-5.2.0/bin/python -m venv --symlinks <path-to-new-virtual-environment>
  ```
- On the command line, you can select a virtual environment by  
  ```
  source  <path-to-new-virtual-environment>/bin/activate
  ```
   this will change your default python to the one you just activated, 
   but _only in the current shell session_. 
   Note: the command prompt will change and display the python environment. 
   To deactivate (go back to the default python environment), type 
   ```
   deactivate
   ```
   (further reading on virtual environments: https://docs.python.org/3/library/venv.html)

### Install Dependencies into a Virtual Environment 

- activate your virtual environment in a shell session
  ```
  source  <path-to-new-virtual-environment>/bin/activate
  ```
- stall dependency (as wheel; automatically downloaded ); example package `numpy`:
  ```
  pip install numpy
  ```
  You can also install a list of packages at once. Here an example of what I install by default
  ```
  pip install h5py numexpr Cython blosc tables numpy pandas scipy scikit-learn matplotlib

  ```
- you can also install a package from local file system (e.g. from a cloned git repository)
  ```
  pip install <path_to_package's_root_directory>
  ```
  The root directory should contain a file setup.py


