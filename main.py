# [controller info]
# To connect a dualsense controller on macos, hold the create button and power button.


# [resources]
# - https://github.com/flok/pydualsense
# - Issue with the usage here of hidapi, so I insatalled
# * For this to work on M1 macs, you need to install a different hidapi:
#    https://github.com/trezor/cython-hidapi
#   (which itself uses a different hidapi - )
# * There seems to be some success with installing specific versions of hidapi, but that didn't work for me
#    https://stackoverflow.com/questions/59188993/osx-hidapi-install-for-python3-pip3-troubleshooting-high-sierra

# [todo]
# https://docs.python.org/3/howto/sockets.html


import pydualsense.pydualsense as pydualsense

ds = pydualsense()
ds.init()
