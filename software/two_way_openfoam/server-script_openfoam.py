import os
import sys
import subprocess
import shutil
import timeit

# start
# timekeeper
start1 = timeit.default_timer()

# local directory in the server to collect user-modified case files sent by the client (user applications)
path_unity="unity_input/constant/"

# local directory in the server to be updated with the user-modified case files
path_simulation="simulation/mixerVessel2D/constant/"

# copy user-modified case files to the simulation directory
shutil.copytree(path_unity, path_simulation)

stop1 = timeit.default_timer()

start2 = timeit.default_timer()

# run OpenFOAM simulations from bash via Allrun script
subprocess.run('source $HOME/.bashrc; ./simulation/mixerVessel2D/Allrun;', shell=True)

stop2 = timeit.default_timer()

# total time for data handling
print('Time_arrange (sec): ', stop1 - start1)

# total time to complete CFD simulations
print('Time_CFD (sec): ', stop2 - start2)

# end