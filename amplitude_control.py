if __name__ == '__main__':
    from acoustools.Levitator import LevitatorController
    from acoustools.Utilities import create_points, add_lev_sig, propagate_abs
    from acoustools.Solvers import wgs

    lev = LevitatorController(ids=(73, 53))
    lev.set_frame_rate(1005)
    input("press return to continue")
    while True:
        amplitude = float(input("enter your amplitude at percentage of max: "))
        print(f"levitating at amplitude {amplitude} of max")
        lev.levitate(amplitude * wgs(create_points(1, 1, x=0, y=0, z=0)))
        input("press enter to try next amplitude")
