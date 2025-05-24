class NeedlemanWunschStepper:
    def __init__(self, seq1, seq2, match=1, mismatch=-1, gap=-2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.filas = len(seq1) + 1
        self.columnas = len(seq2) + 1
        self.i = 1
        self.j = 1

        self.matriz = [[0] * self.columnas for _ in range(self.filas)]
        self.direccion = [[""] * self.columnas for _ in range(self.filas)]

        for i in range(self.filas):
            self.matriz[i][0] = i * gap
            self.direccion[i][0] = "↑"
        for j in range(self.columnas):
            self.matriz[0][j] = j * gap
            self.direccion[0][j] = "←"
        self.direccion[0][0] = "0"

    def step(self):
        if self.i >= self.filas:
            return None

        match = self.matriz[self.i - 1][self.j - 1] + (self.match if self.seq1[self.i - 1] == self.seq2[self.j - 1] else self.mismatch)
        delete = self.matriz[self.i - 1][self.j] + self.gap
        insert = self.matriz[self.i][self.j - 1] + self.gap

        max_score = max(match, delete, insert)
        self.matriz[self.i][self.j] = max_score

        if max_score == match:
            self.direccion[self.i][self.j] = "↖"
        elif max_score == delete:
            self.direccion[self.i][self.j] = "↑"
        else:
            self.direccion[self.i][self.j] = "←"

        pos = (self.i, self.j)
        self.j += 1
        if self.j == self.columnas:
            self.j = 1
            self.i += 1

        return self.matriz, self.direccion, pos

    def run_all(self):
        while self.step() is not None:
            continue
        return self.matriz, self.direccion

    def traceback(self):
        alineacion1 = ""
        alineacion2 = ""
        i = len(self.seq1)
        j = len(self.seq2)

        while i > 0 or j > 0:
            dir_actual = self.direccion[i][j]
            if dir_actual == "↖":
                alineacion1 = self.seq1[i - 1] + alineacion1
                alineacion2 = self.seq2[j - 1] + alineacion2
                i -= 1
                j -= 1
            elif dir_actual == "↑":
                alineacion1 = self.seq1[i - 1] + alineacion1
                alineacion2 = "-" + alineacion2
                i -= 1
            elif dir_actual == "←":
                alineacion1 = "-" + alineacion1
                alineacion2 = self.seq2[j - 1] + alineacion2
                j -= 1
            else:
                break

        return alineacion1, alineacion2
