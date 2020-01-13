from utils import log_utils
import jbrik_solver_move_lib
import jbrik_cube

# middlerow https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/step3-second-layer-f2l/
def solve_middle(cube):
    log_utils.log("Starting middle row solve")
    facetosolve = 3



    solved = are_all_middle_rowcells_solved(cube)
    while not solved:

        cube = swap_backwards_oriented_mid_rowcells(facetosolve, "swap", cube)

        cube = swap_non_oriented_mid_rowcells_to_top(facetosolve, cube)

        cube = align_oppface_crossrowcell_to_adj_ccolor(facetosolve, cube)

        cube = perform_lr_solve_on_cross_rowcells(facetosolve, cube)

        solved = are_all_middle_rowcells_solved(cube)






        '''
        # identify a non matched center row that isn't matched to the front or LR face nor top color,
        # saw back to the top and next step
        #cube =swap_non_oriented_mid_rowcells_to_top(facetosolve, cube)


        # check and solve
        cube = perform_lr_solve_on_cross_rowcells(facetosolve, cube)
        solved = are_all_middle_rowcells_solved(cube)

        # move any middle row oppface middle cell back to oppface
        cube = swap_backwards_oriented_mid_rowcells(facetosolve, "back", cube)
        cube = perform_lr_solve_on_cross_rowcells(facetosolve, cube)
        solved = are_all_middle_rowcells_solved(cube)

        # for each oppface crossrowcell
        # rotate until rowcell adjacent to crossrowcell is alignined with center color
#        cube = align_oppface_crossrowcell_to_adj_ccolor(facetosolve, cube)

#        solved = are_all_middle_rowcells_solved(cube)
        cube = swap_backwards_oriented_mid_rowcells(facetosolve, "swap", cube)
        cube = perform_lr_solve_on_cross_rowcells(facetosolve, cube)
        solved = are_all_middle_rowcells_solved(cube)

        # identify a non matched center row that isn't matched to the front or LR face nor top color,
        # saw back to the top and next step
        swap_non_oriented_mid_rowcells_to_top(facetosolve, cube)

        cube = align_oppface_crossrowcell_to_adj_ccolor(facetosolve, cube)
        cube = perform_lr_solve_on_cross_rowcells(facetosolve, cube)
        solved = are_all_middle_rowcells_solved(cube)
        '''



    cube.finalize_solve_phase()
    log_utils.log("Middle row is solved")

    return cube


def swap_non_oriented_mid_rowcells_to_top(facetosolve, cube):
    for rowcell in jbrik_cube.fivesixmidrowcrossrowcells:
        rowcellcolor = cube.get_cell_val_by_rowcell(rowcell)
        rowcellccolor = cube.get_center_color_for_rowcell(rowcell)
        adjrowcell = jbrik_cube.get_adjrowccell_for_rowcell(rowcell)
        adjrowcellcolor = cube.get_cell_val_by_rowcell(adjrowcell)
        adjrowcellccolor = cube.get_center_color_for_rowcell(adjrowcell)
        ccolor = cube.get_center_color_for_facenum(facetosolve)

        if rowcellcolor != rowcellccolor and adjrowcellcolor != adjrowcellccolor and \
                rowcellcolor != ccolor and adjrowcellcolor != ccolor:
            log_utils.log("Rowcell: " + rowcell + " is a total missalign with cell color: " + rowcellcolor
                          + " and adjacent color: " + adjrowcellcolor)

            # its a rightswap
            #movestrlist = get_leftcross_solution_list(facetosolve, adjrowcell, rowcell)
            movestrlist = get_rightcross_solution_list(facetosolve, adjrowcell, rowcell)
            for rmove in movestrlist:
                cube = jbrik_solver_move_lib.perform_rotation_str(rmove, cube)

            return cube


        #cube = swap_backwards_oriented_mid_rowcell(facetosolve, rowcell, swaptype, cube)

    return cube


def are_all_middle_rowcells_solved(cube):
    for rowcell in jbrik_cube.fivesixmidrowcrossrowcells:
        if not is_middle_rowcell_solved(rowcell, cube):
            return False

    return True

def is_middle_rowcell_solved(rowcell, cube):
    rowcellcolor = cube.get_cell_val_by_rowcell(rowcell)
    rowcellccolor = cube.get_center_color_for_rowcell(rowcell)
    adjrowcell = jbrik_cube.get_adjrowccell_for_rowcell(rowcell)
    adjrowcellcolor = cube.get_cell_val_by_rowcell(adjrowcell)
    adjrowcellccolor = cube.get_center_color_for_rowcell(adjrowcell)

    if rowcellcolor != rowcellccolor or adjrowcellcolor != adjrowcellccolor:
        return False

    return True

def swap_backwards_oriented_mid_rowcells(facetosolve, swaptype, cube):
    for rowcell in jbrik_cube.fivesixmidrowcrossrowcells:
        cube = swap_backwards_oriented_mid_rowcell(facetosolve, rowcell, swaptype, cube)

    return cube

def swap_backwards_oriented_mid_rowcell(facetosolve, rowcell, swaptype, cube):
    rowcellcolor = cube.get_cell_val_by_rowcell(rowcell)
    rowcellccolor = cube.get_center_color_for_rowcell(rowcell)
    adjrowcell = jbrik_cube.get_adjrowccell_for_rowcell(rowcell)
    adjrowcellcolor = cube.get_cell_val_by_rowcell(adjrowcell)
    adjrowcellccolor = cube.get_center_color_for_rowcell(adjrowcell)

    # check orientation
    if rowcellcolor == adjrowcellccolor and adjrowcellcolor == rowcellccolor:
        log_utils.log("Rowcell: " + rowcell + " is backwards oriented, swapping.")
        if jbrik_cube.fivesixmidrowcrossrowcells_l.__contains__(rowcell):
            # its a leftswap
            movestrlist = get_leftcross_solution_list(facetosolve, adjrowcell, rowcell)
            log_utils.log("leftswap " + swaptype + " rowcell: " + rowcell + " of color: " + rowcellccolor + " and adjacent cell: "
                          + adjrowcell + " with color: " + adjrowcellcolor)
        else:
            # its a rightswap
            movestrlist = get_rightcross_solution_list(facetosolve, adjrowcell, rowcell)
            log_utils.log("Rightswap " + swaptype + " rowcell: " + rowcell + " of color: " + rowcellccolor + " and adjacent cell: "
                          + adjrowcell + " with color: " + adjrowcellcolor)

        for rmove in movestrlist:
            cube = jbrik_solver_move_lib.perform_rotation_str(rmove, cube)

        if swaptype != "back":
            cube = jbrik_solver_move_lib.perform_rotation_str("3CW2", cube)

            for rmove in movestrlist:
                cube = jbrik_solver_move_lib.perform_rotation_str(rmove, cube)

    return cube

# TODO we're looping when we align for an LR swap and the LR swap identifies another swap first, performs it and revert this alignment... thinking something like add priority move to cube state
def align_oppface_crossrowcell_to_adj_ccolor(facetosolve, cube):
    oppfacecrossrowcells = jbrik_cube.get_cross_rowcell_for_face(facetosolve)

    for crossrowcell in oppfacecrossrowcells:
        if is_middle_rowcell_solved(crossrowcell, cube):
            log_utils.log("Rowcell: " + crossrowcell + " is already solved.")
            continue

        crossrowcellcolor = cube.get_cell_val_by_rowcell(crossrowcell)
        ccolor = cube.get_center_color_for_facenum(facetosolve)
        adjrowcell = jbrik_cube.get_adjrowccell_for_rowcell(crossrowcell)
        adjrowcellcolor = cube.get_cell_val_by_rowcell(adjrowcell)
        adjrowcellccolor = cube.get_center_color_for_rowcell(adjrowcell)

        # will be an issue here if all adjcell have ccolor
        if adjrowcellcolor == ccolor:
            continue

        # if crossrowcellcolor is not facetosolve ccolor then it must be one of the adj ccolors
        testrowcell = adjrowcell
        testrowcellccolor = adjrowcellccolor
        rotcount = 0
        while adjrowcellcolor != testrowcellccolor:
            if rotcount > 3:
                log_utils.log("No solveface alignment.")
                return cube

            log_utils.log("Rotate face: " + facetosolve.__str__()
                          + " CW1 and check for match to adjacent face center color.")
            rotcount = rotcount + 1
            testrowcell = jbrik_cube.get_dest_pos_for_face_rotation(testrowcell, facetosolve.__str__() + "CW1")
            testrowcellccolor = cube.get_center_color_for_rowcell(testrowcell)

        # we've idetified a match, rotate here
        if rotcount > 0:
            rotstr = facetosolve.__str__() + "CW" + rotcount.__str__()
            log_utils.log("Perform transition: " + rotstr)
            cube = jbrik_solver_move_lib.perform_rotation_str(rotstr, cube)

            log_utils.log("Solveface orbit rowcell: " + testrowcell + " of color: " + adjrowcellcolor
                          + " is aligned for LR check.")
            return cube

    return cube

def perform_lr_solve_on_cross_rowcells(facetosolve, cube):
    oppfacecrossrowcells = jbrik_cube.get_cross_rowcell_for_face(facetosolve)

    for crossrowcell in oppfacecrossrowcells:
        crossrowcellcolor = cube.get_cell_val_by_rowcell(crossrowcell)
        adjrowcell = jbrik_cube.get_adjrowccell_for_rowcell(crossrowcell)
        adjrowcellcolor = cube.get_cell_val_by_rowcell(adjrowcell)
        adjrowcellcolorccolor = cube.get_center_color_for_rowcell(adjrowcell)

        # if this rowcell is already aligned with adjacent color same as center color
        if adjrowcellcolor == adjrowcellcolorccolor:
            adjrowcell = jbrik_cube.get_adjrowccell_for_rowcell(crossrowcell)
            lrrowcells = jbrik_cube.get_oppface_centerrowcell_lr_middle_destcells(crossrowcell)
            lcrossrowcell = lrrowcells.split(" ")[0]
            rcrossrowcell = lrrowcells.split(" ")[1]

            lcrossccolor = cube.get_center_color_for_rowcell(lcrossrowcell)
            rcrossccolor = cube.get_center_color_for_rowcell(rcrossrowcell)

            if crossrowcellcolor == lcrossccolor:
                log_utils.log("Perform an L cross solve on: " + crossrowcell)
                solutionlist = get_leftcross_solution_list(facetosolve, lcrossrowcell, adjrowcell)

                for lmove in solutionlist:
                    cube = jbrik_solver_move_lib.perform_rotation_str(lmove, cube)

                    if not is_middle_rowcell_solved(crossrowcell, cube):
                        cube = swap_backwards_oriented_mid_rowcell(facetosolve, crossrowcell, "swap", cube)
                #return cube

            elif crossrowcellcolor == rcrossccolor:
                log_utils.log("Perform a R cross solve on: " + crossrowcell)
                solutionlist = get_rightcross_solution_list(facetosolve, rcrossrowcell, adjrowcell)

                for rmove in solutionlist:
                    cube = jbrik_solver_move_lib.perform_rotation_str(rmove, cube)

                if not is_middle_rowcell_solved(crossrowcell, cube):
                    cube = swap_backwards_oriented_mid_rowcell(facetosolve, crossrowcell, "swap", cube)

                #return cube

    return cube

# TODO I think we can consolidate these
def get_leftcross_solution_list(facetosolve, lcrossrowcell, adjrowcell):
    tface = facetosolve.__str__()
    lface = jbrik_cube.get_face_for_rowcell(lcrossrowcell).__str__()
    fface = jbrik_cube.get_face_for_rowcell(adjrowcell).__str__()
    solutionlist = [tface + "CC1", lface + "CC1", tface + "CW1", lface + "CW1", tface + "CW1", fface + "CW1", tface
                    + "CC1", fface + "CC1"]

    return solutionlist

def get_rightcross_solution_list(facetosolve, rcrossrowcell, adjrowcell):
    tface = facetosolve.__str__()
    rface = jbrik_cube.get_face_for_rowcell(rcrossrowcell).__str__()
    fface = jbrik_cube.get_face_for_rowcell(adjrowcell).__str__()
    solutionlist = [tface + "CW1", rface + "CW1", tface + "CC1", rface + "CC1", tface + "CC1", fface + "CC1", tface + "CW1", fface + "CW1"]

    return solutionlist