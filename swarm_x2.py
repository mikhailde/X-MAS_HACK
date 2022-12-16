from particleswarm.swarm import Swarm


class Swarm_X2 (Swarm):
    def __init__ (self,
            swarmsize,
            minvalues,
            maxvalues,
            currentVelocityRatio,
            localVelocityRatio,
            globalVelocityRatio):
       Swarm.__init__ (self,
            swarmsize,
            minvalues,
            maxvalues,
            currentVelocityRatio,
            localVelocityRatio,
            globalVelocityRatio)


    def _finalFunc (self, position):
        penalty = self._getPenalty (position, 10000.0)
        finalfunc = sum (position * position)

        return finalfunc + penalty
        
def _getPenalty (self, position, ratio):
    """
    Рассчитать штрафную функцию
    position - координаты, для которых рассчитывается штраф
    ratio - вес штрафа
    """
    penalty1 = sum ([ratio * abs (coord - minval)
        for coord, minval in zip (position, self.minvalues)
        if coord < minval ] )

    penalty2 = sum ([ratio * abs (coord - maxval)
        for coord, maxval in zip (position, self.maxvalues)
        if coord > maxval ] )

    return penalty1 + penalty2
