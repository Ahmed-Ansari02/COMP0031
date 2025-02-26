if __name__ == '__main__':
    from acoustools.Levitator import LevitatorController
    from acoustools.Utilities import create_points, add_lev_sig, propagate_abs
    from acoustools.Solvers import wgs

    lev = LevitatorController(ids=(73,53))
    p = create_points(1,1,x=0,y=0,z=0)
    amplitudes = []
    for i in range(1,6):
        amplitudes.append((i,(i/5)*wgs(p)))

    
    for tup in amplitudes:
        x = tup[1]
        print(f'Amplitude: {tup[0]/5} of max')
        print(propagate_abs(x,p))
        print(x.shape)
        x = add_lev_sig(x)

        lev.levitate(x)
        print('Levitating...')
        input()
    print('Stopping...')
    lev.disconnect()
    print('Stopped')


