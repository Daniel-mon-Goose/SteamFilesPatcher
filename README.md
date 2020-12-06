# SteamFilesPatcher v0.9

A simple environment to create patchers and optional executables for Steam files
using PyInstaller.

An example of ***Killing Floor Cyrillic Patcher*** is provided.

## KF1 Cyrillic Patcher example

For those who have come to add cyrillic symbols support to your
KF Game according to the instructions here: 

http://kf-wiki.com/wiki/Help:Cyrillic_language_support:
* download `dist/patch.exe`;
* launch the executable;
* provide the path to your local Steam directory;

And voila.

## Patchers extension

For those who are interested in creating patchers for other Steam products:

### Install dependencies

* install libraries `pyinstaller` (optional, in case you wish to distribute your scripts as executables):
 
```commandline
pip install pypiwin32
pip install pyinstaller
```
or
```commandline
conda install pyinstaller
```

* and `keyboard`:
```commandline
pip install keyboard
```

### `ContextInterface` class

The patcher works with contexts which should implement `ContextInterface` class ().
The module `context` has the `KF1Context` implementation example.
   
`ContextInterface` provides 3 properties which have to be overridden:
* `filenames` - `Iterable[str]` for filenames which will be accessed in the directory;
* `directories_chain` - `Iterable[str]` to build the path to directory with `os.path.join`;
* `replacements` - `Dict[str, str]`, the key component which stores all the changes to apply to the 
      files in `filename`.
      
There are also 3 optional properties:
* `desc` - the `str` description of your tool (e.g. the game and/or the exact files you wish to modify);
* `prerequisites` - the `str` to describe the preparations before launching the .exe;
* `success` - the `str` to show on successful file modification.
    
You are free to use the `main` method in `patch` module or any code of your one if you wish 
to alter the context processing.
  
If your only option is to launch and distribute the `.py` scripts themselves, drop the next part.
  
## Creating an exe

Once your context class is ready, it's time you created your exe with `pyinstaller`:

* add the icon to `icons` directory (optional);
* validate the library:
```commandline
pyinstaller --version
```
* run this:
```commandline
pyinstaller --onefile [--icon=icons/your_icon.ico] patch.py
```
`--onefile` indicates that only .exe will be created, `--icon` is optional.

You will find your executalbe in the `dist` folder.

## To be continued...

At the moment ***v0.9*** supports changes only in one folder and only similar changes to files
(which was enough for KF1). 

***v1.0*** with more options and flexibility is on the way.

Just kidding.

Or not...

Or kidding indeed, I dunno, time is a limited resource...