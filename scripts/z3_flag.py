from z3 import *
import random

NUM_CHARS = 64;
for q in range(50):
    solver = Solver()
    
    input_chars = [BitVec(f'c{i}', 8) for i in range(NUM_CHARS)]
    
    # Let's track valid characters - ASCII printable range
    for i in range(64):
         solver.add(input_chars[i] >= 32)  # Printable ASCII starts at space (32)
         solver.add(input_chars[i] <= 126) # Ends at tilde (~)
    
    # constraints like input_chars[0:6] = 'ISCTF{', 
    guaranteed_constraints = [
    ]
    # raw contraints gathered from the source code 
    constraints = [
    ] 
    
    random.shuffle(constraints)
    
    def add_constraint(constraint):
        # Check if the constraint is satisfiable with the current constraints
        if solver.check(constraint) == sat:
            solver.add(constraint)
    
    # Add all these constraints to the solver
    for constraint in guaranteed_constraints:
        solver.add(constraint)
    for constraint in constraints:
        add_constraint(constraint)
    # Attempt to find a solution
    if solver.check() == sat:
        model = solver.model()
        
        # Print the solution, trim it to where the null terminator would be or the end
        for i in range(NUM_CHARS):
            char = model[input_chars[i]].as_long()
            #print(char)
            print(chr(char), end='')
    else:
        print("No solution found with current constraints")
