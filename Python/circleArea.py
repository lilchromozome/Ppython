import math
import numpy as np

# Calculate are of a circle
radius = 5
area = math.pi*radius**2
circ = 2*radius*math.pi
# print("area = {}, circumference={}".format(area, circ))




def find_connectivity(points , low_th = 0.95, up_th = 1.05):
    '''
    input:
        points: a two-dimensional (2D) numpy array that contains x and y coordinates of
            points in 2D space. Accordingly, this numpy array will have a dimension of number
            of points × 2.
        low th: a scalar float quantity defines the lower accepted threshold values for the
            Euclidean distance squared value. Use 0.95.
        up th: a scalar float quantity defines the upper accepted threshold values for the
            Euclidean distance squared value. Use 1.05.
    output:
        DistMat:
    '''
    a = len(points)
    DistMat = []
    allx = points[:,0]
    ally = points[:,1]
    for i in range(a):
        DistMat.append(list(np.power(np.subtract(allx, points[i,0]),2) + np.power(np.subtract(ally, points[i,1]),2)))
    
    if DistMat[...] > low_th: DistMat = 0
    
    return DistMat


if __name__ == '__main__': 
    # pp = np.array([[0.98741274 , 0.45638062] ,[0.01421964 , 0.90581148] , [0.30552894 , 0.03409079]])
    # D = []
    # allx = pp[:,0]
    # ally = pp[:,1]
    # for i in range(len(pp)):
    #     f = np.power((allx - pp[i,0]),2) + np.power(ally - pp[i,1],2)
    #     for j in range(len(f)):
    #         if f[j] > 1:
    #             f[j] = 0     
    #     D.append(f)
            
    # print(D)
    
    
    a = np.array([[1,2,3,4],[3,4,5,6]])
    print(np.vstack((a,a)))
    
    a = np.ones([5,5])
    q = np.full((3,3),9)
    a[1:-1,1:-1] = q
    print(a)
    
    
    # print(find_connectivity (pp ,0.5 ,1))
    pass