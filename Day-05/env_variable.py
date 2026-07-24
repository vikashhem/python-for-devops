#first create the environment variable
#using the export env key='value'
#in this case it was password= "something"

#you have to import the os module to use the environment variable

import os

print(os.getenv("password"))