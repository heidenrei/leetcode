# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        DIRSd = deque(['u','r','d','l'])
        DIRS = {'u':[-1,0],'r':[0,1],'d':[1,0],'l':[0,-1]}
        # backtracking...
        seen = set()
        seen.add((0, 0, 'u'))
        def go(i, j, d):
            robot.clean()
            for _ in range(4):
                ni, nj = i + DIRS[d][0], j + DIRS[d][1]
                if (ni, nj) not in seen and robot.move():
                    seen.add((ni,nj))
                    go(ni, nj, d)
                DIRSd.rotate()
                d = DIRSd[0]
                robot.turnRight()
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        go(0,0,'u')
                