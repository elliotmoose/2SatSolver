# INPUT_FILE_PATH = "./example1.cnf"
INPUT_FILE_PATH = "./2sat.cnf"

def parse_cnf_file(file_path):
    """
    Generates the array of clauses
    """
    cnf_file = open(file_path, "r")
    lines = cnf_file.readlines()

    clauses = [[]]
    for line in lines:
        components = line.strip("\n").split(" ")

        if line[0] == "c":
            print("Comment: ", line[2:])
        elif line[0] == "p":        
            print("Problem. Format: {0} Variables: {1} Clauses: {2}".format(components[1], components[2], components[3]))
        else: #clause lines
            for literal in components:            
                if literal == "0" : #terminate clause and move to next
                    if lines.index(line) != len(lines)-1:
                        clauses.append([])
                else:                
                    clauses[len(clauses)-1].append(literal)

    return clauses