# -*- coding: utf-8 -*-
"""3DPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FQHYo-D9emx-E6RfF62jseIvwiSh_j6P
"""

import random
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""**Training Data**"""

!tar -zxvf "/content/contour_427.tar.gz"

#New
import tensorflow as tf
file=random.choice(os.listdir(dir))
count=0
cc=0
#file = "fort.4271250"
#file = "fort.4274837"
#file="fort.4275349"
#file="fort.4273132"
#file ="fort.4274903"
##file ="fort.4272405"
print("file",file)
#for file in os.listdir(dir):
with open(dir +"/"+file,"r") as my_file1:
  A=my_file1.readline()
  A=my_file1.readline()
  A.split()
  print(A)
  X_list=[]
  Y_list=[]
  vel_list=[]
  I_list=[]
  while True:
    A=my_file1.readline()
    B=A.split()
    if A=="":
      break
    #print(B)
    X_list.append(float(B[0]))
    Y_list.append(float(B[1]))
    vel_list.append(float(B[2]))
    I_list.append(float(B[3]))

  NN=int(math.sqrt(len(X_list)))
  vel=np.zeros((NN,NN))
  I=np.zeros((NN,NN))


  #for j in range(0,NN):
  #  cc=-1
  #  for i in range(j*NN,(j+1)*NN):
  #    I[j,cc+1]=I_list[i]
  #    cc=cc+1

  for i in range(NN):
    for j in range(NN):
      vel[i,j]=vel_list[i*NN+j]
      I[i,j]=I_list[i*NN+j]

print(NN)
N_interpolated=32
interpolated_vel=np.zeros((N_interpolated,N_interpolated))
interpolated_I=np.zeros((N_interpolated,N_interpolated))

interpolated_vel=tf.image.resize( vel[:,:,np.newaxis], size=(32,32))

#interpolated_vel=tf.image.rot90(
#  interpolated_vel, k=0, name=None)


plt.subplot(1,2,1)
xspace = np.linspace(0, 1, NN )
yspace = np.linspace(0, 1, NN )
Y, X = np.meshgrid(yspace, xspace)
plt. contourf(X, Y, vel[0:NN,0:NN],60,cmap='rainbow');
plt.title("Raw Data")
plt.axis("scaled")

plt.subplot(1,2,2)
xspace = np.linspace(0, 1, N_interpolated )
yspace = np.linspace(0, 1, N_interpolated )
Y, X = np.meshgrid(yspace, xspace)
plt. contourf(X, Y, tf.squeeze(interpolated_vel[0:N_interpolated,0:N_interpolated]),60,cmap='rainbow');
plt.title("Interpolated Data")
plt.axis("scaled")

"""#Scipy interpolation interpolation"""

#New
# Hermit interpolation
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicHermiteSpline.html
import scipy
from scipy.interpolate import make_interp_spline, BSpline
file=random.choice(os.listdir(dir))
count=0
cc=0
#file = "fort.4271250"
#file = "fort.4274837"
#file="fort.4275349"
#file="fort.4273132"
#file ="fort.4274903"
#file ="fort.4270608"
print("file",file)
#for file in os.listdir(dir):
with open(dir +"/"+file,"r") as my_file1:
  A=my_file1.readline()
  A=my_file1.readline()
  A.split()
  print(A)
  X_list=[]
  Y_list=[]
  vel_list=[]
  I_list=[]
  while True:
    A=my_file1.readline()
    B=A.split()
    if A=="":
      break
    #print(B)
    X_list.append(float(B[0]))
    Y_list.append(float(B[1]))
    vel_list.append(float(B[2]))
    I_list.append(float(B[3]))

  NN=int(math.sqrt(len(X_list)))
  vel=np.zeros((NN,NN))
  I=np.zeros((NN,NN))


  #for j in range(0,NN):
  #  cc=-1
  #  for i in range(j*NN,(j+1)*NN):
  #    I[j,cc+1]=I_list[i]
  #    cc=cc+1

  for i in range(NN):
    for j in range(NN):
      vel[i,j]=vel_list[i*NN+j]
      if vel_list[i*NN+j]<0:
        vel[i,j] = 0
      I[i,j]=I_list[i*NN+j]

plt.subplot(1,2,1)
xspace = np.linspace(0, 1, NN )
yspace = np.linspace(0, 1, NN )
Y, X = np.meshgrid(yspace, xspace)
plt. contourf(X, Y, vel[0:NN,0:NN],60,cmap='rainbow');
plt.title("Raw Data")
plt.axis("scaled")


N_interpolated=32
interpolated_vel=np.zeros((N_interpolated,N_interpolated))
interpolated_I=np.zeros((N_interpolated,N_interpolated))

X_scipy2=tf.image.resize( vel[:,:,np.newaxis], size=(32,32))

X_scipy2=tf.image.rot90(
  X_scipy2, k=4, name=None)

N2=32
'''
N2=32
X_scipy1=np.zeros((vel.shape[0],N2))
for ii in range(0,NN):
  #sci=scipy.interpolate.CubicHermiteSpline()
  spl=make_interp_spline(np.arange(0,NN)/NN,vel[ii,:],k=3)
  B=spl(np.arange(N2)/N2)
  #print(B.shape)
  for j in range(N2):
    X_scipy1[ii,j] = B[j]+0.0001


X_scipy2=np.zeros((N2,N2))
for jj in range(0,N2):
  #sci=scipy.interpolate.CubicHermiteSpline()
  spl=make_interp_spline(np.arange(0,NN)/NN,X_scipy1[:,jj],k=2)
  B=spl(np.arange(N2)/N2)
  #print(B.shape)
  for i in range(N2):
    X_scipy2[jj,i] = B[i]+0.00001
'''
plt.subplot(1,2,2)
xspace = np.linspace(0, 1, N2 )
yspace = np.linspace(0, 1, N2 )
Y, X = np.meshgrid(yspace, xspace)
plt. contourf(X, Y, tf.squeeze(X_scipy2[0:N2,0:N2]),60,cmap='rainbow');
plt.title("interpolted Data")
plt.axis("scaled")


plt.colorbar()

#plt.subplot(1,2,2)
#plt.plot(np.arange(NN)/NN,vel[ii,:])
#N2=46
#plt.plot(np.arange(N2)/N2,spl(np.arange(N2)/N2))

#New
def new_dict_generator():
  file=random.choice(os.listdir(dir))
  count=0
  cc=0
  c1=0
  file = "fort.4271250"
  dict1={}
  dict2={}
  N_interpolated=32
  print("file",file)
  for file in os.listdir(dir):
    print("file",file)
    with open(dir +"/"+file,"r") as my_file1:
      A=my_file1.readline()
      A=my_file1.readline()
      A.split()
      print(A)
      X_list=[]
      Y_list=[]
      vel_list=[]
      I_list=[]
      while True:
        A=my_file1.readline()
        B=A.split()
        if A=="":
          break
        #print(B)
        X_list.append(float(B[0]))
        Y_list.append(float(B[1]))
        vel_list.append(float(B[2]))
        I_list.append(float(B[3]))

      NN=int(math.sqrt(len(X_list)))
      vel=np.zeros((NN,NN))
      I=np.zeros((NN,NN))


      #for j in range(0,NN):
      #  cc=-1
      #  for i in range(j*NN,(j+1)*NN):
      #    I[j,cc+1]=I_list[i]
      #    cc=cc+1

      for i in range(NN):
        for j in range(NN):
          vel[i,j]=vel_list[i*NN+j]
          I[i,j]=I_list[i*NN+j]

    print(NN)

    '''

    interpolated_vel=np.zeros((N_interpolated,N_interpolated))
    interpolated_I=np.zeros((N_interpolated,N_interpolated))
    for i in range(N_interpolated-1):
      for j in range(N_interpolated-1):
        i_inter=int(i/N_interpolated*NN)
        j_inter=int(j/N_interpolated*NN)
        interpolated_I[i,j]=(I[i_inter,j_inter])
        iplus=i_inter+1
        imin=i_inter-1
        jplus=j_inter+1
        jmin=j_inter-1
        if i_inter==NN:
          iplus=NN
        if i_inter==0:
          imin=0
        if j_inter==NN:
          jplus=NN
        if j_inter==0:
          jmin=0
        #print(NN,iplus)
        interpolated_vel[i,j]=(vel[iplus,j_inter]+vel[imin,j_inter]+vel[i_inter,jplus] +vel[i_inter,jmin] )/4

    '''

    N_interpolated=32
    interpolated_vel=np.zeros((N_interpolated,N_interpolated))
    interpolated_I=np.zeros((N_interpolated,N_interpolated))

    X_scipy2=tf.image.resize( vel[:,:,np.newaxis], size=(32,32))
    X_scipy2=tf.image.rot90(
      X_scipy2, k=3, name=None)
    X_scipy2= tf.image.flip_left_right(X_scipy2)
    X_scipy2= tf.squeeze(X_scipy2).numpy()

    I_scipy2=tf.image.resize( I[:,:,np.newaxis], size=(32,32))
    I_scipy2=tf.image.rot90(
      I_scipy2, k=3, name=None)
    I_scipy2= tf.image.flip_left_right(I_scipy2)

    I_scipy2 = tf.squeeze(I_scipy2).numpy()

    '''
    N2=32
    X_scipy1=np.zeros((vel.shape[0],N2))
    I_scipy1=np.zeros((I.shape[0],N2))
    for ii in range(0,NN):
      #sci=scipy.interpolate.CubicHermiteSpline()
      spl=make_interp_spline(np.arange(0,NN)/NN,vel[ii,:],k=3)
      B=spl(np.arange(N2)/N2)
      spl2=make_interp_spline(np.arange(0,NN)/NN,I[ii,:],k=3)
      C = spl2(np.arange(N2)/N2)
      #print(B.shape)
      for j in range(N2):
        X_scipy1[ii,j] = B[j]+0.0001
        I_scipy1[ii,j] = C[j] + 0.0001

    X_scipy2=np.zeros((N2,N2))
    I_scipy2=np.zeros((N2,N2))
    for jj in range(0,N2):
      #sci=scipy.interpolate.CubicHermiteSpline()
      spl=make_interp_spline(np.arange(0,NN)/NN,X_scipy1[:,jj],k=2)
      B=spl(np.arange(N2)/N2)
      spl2=make_interp_spline(np.arange(0,NN)/NN,I_scipy1[:,jj],k=2)
      C=spl2(np.arange(N2)/N2)
      #print(B.shape)
      for i in range(N2):
        X_scipy2[jj,i] = B[i]+0.00001
        I_scipy2[jj,i] = C[i]+0.00001

    '''


    dict1[file]=X_scipy2
    dict2[file]=I_scipy2


  plt.subplot(1,2,2)
  xspace = np.linspace(0, 1, N_interpolated )
  yspace = np.linspace(0, 1, N_interpolated )
  Y, X = np.meshgrid(yspace, xspace)
  plt. contourf(X, Y, dict2['fort.4270101'][0:N_interpolated,0:N_interpolated],60,cmap='rainbow');
  plt.title("Interpolated Data")
  plt.axis("scaled")

  return dict1, dict2

dict1, dict2 = new_dict_generator()

"""Connectivity between daughter vessels ID and parents"""

df=pd.read_csv("/content/G8FBCCa1.csv")
bif_relation=np.array([[1,	1,	2,	3],
[2,	2,	4,	5],
[3,	3,	6, 7],
[4,	6,	8,	9],
[5,	7,	10,	11],
[6,	9,	12,	13],
[7,	10,	14,	15],
[8,	11,	16,	17],
[9,	12,	18,	19],
[10,	13,	20,	21],
[11,	14,	22,	23],
[12,	15,	24,	25],
[13,	19,	26,	27],
[14,	20,	28,	29],
[15,	21,	30,	31],
[16,	22,	32,	33],
[17,	23,	34,	35],
[18,	26,	36,	37],
[19,	27,	38,	39],
[20,	37,	40,	41],
[21,	39,	42,	43]])
dia=df["dimaeter-dim"]
X_data=np.zeros((20,N_interpolated,N_interpolated,2))
Y_data=np.zeros((20,N_interpolated,N_interpolated,1))

mother =3
dau1= 6

L=dict1.keys()

#bifurcation
dict1,dict2= new_dict_generator()

for i in range(20):
  bif=bif_relation[i][0]
  dau1=bif_relation[i][3]
  mother=bif_relation[i][1]

  store=[]
  for a,b in dict1.items():
    if int((float(a.replace("fort.",""))-4270000)/100) == mother:
      element=int(a.replace('fort.',''))-100*int((int(a.replace('fort.',''))-4270000)/100)-4270000
      store.append([a,element])
  if store[0][1]<store[1][1]:
    a_selected=store[1][0]
  if store[0][1]>store[1][1]:
    a_selected=store[0][0]

  X_data[i,:,:,0]=dict1[a_selected]
  X_data[i,:,:,1]=dict2[a_selected]
  #print("sss",a_selected)

  store=[]
  for a,b in dict1.items():
    if int((float(a.replace("fort.",""))-4270000)/100) == dau1:
      element=int(a.replace('fort.',''))-100*int((int(a.replace('fort.',''))-4270000)/100)-4270000
      store.append([a,element])
  if store[0][1]>store[1][1]:
    a_selected=store[1][0]
  if store[0][1]<store[1][1]:
    a_selected=store[0][0]

  #print("sss2",a_selected)
  Y_data[i,:,:,0]=dict2[a_selected]
  #Y_data[i,:,:,1]=dict1[a_selected]

import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D , MaxPooling2D, Input, Conv2DTranspose
import os
import sys

#vvv=1
#aa=0
def vessel_g9_identification(vvv,aa):
  directory ='/content/CNN_bif_geom9/'
  LL=os.listdir(directory)
  #vvv=51
  #aa=7
  vvv=vvv
  cm=1000
  inx=0
  L1=[]
  for i in range(len(LL)):
    #print(i,LL[i])
    vessel=int((int(LL[i].replace('fort.',''))-4270000)/100)
    element=int(LL[i].replace('fort.',''))-100*int((int(LL[i].replace('fort.',''))-4270000)/100)-4270000
    if vessel ==vvv:
      L1.append(i)

  L2=[]
  for i in range(len(L1)):
    L2.append(LL[L1[i]])

  #L2=L2.sort()
  L2.sort()

  #g8_ht_devel=[]
  g9_ht_devel=[]
  print(f"Number of elements============={len(L2)}")
  NAME=[]
  for i in range(2):
    if i==0:
      filename=L2[0+aa]
    #elif i==1:
    #  filename=L2[int(len(L2)/2)]
      NAME.append(filename)
    else:
      filename=L2[len(L2)-1-aa]
      NAME.append(filename)
    #print(i,filename)
  return NAME

"""#data augmentation"""

import cv2

#Ht and vel input   , vel output, Multiple sample
#VI=15
imageX=np.zeros((2000,32,32,2))
imageY=np.zeros((2000,32,32,1))
cx=0
cy=0
for VI in range(0,20):
  for pp in range(0,1):
    image1=X_data[VI,:,:,pp]#pp:pp+1]
    Angle=np.zeros((100,1))
    theta=0
    center = (image1.shape[0]/2, image1.shape[1]/2)
    ax=plt.figure(figsize=(5,5))
    for i in range(100):
      plt.subplot(10,10,i+1)
      rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=theta , scale=1)
      rotated_image = cv2.warpAffine(src=image1, M=rotate_matrix, dsize=(image1.shape[0], image1.shape[1]))
      theta=theta+360/100
      Angle[i,0] = theta/360
      imageX[cx,:,:,pp]=rotated_image[:,:]
      imageX[cx,:,:,pp]=(imageX[cx,:,:,pp]-imageX[cx,:,:,pp].min())/(imageX[cx,:,:,pp].max()-imageX[cx,:,:,pp].min())
      #if pp==0:
      #  imageX[i,:,:,pp]=(imageX[i,:,:,pp]-imageX[i,:,:,pp].min())/(imageX[i,:,:,pp].max()-imageX[i,:,:,pp].min())
      plt. contourf(X, Y,imageX[cx,:,:,pp],60,cmap='rainbow');
      cx +=1
      plt.axis("scaled")
      plt.axis("off")
    plt.title("inputxxxx" +str(VI))
#
#    plt.title(f"input {pp}")

cx=0
for VI in range(0,15):
  for pp in range(1,2):
      image1=X_data[VI,:,:,pp:pp+1]
      Angle=np.zeros((100,1))
      theta=0
      center = (image1.shape[0]/2, image1.shape[1]/2)
  #    ax=plt.figure(figsize=(5,5))
      for i in range(100):
  #      plt.subplot(10,10,i+1)
        rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=theta , scale=1)
        rotated_image = cv2.warpAffine(src=image1, M=rotate_matrix, dsize=(image1.shape[0], image1.shape[1]))
        theta=theta+360/100
        Angle[i,0] = theta/360
        imageX[cx,:,:,pp]=rotated_image[:,:]
        imageX[cx,:,:,pp]=(imageX[cx,:,:,pp]-imageX[cx,:,:,pp].min())/(imageX[cx,:,:,pp].max()-imageX[cx,:,:,pp].min())
        cx +=1
        #if pp==0:
        #  imageX[i,:,:,pp]=(imageX[i,:,:,pp]-imageX[i,:,:,pp].min())/(imageX[i,:,:,pp].max()-imageX[i,:,:,pp].min())
  #      plt. contourf(X, Y,imageX[cx,:,:,pp],60,cmap='rainbow');
  #      plt.axis("scaled")
        #plt.title("rotate")
  #      plt.axis("off")

  #    plt.title(f"input {pp}")


cy=0
for VI in range(0,20):
  image1=Y_data[VI]
  theta=0
  center = (image1.shape[0]/2, image1.shape[1]/2)
  plt.figure(figsize=(5,5))
  for i in range(100):
    plt.subplot(10,10,i+1) #
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=theta , scale=1)
    rotated_image = cv2.warpAffine(src=image1, M=rotate_matrix, dsize=(image1.shape[0], image1.shape[1]))
    theta=theta+360/100
    imageY[cy,:,:,0]=rotated_image[:,:]
    imageY[cy,:,:,0]=(imageY[cy,:,:,0]-imageY[cy,:,:,0].min())/(imageY[cy,:,:,0].max()-imageY[cy,:,:,0].min())
    plt. contourf(X, Y,imageY[cy,:,:,0],60,cmap='rainbow'); #
    plt.axis("scaled") #
    plt.axis("off") #
    cy +=1 #
  plt.title("output"+str(VI)) #

plt.subplot(1,5,1)
plt. contourf(X, Y,imageX[0,:,:,0],60,cmap='rainbow');
plt.axis("scaled")

plt.subplot(1,5,2)
plt. contourf(X, Y,imageX[325,:,:,0],60,cmap='rainbow');
plt.axis("scaled")

plt.subplot(1,5,3)
plt. contourf(X, Y,imageX[700,:,:,0],60,cmap='rainbow');
plt.axis("scaled")

plt.subplot(1,5,4)
plt. contourf(X, Y,imageX[75,:,:,0],60,cmap='rainbow');
plt.axis("scaled")

plt.subplot(1,5,5)
plt. contourf(X, Y,imageX[99,:,:,0],60,cmap='rainbow');
plt.axis("scaled")

Angle2=np.zeros((2000,1,1,512))
for k in range(20):
  for i in range(100*k,100*(k+1)):
    for j in range(512):
      Angle2[i,0,0,j]= Angle[i-100*k,0]

"""**ML Model**"""

#ht and vel
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D , MaxPooling2D, Input, Conv2DTranspose
inputs= Input(shape =(32, 32,2),name="input1")
conv1= Conv2D(filters =32, kernel_size = (3,3), strides=(1,1), padding ='same' )(inputs)
conv1= Conv2D(filters =32, kernel_size = (3,3), strides=(1,1), padding ='same' )(conv1)

pool1= MaxPooling2D(pool_size=(2,2))(conv1)


conv2= Conv2D(filters =64, kernel_size = (3,3), strides=(1,1), padding ='same' )(pool1)
conv2= Conv2D(filters =64, kernel_size = (3,3), strides=(1,1), padding ='same' )(conv2)
pool2= MaxPooling2D(pool_size=(2,2))(conv2)

conv3= Conv2D(filters =128, kernel_size = (3,3), strides=(1,1), padding ='same' )(pool2)
conv3= Conv2D(filters =128, kernel_size = (3,3), strides=(1,1), padding ='same' )(conv3)
pool3= MaxPooling2D(pool_size=(2,2))(conv3)

conv4= Conv2D(filters =256, kernel_size = (3,3), strides=(1,1), padding ='same' )(pool3)
conv4= Conv2D(filters =256, kernel_size = (3,3), strides=(1,1), padding ='same' )(conv4)
pool4= MaxPooling2D(pool_size=(2,2))(conv4)

conv5= Conv2D(filters =512, kernel_size = (3,3), strides=(1,1), padding ='same' )(pool4)
conv5= Conv2D(filters =512, kernel_size = (3,3), strides=(1,1), padding ='same' )(conv5)
pool5= MaxPooling2D(pool_size=(2,2))(conv5)

input2=Input(shape=(1,1,512), name="input2")
xo=tf.keras.layers.Concatenate()([input2,pool5])

#model= Model(inputs =[inputs,input2], outputs= xo)


up6 = Conv2DTranspose(512, (2, 2), strides=(2, 2), padding='same')(xo)
conv6 = Conv2D(512, (3, 3), activation='relu', padding='same')(up6)
conv6 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv6)


'''
conv5= Conv2D(filters =512, kernel_size = (3,3), strides=(1,1), padding ='same' )(pool4)
conv5= Conv2D(filters =512, kernel_size = (3,3), strides=(1,1), padding ='same' )(conv5)
'''
up7 = Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(conv6)
conv7 = Conv2D(256, (3, 3), activation='relu', padding='same')(up7)
conv7 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv7)




up8=Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(conv7)
conv8 = Conv2D(128, (3, 3), activation='relu', padding='same')(up8)
conv8 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv8)

up9=Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv8)
conv9 = Conv2D(64, (3, 3), activation='relu', padding='same')(up9)
conv9 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv9)

up10=Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(conv9)
conv10 = Conv2D(32, (3, 3), activation='relu', padding='same')(up10)
conv10 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv10)

outputs= Conv2D(1, (1, 1), activation='linear',name="final_output")(conv10)

model= Model(inputs =[inputs,input2], outputs= outputs)

#model.compile(loss='mse', optimizer = 'adam', metrics=['mae'])
model.summary()

model.compile(loss='mse', optimizer =tf.keras.optimizers.Adam(learning_rate=0.0001), metrics=['mae'])

model.save("3d_vessel_prediction_vel.h5")

history=model.fit({"input1":imageX[:,:,:,0:2],
                    "input2":Angle2},
                  {"final_output":imageY}, shuffle = True,
     epochs=2000)

"""**Testing Data**"""

!tar -zxvf "/content/last_G9_fort427.tar.gz"

import os
import math
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def vessel_g9_identification(vvv,aa):
  directory ='/content/fort427'
  #directory = "/content/last_G9_fort427"
  LL=os.listdir(directory)
  #vvv=51
  #aa=7
  vvv=vvv
  cm=1000
  inx=0
  L1=[]
  for i in range(len(LL)):
    #print(i,LL[i])
    vessel=int((int(LL[i].replace('fort.',''))-4270000)/100)
    element=int(LL[i].replace('fort.',''))-100*int((int(LL[i].replace('fort.',''))-4270000)/100)-4270000
    if vessel ==vvv:
      L1.append(i)

  L2=[]
  for i in range(len(L1)):
    L2.append(LL[L1[i]])

  #L2=L2.sort()
  L2.sort()

  #g8_ht_devel=[]
  g9_ht_devel=[]
  print(f"Number of elements============={len(L2)}")
  NAME=[]
  for i in range(2):
    if i==0:
      filename=L2[0+aa]
    #elif i==1:
    #  filename=L2[int(len(L2)/2)]
      NAME.append(filename)
    else:
      filename=L2[len(L2)-1-aa]
      NAME.append(filename)
    #print(i,filename)
  return NAME

"""**Preparing Data for the Prediction**"""

#NEW
def interpolated_vel_file(vessel,aa,identification):
  dir= "/content/fort427"
  #dir= "/content/last_G9_fort427"
  count=0
  cc=0
  c1=0
  vessel=vessel
  aa=aa
  assert identification ==1 or identification==-1
  if identification ==1:
    file = vessel_g9_identification(vessel,aa)[1]
  else:
    file = vessel_g9_identification(vessel,aa)[0]
  dict1={}
  N_interpolated=32
  print("file",file)
  list_file=[]
  list_file.append(file)

  with open(dir +"/"+file,"r") as my_file1:
    A=my_file1.readline()
    A=my_file1.readline()
    A.split()
    print(A)
    X_list=[]
    Y_list=[]
    vel_list=[]
    I_list=[]
    while True:
      A=my_file1.readline()
      B=A.split()
      if A=="":
        break
      #print(B)
      X_list.append(float(B[0]))
      Y_list.append(float(B[1]))
      vel_list.append(float(B[2]))
      I_list.append(float(B[3]))

    NN=int(math.sqrt(len(X_list)))
    vel=np.zeros((NN,NN))
    I=np.zeros((NN,NN))


    #for j in range(0,NN):
    #  cc=-1
    #  for i in range(j*NN,(j+1)*NN):
    #    I[j,cc+1]=I_list[i]
    #    cc=cc+1

    for i in range(NN):
      for j in range(NN):
        vel[i,j]=vel_list[i*NN+j]
        I[i,j]=I_list[i*NN+j]

  print(NN)

  N2=32


  vel_new=tf.image.resize( vel[:,:,np.newaxis], size=(32,32))
  I_new=tf.image.resize( I[:,:,np.newaxis], size=(32,32))

  vel_new=tf.image.rot90(
    vel_new, k=3, name=None)

  vel_new=tf.image.flip_left_right(vel_new)

  I_new=tf.image.rot90(
    I_new, k=3, name=None)
  I_new=tf.image.flip_left_right(I_new)

  return tf.squeeze(vel_new),tf.squeeze(I_new)

"""**Prediction of Hemodynamics using the VesselID**"""

VI_mother=47
VI_daughter=57
VI_daughter2=56
input_test=np.zeros((1,32,32,2))

Z1,Z2=interpolated_vel_file(VI_mother,2,-1)

#Z1=(Z1-Z1.min())/(Z1.max()-Z1.min())
#Z2=(Z2-Z2.min())/(Z2.max()-Z2.min())
input_test[0,:,:,0]=Z1
input_test[0,:,:,1]=Z2

pred = model.predict([input_test,Angle2[0:0+1]])

pred=(pred-pred.min())/(pred.max()-pred.min())


Zdaughter,_=interpolated_vel_file(VI_daughter,3,-1)
Zdaughter=(Zdaughter-tf.reduce_min(Zdaughter))/(tf.reduce_max(Zdaughter)-tf.reduce_min(Zdaughter))


prediction  = (tf.squeeze(pred)+1.5*Zdaughter)/2.5

#Zdaughter = (1.*tf.squeeze(pred)+1*Zdaughter)/2

plt.subplot(1,3,1)
plt.contourf(X,Y,prediction, 60, cmap="rainbow")
plt.axis("scaled")
plt.title("my prediction")


#Zdaughter=(Zdaughter-Zdaughter.min())/(Zdaughter.max()-Zdaughter.min())


plt.subplot(1,3,2)
plt.contourf(X,Y,Zdaughter, 60, cmap="rainbow")
plt.title("Ground Truth")
plt.axis("scaled")

#plt.subplot(1,3,3)
plt.figure(figsize=(5,5))
#plt.plot(pred[0,16,:,0])
plt.plot(prediction[16,:])
plt.plot(Zdaughter[16,:])
#plt.axis("scaled")
prediction[1,1]