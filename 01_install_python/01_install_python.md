# Installation of Python for Data Science

This tutorial gives a recommendation for a data science python stack. This tutorial
is merely a suggestion for one out of many different usefull alternatives.

Overview:
- The first section describes the fastest path
to getting a working python development environment set up for data science projects.
I will point out where you are taking shortcuts shortcuts.
- The second section suggests some alternatives to the shortcuts in the first section.


# Pythonic Data-Science Stack: fast route

#### Install Anaconda Python

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
   outlines above, you could install it in
   ```
   /Users/alex/Development/Python/pycharm
   ```

#### Create a PyCharm Project

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
2. You will be presented with:
![alt text](https://github.com/AlexHentschel/python-tutorials/blob/master/figures/Project_conf_1.png)


     The project's name is implicitly determined by the tailing folder name. Hence,
     to create a project with the name `sandbox`, specify as folder:
     ```
     /Users/alex/Development/Python/IDE-Project-Configurations/sandbox
     ```

   Lets name our first project      

3) Configure Anaconda as an interpreter in pycharm:


/Users/alex/Development/Python/Python3.6-x64_Anaconda-5.2.0/bin/python




https://www.anaconda.com/download/

1) dow Anaconda Python 3.6: https://www.anaconda.com/download/#macos



2) create virtual environment (Python 3 already comes with everything to create a virtual environment):
  `python -m venv --symlinks <path-to-new-virtual-environment>`
  `source  <path-to-new-virtual-environment>/bin/activate`
   this will change your default python to the one you activated _only in the current shell session_
   to go back to default: `deactivate`
   details: https://docs.python.org/3/library/venv.html (edited)
3) In the _activated_ python environment, install tensorflow (https://www.tensorflow.org/install/install_mac):
• Ensure pip ≥8.1 is installed:
 `easy_install -U pip`
• install TensorFlow
 `pip3 install --upgrade tensorflow`
• install other useful dependencies for data science
`pip install matplotlib pandas h5py` (edited)

# Pythonic Data-Science Stack: best practices

#### Use Miniconda as root environment

https://conda.io/miniconda.html


###
