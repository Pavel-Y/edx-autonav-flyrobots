import numpy as np

class Pose3D:
    def __init__(self, rotation, translation):
        self.rotation = rotation
        self.translation = translation
        
    def inv(self):
        '''
        Inversion of this Pose3D object
        
        :return inverse of self
        '''
        # TODO: implement inversion
        inv_rotation = self.rotation.transpose()
        inv_translation = -np.dot(inv_rotation, self.translation)
        
        return Pose3D(inv_rotation, inv_translation)
    
    def __mul__(self, other):
        '''
        Multiplication of two Pose3D objects, e.g.:
            a = Pose3D(...) # = self
            b = Pose3D(...) # = other
            c = a * b       # = return value
        
        :param other: Pose3D right hand side
        :return product of self and other
        '''
        # TODO: implement multiplication
        mul_rotation = np.dot(self.rotation, other.rotation) 
        mul_translation = np.dot(self.rotation, other.translation) + self.translation
        
        return Pose3D(mul_rotation, mul_translation)
    
    def __str__(self):
        return "rotation:\n" + str(self.rotation) + "\ntranslation:\n" + str(self.translation.transpose())

def compute_quadrotor_pose(global_marker_pose, observed_marker_pose):
    '''
    :param global_marker_pose: Pose3D 
    :param observed_marker_pose: Pose3D
    
    :return global quadrotor pose computed from global_marker_pose and observed_marker_pose
    '''
    # TODO: implement global quadrotor pose computation
    # global marker position is T_W->M = T_W->Q * T_Q->M hence T_WQ = T_WM * T_QM^-1
    global_quadrotor_pose = global_marker_pose * observed_marker_pose.inv()

    return global_quadrotor_pose
