import os
import sys
import subprocess
import shutil
import timeit

# start
# timekeeper
start1 = timeit.default_timer()

# a network-script should be created by developer based on remote connections maintained in the system.
# it completely depends to the facilities targeted by developers; cloud-based, webserver, and so on.
# therefore, we do not share a dedicated script but a workflow in the paper which can be easily replicated to set-up remote connections.

stop1 = timeit.default_timer()

# total time for data handling
print('Time_arrange (sec): ', stop1 - start1)

# end