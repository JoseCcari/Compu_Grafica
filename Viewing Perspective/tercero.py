import numpy as np
import math

def uVector(v):
    return v/ np.linalg.norm(v)
def mult(a,b):
    return np.matmul(a,b)
def divide(M):
  R=np.zeros((4,4))
  for i in range(3):
    for j in range(4):
      R[i][j]=M[i][j]/M[3][j]
  return R

def PerspectiveView(Mvp,Mper,Mcam,Puntos):
  R=np.matmul(Mvp,np.matmul(Mper,np.matmul(Mcam,Puntos)))
  return divide(R) 
def OrthographicView(Mvp,Morth,Mcam,Puntos):
  R=np.matmul(Mvp,np.matmul(Morth,np.matmul(Mcam,Puntos)))
  return R 


nx=100
ny=80

# Puntos
Puntos=np.array([
                [-1,1,-1,1],
                [2,2,0,0],
                [-6,-6,-6,-6],
                [1,1,1,1]])


#Matrix ViewPort Nx=ancho, Ny=alto
Mvp=np.array([
              [nx/2, 0,0,(nx-1)/2],
              [0,ny/2,0,(ny-1)/2],
              [0,0,1,0],
              [0,0,0,1]
              ])
#print(Mvp)




"""l=-2
r=2
b=0
t=3
"""
aspectRatio = 100/80
n=-4
f=-8
t=math.tan(30 * math.pi /180)*abs(n)

print ("t : " ,t)
b=-t
print ("b: ",b)
r=aspectRatio*abs(t)

print ("r: " ,r)
l=-r
print ("l: ",l)
print ("\n")
# Matriz de Proyección ortográfica
Morth=np.array([[2/(r-l),0,0,-((r+l)/(r-l))],
                [0,2/(t-b),0,-((t+b)/(t-b))],
                [0,0,2/(n-f),-((n+f)/(n-f))],
                [0,0,0,1]])



e=np.array([0,4,2])
g=np.array([0,-2,-5])
t=np.array([0,1,0])

w=-uVector(g)
u=uVector(np.cross(t,w))
v=np.cross(w,u)
'''
print("w=",w)
print("u=",u)
print("v=",v)
'''
M1=np.array([[u[0],u[1],u[2],0],
              [v[0],v[1],v[2],0],
              [w[0],w[1],w[2],0],
              [0,0,0,1]])
M2=np.array([
              [1,0,0,-e[0]],
              [0,1,0,-e[1]],
              [0,0,1,-e[2]],
              [0,0,0,1]])
Mcam=np.matmul(M1,M2)
#print(Mcam)

P=np.array([
             [n,0,0,0],
             [0,n,0,0],
             [0,0,n+f,-f*n],
             [0,0,1,0]
])
Mper = mult(Morth,P)
" Mvp * Mcam * Mper * puntos"
#print(Mper)



#Resultados

print("\n Matriz perpectiva: \n")
print(PerspectiveView(Mvp, Mper, Mcam, Puntos))