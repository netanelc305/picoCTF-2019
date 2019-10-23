import os 

for i in range(1000, 0, -1):
    os.system("tar -xf" + str(i) + ".tar")
os.system("rm *.tar")