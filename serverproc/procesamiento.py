import math
class Procesador:

    def __init__(self,topico,datos):
        self.topico=topico
        datos=datos[1:-1].split(",")
        self.datos=[0]*19+[float(i) for i in datos]
        self.n = len(datos)
        print(self.datos, self.n)
        self.coef = [-0.0028779, 0.0023849, -0.0081774, 0.0102338, -0.0268824, 0.0338147, -0.0705264, 0.0990351, -0.2074783,
                0.6218039, 0.6218039, -0.2074783, 0.0990351, -0.705264, 0.0338147, -0.0268824, 0.0102338, -0.0081774,
                0.0023849, -0.0028779]
        self.coef2 = [-0.0039666, -0.0086890, -0.0026846, 0.0317854, 0.0621680, 0.0083552, -0.1189332, -0.1589852,
                 -0.0055601, 0.1920132, 0.1920132, -0.0055601, -0.1589852, -0.1189332, 0.0083552, 0.0621680, 0.0317854,
                 -0.0026846, -0.0086890, -0.0039666]
        self.orden = 19
        self.frec = 100
        self.filtrar()
        self.picos()
        self.hr()
        self.var()
    def filtrar(self):
        self.datosFiltrados=[0 for i in range(self.n)]
        self.filtro2=[0 for i in range(self.n)]
        for i in range(self.orden,self.n+self.orden):
            for j in range(self.orden):
                self.datosFiltrados[i-self.orden] += self.datos[i-j] * self.coef[j]
                self.filtro2[i - self.orden] += self.datos[i - j] * self.coef2[j]

    def __rollingMean(self,ecg):
        mean = [0 for i in range(self.n)]
        max = -1
        for i in range(self.n):
            if (i < self.n - self.frec):
                for j in range(i, i+self.frec):
                    if(j<self.n):
                        mean[i] += (ecg[i] * ecg[j])
                    else:
                        break
            mean[i] =mean[i]/ self.frec
            mean[i] =mean[i]* 100
            if (mean[i] > max):
                max=mean[i]
        return max
    def picos(self):
        mean = self.__rollingMean(self.filtro2)
        peaks = [0 for i in range(self.n)]
        pos =[]
        for i in range(self.n):
            if (self.filtro2[i] < mean):
                peaks[i] = 0
            else :
                peaks[i] = self.filtro2[i]
        for i in range(1,self.n-1):
            if (not(((peaks[i] - peaks[i + 1]) > 0) and ((peaks[i - 1] - peaks[i]) < 0))):
                peaks[i] = 0
            else:
                pos.append(i)
        self.posiciones=pos
    def hr(self):
        n=len(self.posiciones)
        der = [0 for i in range(n-1)]
        av = 0
        max = -1
        min = float('inf')
        for i in range(1,n):
            der[i - 1]=(self.posiciones[i]-self.posiciones[i-1]) * 60 / self.frec
            av += der[i-1]
            if (der[i-1] > max):
                max=der[i-1]
            if (der[i-1] < min):
                min=der[i-1]
        av=av/n
        print("HR:",av)
    def var(self):
        diff =[0 for i in range(len(self.posiciones)-1)]
        f = [0 for i in range(len(self.posiciones)-1)]
        n=len(diff)
        meandiff = 0
        rmssd = 0
        nn50 = 0
        nn20 = 0
        std = 0
        for i in range(1,n-1) :
            resta = self.posiciones[i] - self.posiciones[i - 1]
            diff[i - 1] = resta
            f[i - 1] = (resta * 60) / self.frec
            meandiff += diff[i - 1]
            rmssd += resta**2
            if (resta > 50):
                nn50+=1
            if (resta > 20):
                nn20+=1
        pnn50=(nn50 / n) * 100
        pnn20 = (nn20 / n) * 100
        meandiff /= n
        rmssd = math.sqrt(rmssd / (n - 2))
        for i in range(n):
            std += math.pow(diff[i] - meandiff, 2)
        std = math.sqrt(std / (n - 1))

