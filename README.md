# keybind-windows
This repository contains a windows solution for binding windows to keys. For example one can globally bind the key 'a' to pull up google chrome.

# Installing
First make sure [python3](https://www.python.org/downloads/windows/) is installed. Navigate to the working directory of the project. Use the following command in terminal:

    python3 -m pip install -r requirements.txt
    
# Getting Started
The config.json file is where one can set the key binds and the process identifiers (PIDs).  An example config file is shown below. In this instance there are two process' that have keybinds. The "keys" prop denotes the key combination to bind to the PID.  The first object in the "key_binds" array binds ctrl shift 1 to the pid 8016. 

    {
		"key_binds":
			[
				{"keys":"ctrl+shift+1", "pid":8016},
				{"keys":"ctrl+shift+2", "pid": 364}
			]
	}
# What if I have 3 windows!?
What if there is 3 windows that need keybinds?? All that is required is to add a new object to the array shown below. Make sure that the new object has a unique keybind.

    {
		"key_binds":
			[
				{"keys":"ctrl+shift+1", "pid":8016},
				{"keys":"ctrl+shift+2", "pid": 364}, // <- added a comma
				{"keys":"alt+shift+2", "pid": 9999} // <- the new object
			]
	}

# What is a PID?!
A PID is a process identifier that windows uses as a unique id in order to keep track of programs. One can find the PID of a specific program by going to the task manager.

![tempsnip](https://user-images.githubusercontent.com/25306965/132424712-388e0d7f-52da-41fb-8115-5dc20e3daa9b.png)

