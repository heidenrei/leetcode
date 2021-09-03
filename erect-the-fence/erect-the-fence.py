class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) == 1:
            return trees
        if not trees:
            return []
        
        def orientation(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p3
            x3, y3 = p2

            return (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)

        def euc_dist(p1, p2):
            return (trees[p1][0] - trees[p2][0])**2 + (trees[p1][1] - trees[p2][1])**2
        
        
        def get_convex_hull(coords):
            N = len(coords)
            start = point = coords.index(min(coords, key = lambda x: x[0]))
            hull = set([start])
            far_point = None

            while far_point is not start:
                #print(hull)
                p1 = None
                for i in range(N):
                    if i is point:
                        continue
                    else:
                        p1 = i
                        break
                far_point = p1
                extra_points = set()
                for j in range(N):
                    if j is point or j is p1:
                        continue
                    else:
                        direction = orientation(coords[point], coords[far_point], coords[j])
                        #print(point, far_point, j, direction)
                        if direction > 0:
                            far_point = j
                            extra_points = set()
                        if direction == 0:# and j not in hull and j not in extra_points:
                            if euc_dist(point, j) >  euc_dist(point, far_point):
                                extra_points.add(far_point)
                                far_point = j
                            else:
                                extra_points.add(j)

                                
                hull.add(far_point)
                hull |= extra_points
                if far_point == start:
                        break

                point = far_point
                            
                            
#                 if far_point == start:
#                     break

#                 hull.append(far_point)
#                 point = far_point

            return [coords[x] for x in set(hull)]
        
        return get_convex_hull(trees)