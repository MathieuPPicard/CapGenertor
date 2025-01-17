import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import sys

OK = 2  #number of OK image cap
NOK = 100   #number of NOK image cap
COLOR = ["#FF0000","#0000FF","#00FF00"] #Choice of colors
OK_PATH = f'CapGenerator/OK' #Your folder path for the OK image
NOK_PATH = f'CapGenerator/NOK'   #Your folder path for the NOK image

P_COLOR = np.floor(NOK/4)  #sub number of NOK image (color problem)
P_COLOR_PATH = NOK_PATH + '/P_COLOR'
P_MATTER = np.floor(NOK/4)  #sub number of NOK image (matter problem)
P_MATTER_PATH = NOK_PATH + '/P_MATTER'
P_SIZE = np.floor(NOK/4) #sub number of NOK image (size problem)
P_SIZE_PATH = NOK_PATH + '/P_SIZE'
P_CURVE = np.floor(NOK/4)   #sub number of NOK image (curve problem)
P_CURVE_PATH = NOK_PATH + '/P_CURVE'

# Representation of a cap will be done inside of a 17x17 square,
# Acceptable one will ONLY be 11x11 with 2 pixel for curvature
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]
#[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0]
#[0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
#[0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0]
#[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0]
#[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

'''
Input : 
    width = The width of the image
    height = the height of the image
Output : 
    array = a OK array generated
'''
def createOkButton(width, height):
    array = np.zeros((height,width))
    for i in range(width) :
        for j in range(height) :
            if i == 3 or i == 13 :
                if j >= 6 and j <= 10 : 
                    array[i][j] = 1
            if i == 4 or i == 12 :
                if j >= 5 and j <= 11 :
                    array[i][j] = 1
            if i == 5 or i == 11 :
                if j >= 4 and j <= 12 :
                    array[i][j] = 1
            if i >= 6 and i < 11 :
                if j >= 3 and j <= 13 :
                    array[i][j] = 1
    return array

'''
Input : 
    width = The width of the image
    height = the height of the image
Output : 
    array = a Nok array generated
'''
def createNokButton(width, height) : 
    array = np.zeros((height,width))
    
    return array

'''
Input : 
    color = list of colors
Output : 
    A random colors pick from the array color
'''
def randomColorPick(color) :
    rand = np.int8(np.floor(np.random.rand() * len(color)))
    return COLOR[rand]

'''
Input : 
    array = the array generated
    ok = boolean indicating if its a conform cap or not
Output : 
    An image in one of the folders
'''
def createImage(array, ok, num, type) :
    rndColor = randomColorPick(COLOR)
    colors = ['white', rndColor]
    cmap = mcolors.ListedColormap(colors)
    plt.axis('off')
    plt.imshow(array, cmap=cmap, interpolation='nearest')
    #Indicate how to name and where to save the image
    if ok == True :
        plt.savefig(f'{OK_PATH}/Ok_image_{num}.png',bbox_inches='tight',pad_inches=0)
    else : 
        if type == "P_COLOR" :
            plt.show()
        if type == "P_CURVE" :
            plt.show()
        if type == "P_MATTER" :
            plt.show()
        if type == "P_SIZE" :
            plt.show()

def main() :
    #Create the ok images
    for i in range(OK):
        array = createOkButton(17, 17)
        createImage(array, True, i)

    #Create the nok images
    for j in range(NOK) :
        array = createNokButton(17, 17)
        #createImage(array, False, j ,)

if __name__ ==  "__main__" :
    sys.exit(main())