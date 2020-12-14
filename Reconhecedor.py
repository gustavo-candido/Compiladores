from AFD import AFD
import os

class Reconhecedor:

    def __init__(self, file_path):
        self.file = open(file_path, "r")
        self.line = 0
        self.column = 0
        self.read_bytes = 0
        self.AFD = AFD()
        self.identificadores = []
        self.tokens = []

        while self.file.tell() != os.fstat(self.file.fileno()).st_size:
            line = self.line
            column = self.column
            ret = self.search(1,"")
            if ret != '<null>':
                self.tokens.append(((line,column),ret))
            if '<id,' in ret:
                if ret[4:-1] not in self.identificadores:
                    self.identificadores.append(ret[4:-1])
        
    
    def search(self, vertex, buffer):
        if vertex in self.AFD.finals:
            ret = self.AFD.finals[vertex].split(',')

            if vertex in self.AFD.retreat:
                self.read_bytes-=1
                self.file.seek(self.read_bytes)

                buffer = buffer[0:-1]
            if len(ret) == 1:
                return ('<{}>'.format(ret[0]))

            if ret[1] == 'buffer':
                return ('<{},{}>'.format(ret[0], buffer))

            return ('<{},{}>'.format(ret[0], ret[1]))

        neighbors = self.AFD.graph[vertex]
        next_char = self.file.read(1)
        self.read_bytes+=1

        self.column+=1

        if next_char == '\n':
            self.line+=1
            self.column=0
            
        for aresta in neighbors:
            vertex_neighbor, c_list = aresta

            if next_char in c_list:
                if next_char == '':
                    return self.search(vertex_neighbor, buffer + ' ')

                return self.search(vertex_neighbor, buffer+next_char)

    