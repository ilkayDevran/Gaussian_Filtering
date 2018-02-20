from PIL import Image
import numpy as np
import math

#author=__Ilkay Tevfik Devran__

"Variable which is up to User"
SIGMA = None

def main(sigma = 1):
    global SIGMA 
    SIGMA = sigma
    img = readPILimg()
    arr = PIL2np(img)

    gaus_filter = create_Gaussian_filter(sigma=SIGMA)
    #my_filter = np.array(gaus_filter)
    #im_out = convolve(arr, my_filter)
    im_out = Gaussian_filtering(arr, gaus_filter)
    new_img = np2PIL(im_out)
    new_img.show()
    saveImage(new_img)

def readPILimg():
    img = Image.open('bird.png')
    #img.show()
    img_gray = color2gray(img)
    img_gray.show()
    img_gray.save("grayScale.png")
    return img_gray

def color2gray(img):
    img_gray = img.convert('L')
    return img_gray

def PIL2np(img):
    nrows, ncols = img.size
    print("nrows, ncols:", nrows,ncols)
    imgarray = np.array(img)
    return  imgarray

def np2PIL(im):
    print("size of arr:",im.shape)
    img = Image.fromarray(np.uint8(im))
    return img

def convolve(im, filter):
    (nrows, ncols) = im.shape
    (k1, k2) = filter.shape
    k1h = (k1 -1) / 2
    k2h = (k2 -1)/2
    im_out = np.zeros(shape = im.shape)
    print("image size, filter size:" , nrows, ncols, k1, k2)
    for i in range(k1h, nrows-k1h):
        for j in range(k2h, ncols-k2h):
            sum = 0.
            for l in range(-k1h, k1h +1):
                for m in range (-k2h, k2h +1):
                    sum += im[i-l][j-m] * filter[l + k1h][m + k2h]
            im_out[i][j] = sum
    return im_out

def create_Gaussian_filter(sigma):
	temp=1./(2*np.pi*(sigma*sigma))
	interval=int(2*sigma+1)
	startI=int(-interval/2.)
	endI=int(interval/2.+1)
	filterG=[[0 for x in range(interval)]for y in range(interval)]
	for i in range(startI,endI):
		for j in range(startI,endI):
			filterG[i][j]=temp*math.exp( (i*i+j*j)/(2*sigma*sigma)*-1)
			#print filterG[i][j],
		#print
	return filterG

def Gaussian_filtering(img, gaussian_filter):
    my_filter = np.array(gaussian_filter)
    im_out = convolve(img, my_filter)
    return im_out

def saveImage(img):
    imageName = "sigma" + str(SIGMA) + ".png"
    img.save(imageName)


if __name__ == '__main__':
    main()

