import jbrik_solver_phase1
import jbrik_solver_phase2
import jbrik_solver_phase3
import jbrik_cube
import jbrik_solver_move_lib

cubeStateStr = "rrwbwbyybggoooyyrgowwbybyworgborrwybrgyogwwoobggybrgwr" # solved in 12/21/39
#cubeStateStr = "bbwywgyrwowgooowgrgrgwybyowrgrrroywobwbygyryybbogbrobg" # solved in 12/13/41
#cubeStateStr = "obggwgowogrbboyygwrwobyobwwrogbrgwrryyrrgyyrgwybobobwy" # solved in 6/21/32
#cubeStateStr = "wwowwwoyggbroowwyoogbryyyrbgyrgrbrgwgrybgowryrobgbobby" # solved in 12/18 loops on 3
#cubeStateStr = "gowowyygwgyrwoobogybowyyyrwbbbwrrrggogorgbbwyorwbbyrgr" # solved in 15/19 loops on 3
#cubeStateStr = "owowwwywbgoryorobowowgyybrwryggrgyrybrrggoybbwygobbgbr" # solved in 0/17 loops on 3
#cubeStateStr = "grrowgwywgbbrorogygoobyggwyrbborwrwwborygwogbyywrbbyyo" # solved in 13/16 loops on 3
#cubeStateStr = "gorowbbyowoywobbgbryrrygowowrbgrrywgwyywgogyygrrbbbwgo" # solved in 16/26 loops on 3
#cubeStateStr = "rwgrwbbbbyoogoyogwyrgrybrgwyyoorwbgyobgygrworgwwwbybor" # solved in 11/26 loops on 3
#cubeStateStr = "bwrwwwyworoggobygborogyyrrgwyybrbyrgworggowywbroobbgyb" # solved in 0/26 loops on 3
#cubeStateStr = "bbrgwgrogbwwwobgyowobyyboygbrobrrwoyggyogworywyrgbwrry" # solved in 6/19 loops on 3
#cubeStateStr = "rgrowgrgwyworoobwoybbryygboyoworywywbrbrgbgyyowgbbgrwg" # solved in 9/27 loops on 3


Cube = jbrik_cube.JbrikCube(cubeStateStr)

Cube = jbrik_solver_phase1.solvecross(Cube)
print
Cube.print_cube("", True)
Cube.print_solvemap()
#raw_input("\nPress Enter to continue...\n")

Cube = jbrik_solver_phase2.solvecrosscorners(Cube)
print
Cube.print_cube("", True)
Cube.print_solvemap()
#raw_input("\nPress Enter to continue...\n")

Cube = jbrik_solver_phase3.solve_middle(Cube)
print
Cube.print_cube("", True)
Cube.print_solvemap()
#raw_input("\nPress Enter to continue...\n")
