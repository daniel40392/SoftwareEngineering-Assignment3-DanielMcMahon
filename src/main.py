'''
Created on Feb 24, 2017

@author: Daniel McMahon
'''

import argparse
import urllib.request

def turnOn(a,b,c,d,LEDgrid):
    '''Function intended to handle turnOn feature. Turns lights on (or 'true') regardless of their current state'''
    #initially setup with (a-1,c) and (b-1,d) but would return error if 0,0 light appeared on file
    #modified plotMap function accordingly to preempt this issue
    
    for column in range(a,c+1):
        for row in range (b,d+1):
            LEDgrid[column][row] = True
    return LEDgrid

def switch(a,b,c,d,LEDgrid):
    '''Function intended to switch on or off lights depending on their current state. If light on - switch off and vice versa.'''   
    for column in range(a,c+1):
        for row in range (b,d+1):
            
            if LEDgrid[column][row] == True:
                LEDgrid[column][row] = False
            else:
                LEDgrid[column][row] = True
                
    return LEDgrid

def turnOff(a,b,c,d,LEDgrid):
    '''Function intended to handle turnOff feature.  Turns lights off (or 'false') regardless of their current state'''
    for column in range(a,c+1):
        for row in range (b,d+1):
            LEDgrid[column][row] = False
        
    return LEDgrid;

def fileReadL(file):
    '''Function that reads the value of L from a text file - this will determine size of LEDgrid'''
    #this feels a little cheaty.... returns after first line is iterated in loop!
    for line in file.split('\n'):
        x = line
        L = int(x)
        return L
    
def applyChanges(file,L):
    '''Function that parses input from file and carries out various functions according to strings starting values'''
    for line in file.split('\n'):
        if (line.startswith("turn on")):
            ab = line.split(" ")[2]
            cd = line.split(" ")[4]
            
            #test statement checking characters before and after , are numeric
            #the initial ab.count and cd.count ensure that there is in fact a delimiter in the parsed data
            if(ab.count(",")==1 and cd.count(",")==1 and ab.split(",")[0].isnumeric() and ab.split(",")[1].isnumeric() and cd.split(",")[0].isnumeric() and cd.split(",")[1].isnumeric()):    
                a = int(ab.split(",")[0])
                b = int(ab.split(",")[1])
                    
                c = int(cd.split(",")[0])
                d = int(cd.split(",")[1])

            #checking the values are consistent before running function
            if(c>a and d>b):
                #if all values are less then size of the array and greater than 0 continue
                #otherwise make them equal to size of the array, break out of that loop, and retry initial check
                if(a<len(L) and b<len(L) and c<len(L) and d<len(L) and a>0 and b>0 and c>0 and d>0):
                    x=turnOn(a,b,c,d,L)
                    L=x
                elif(a>len(L)):
                    a = len(L)
                    break
                elif(b>len(L)):
                    b = len(L)
                    break
                elif(a>len(L)):
                    c = len(L)
                    break
                elif(a>len(L)):
                    d = len(L)
                    break
                elif(a<0):
                    a = 0
                    break
                elif(b<0):
                    b = 0
                    break
                elif(c<0):
                    c = 0
                    break
                elif(d<0):
                    d = 0
                    break
                    
        elif line.startswith("switch"):
            ab = line.split(" ")[1]
            cd = line.split(" ")[3]
            
            #test statement checking characters before and after , are numeric
            #the initial ab.count and cd.count ensure that there is in fact a delimiter in the parsed data
            if(ab.count(",")==1 and cd.count(",")==1 and ab.split(",")[0].isnumeric() and ab.split(",")[1].isnumeric() and cd.split(",")[0].isnumeric() and cd.split(",")[1].isnumeric()):
                a = int(ab.split(",")[0])
                b = int(ab.split(",")[1])
                    
                c = int(cd.split(",")[0])
                d = int(cd.split(",")[1])
            
            #checking the values are consistent before running function
            if(c>a and d>b):
                #if all values are less then size of the array continue
                #otherwise make them equal to size of the array, break out of that loop, and retry initial check
                if(a<len(L) and b<len(L) and c<len(L) and d<len(L) and a>0 and b>0 and c>0 and d>0):
                    x=switch(a,b,c,d,L)
                    L=x
                elif(a>len(L)):
                    a = len(L)
                    break
                elif(b>len(L)):
                    b = len(L)
                    break
                elif(a>len(L)):
                    c = len(L)
                    break
                elif(a>len(L)):
                    d = len(L)
                    break
                elif(a<0):
                    a = 0
                    break
                elif(b<0):
                    b = 0
                    break
                elif(c<0):
                    c = 0
                    break
                elif(d<0):
                    d = 0
                    break
                
        elif line.startswith("turn off"):
                
            ab = line.split(" ")[2]
            cd = line.split(" ")[4]
                
            #test statement checking characters before and after , are numeric
            #the initial ab.count and cd.count ensure that there is in fact a delimiter in the parsed data
            if(ab.count(",")==1 and cd.count(",")==1 and ab.split(",")[0].isnumeric() and ab.split(",")[1].isnumeric() and cd.split(",")[0].isnumeric() and cd.split(",")[1].isnumeric()):
                a = int(ab.split(",")[0])
                b = int(ab.split(",")[1])
                    
                c = int(cd.split(",")[0])
                d = int(cd.split(",")[1])
            
            #checking the values are consistent before running function
            if(c>a and d>b):
                #if all values are less then size of the array continue
                #otherwise make them equal to size of the array, break out of that loop, and retry initial check
                if(a<len(L) and b<len(L) and c<len(L) and d<len(L) and a>0 and b>0 and c>0 and d>0):
                    x=turnOff(a,b,c,d,L)
                    L=x
                elif(a>len(L)):
                    a = len(L)
                    break
                elif(b>len(L)):
                    b = len(L)
                    break
                elif(a>len(L)):
                    c = len(L)
                    break
                elif(a>len(L)):
                    d = len(L)
                    break
                elif(a<0):
                    a = 0
                    break
                elif(b<0):
                    b = 0
                    break
                elif(c<0):
                    c = 0
                    break
                elif(d<0):
                    d = 0
                    break
    
    return L

def plotMap(L):
    '''function to create the starting LEDgrid'''
    plottedMap = []
    
    #these were initially set to L-1
    #due to range function logic need these to go up as far as L to get accurate output
    
    for i in range(0,L):
        plottedMap.append([False] * (L))
        
    return plottedMap
    
def main(): 
    '''main function - reads console input and passes it through various functions and outputs total lights left on'''
    
    #parsing the user input - expecting a link from the users input...
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    link = args.input #replace link with filename to read standard files
    
    #reading the link
    req=urllib.request.urlopen(link)
    buffer=req.read().decode('utf-8')
    
    #setting value L from file
    L = fileReadL(buffer)#replace buffer with filename to read standard files
    
    #setting up grid based on L value
    LEDgrid = plotMap(L)
    
    #applying changes with turnOn,Switch,turnOff functions called in applyChanges function
    changes=applyChanges(buffer,LEDgrid)#replace buffer with filename to read standard files
    LEDgrid=changes
    #note: functions called within applyChanges return the updated LEDgrid
    #the below prints out total number of lights on by iterating through values of a list inside a list
    counter = 0
    
    for line in LEDgrid:
        for value in line:
            if value == True:
                counter += 1
    
    print("Total number of lights on:", counter)
    
if __name__ == '__main__':
    main()