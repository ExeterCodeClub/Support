import time
path="/home/cormorant/documents/devon-library/christmas/"
name="output"
filepath = path + name

num = 0
numarr = [num]
while True:
    with open(filepath,'w') as output:
        output.write(str(numarr))
        print("output: " + str(numarr))
        num = num + 1
        numarr.append(num)

        #to read back again
    with open(filepath,'r') as inputdat:
        inputstr=inputdat.read()
        print(inputstr)
        exec('array='+inputstr)
        print(array)

    time.sleep(1)

#to read

