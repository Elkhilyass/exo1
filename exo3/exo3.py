def processLines(lines) -> str:
        N=int(lines[0])
        T=int(lines[1])
        backlog = T
        for i in range(2,N+2):
                V,U = map(int, lines[i].split())
                backlog = backlog- V + U
                
                if backlog < 0:
                        return "KO"
                     
        if backlog == 0:
                return "OK"
        else:
                return "KO"
        
with open("exo3/sample/input2.txt") as input1:
        lines = input1.readlines()
result = processLines(lines)
print(result)