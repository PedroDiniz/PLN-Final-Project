from sellers import sellers
import math

def get_suggestions(text):
    txt = open("words.txt")
    suggests =[]
    distance = ((len(text)+2)/3)
    max_distance = len(text)
    seller = sellers()
    for line in txt:
        line = line.strip('\n\r')
        #result = seller.sellers_algorithm(text,line)
        if math.fabs(len(line)-len(text)) <= distance:
            result = seller.sellers_algorithm_optmized(text,line, distance)
            if result <= distance and result > 0:
                if result <= max_distance:
                    suggests.append((line,result))
                    if len(suggests) > 5:
                        suggests = sorted(suggests, key=lambda result: result[1])
                        max_distance = suggests[-2][1]
                        suggests.pop(-1)
    return [i[0] for i in suggests]
        
def new_word(text):
    f = open("words.txt", 'a')
    f.write(text+'\n')
    f.close()

if __name__ == '__main__':
    a = get_suggestions("caza")
    print a
