import sys
from PIL import Image
import numpy as np
from scipy import ndimage as nd
src,dst,DY,DX=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
a=np.array(Image.open(src).convert('RGB')).astype(int)
def isg(x): return (x[...,1]-np.maximum(x[...,0],x[...,2])>25)&(x[...,1]>100)
green=isg(a); G=np.array([0,255,0])
lab,_=nd.label(~green)
rp=nd.binary_dilation(lab==2,iterations=4)
yy,xx=np.mgrid[0:a.shape[0],0:a.shape[1]]
edge=540-(yy-200)*0.5-6
zone=((yy>=128)&(yy<212)&(xx>=348)&(xx<518))|((yy>=212)&(yy<322)&(xx>=348)&(xx<478))|((yy>=264)&(yy<322)&(xx>=425)&(xx<480))
lp=nd.binary_dilation((~green)&zone,iterations=4)&zone
res=(yy>=205)&(yy<316)&(xx>=466)&(xx<edge)
out=a.copy(); out[rp|lp|res]=G
# cloud: rows 130..236 of the right puff, closed with an outline
y0,y1,x0,x1=125,240,900,1080
sub=a[y0:y1,x0:x1]; body=(lab[y0:y1,x0:x1]==2)
body[-14:,:]=False
M=nd.binary_fill_holes(nd.binary_closing(body,iterations=8))
inner=nd.binary_erosion(M,iterations=7)
cloud=np.zeros(sub.shape,int); cloud[:]=(40,22,30)
light=np.where(isg(sub)[...,None]|~body[...,None],np.array([228,222,228]),sub)
cloud[inner]=light[inner]
def paste(p,m,X,Y):
    h,w=m.shape; reg=out[Y:Y+h,X:X+w]; ok=m&isg(reg); reg[ok]=p[ok]
paste(cloud,M,x0+DX,y0+DY)
paste(cloud[:,::-1],M[:,::-1],2*712-x1-DX,y0+DY)
Image.fromarray(out.astype('uint8')).save(dst)
