import os
import sys
import subprocess
import shutil
import timeit

# start
# timekeeper
start1 = timeit.default_timer()

# local directory in the server to collect user-modified case files sent by the client (user applications)
path_unity="unity_input/simulation/"

# local directory in the server to be updated with the user-modified case files
path_simulation="comsol/simulation/"

# copy user-modified case files to the simulation directory
shutil.copytree(path_unity, path_simulation)

stop1 = timeit.default_timer()

start2 = timeit.default_timer()

# compiling Java file from batch with the modifed state file
# do not forget to update the directory of comsolcompile.exe in local server
comm = ['C:/Program Files/COMSOL/COMSOL56/Multiphysics/bin/win64/comsolcompile.exe','-jdkroot','C:/Program Files/Java/jdk1.8.0_261','comsol/simulation/ussim.java']
subprocess.run(comm, shell=True)

# running COMSOL software from batch the modifed state file
# do not forget to update the directory of comsolbatch.exe in local server
comrun = ['C:/Program Files/COMSOL/COMSOL56/Multiphysics/bin/win64/comsolbatch.exe', '-inputfile', 'comsol/simulation/ussim.class', '-outputfile', 'comsol/simulation/ussim_new.mph']
subprocess.run(comrun, shell=True)

# alternatively batch executions can be run via Allrun script and with a similar command:
#subprocess.run('source $HOME/.batchrc; ./Allrun;', shell=True)

stop2 = timeit.default_timer()

# total time for data handling
print('Time_arrange (sec): ', stop1 - start1)

# total time to complete CFD simulations
print('Time_CFD (sec): ', stop2 - start2)

# end