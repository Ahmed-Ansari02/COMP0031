if __name__ == '__main__':
    from acoustools.Levitator import LevitatorController
    from acoustools.Utilities import create_points, add_lev_sig, propagate_abs
    from acoustools.Solvers import wgs

    lev = LevitatorController(ids=(73,53))
    points = []
    x = []
    for i in range(200):

        x.append(i)
        points.append(wgs(create_points(1,1,x=0,y=0.0001*i,z=0)))

    rev_points = points[::-1]
    lev.set_frame_rate(200)
    lev.levitate(points[0])
    input("press return to continue")
    while True:
        lev.levitate(points)
        print("press enter to backward")
        input()
        lev.levitate(rev_points)
        print("press enter to forward")
        input()
    
