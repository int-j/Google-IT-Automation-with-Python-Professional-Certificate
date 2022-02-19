
#!/usr/bin/env python

from multiprocessing import Pool '''in order to efficiently back up parallelly, use multiprocessing to take advantage of the idle CPU cores.
                                  Initially, because of CPU bound, the backup process takes more than 20 hours to finish, which isn't efficient for a daily backup. Now,
                                  by using multiprocessing, you can back up your data from the source to the destination parallelly by utilizing the multiple cores of the CPU '''

import subprocess             ''' In order to use the rsync command in Python, use the subprocess module by calling call methods and passing a list as an argument'''

import os  ''' we will need walk method os.walk(top, topdown=True, onerror=None, followlinks=False)
          to Generate the file names in a directory tree by walking the tree either top-down or bottom-up.
           This is used to traverse the file system in Python. '''

src = "data/prod"  #make sure to put the right path for you
dest = "data/prod_backup" 

def run(dir):
        subprocess.call(["rsync", "-arq", src, dest])


if __name__ == '__main__':
        for root, dirs, files in os.walk(src): 
                if len(files) > 0:
                        p = Pool(len(files))
                        p.map(run, files)
                if len(dirs) > 0:
                        p = Pool(len(dirs))
                        p.map(run, dirs)
                      
 #further explanation:
'''The import os is used to provide the independent functionality to the script to interact with the file system

Before executing code, Python interpreter reads source file and define few special variables/global variables.

If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. 
If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

Every Python module has it’s __name__ defined and if this is ‘__main__’, it implies that the module is being run standalone by the user 
and we can do corresponding appropriate actions.

If you import this script as a module in another script, the __name__ is set to the name of the script/module.

Python files can act as either reusable modules, or as standalone programs.

if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.'''
