class sellers:
    
    def __init__(self):
        self.result = 0
        
    def fi(self, letterA, letterB): 
        if letterA.lower() == letterB.lower():
            self.result = 0
            return 0
        else:
            self.result = 2
            return 2
        
    def sellers_algorithm(self, text1, text2):
        line = (len(text1)+1)
        column = (len(text2)+1)
        matrix = []
        for i in range(line):
            matrix.append([0]*column)
        
        for i in range(line):
            matrix[i][0] = i
            
        for i in range(column):
            matrix[0][i] = i
            
            
        for i in range(1, line): 
            for j in range(1, column): 
                minimum = min((matrix[i-1][j]+1), (matrix[i][j-1]+1), (matrix[i-1][j-1]+self.fi(text1[i-1], text2[j-1])))
                matrix[i][j] = minimum
        return matrix[-1][-1]
    
    def sellers_algorithm_optmized(self, text1, text2, max_distance):
        line = (len(text1)+1)
        column = (len(text2)+1)
        matrix = []
        minimum_in_line = 0
        for i in range(line):
            matrix.append([0]*column)
        
        for i in range(line):
            matrix[i][0] = i
            
        for i in range(column):
            matrix[0][i] = i
            
            
        for i in range(1, line): 
            if minimum_in_line > 0:
                if minimum_in_line > max_distance:
                    return -1
            minimum_in_line = column
            for j in range(1, column): 
                minimum = min((matrix[i-1][j]+1), (matrix[i][j-1]+1), (matrix[i-1][j-1]+self.fi(text1[i-1], text2[j-1])))
                matrix[i][j] = minimum
                if minimum < minimum_in_line:
                    minimum_in_line = minimum
        return matrix[-1][-1]