#!/usr/bin/env python
# encoding: utf-8
import math
import rand_generator

# Classe para gera��o de n�meros aleat�rios segundos v�rias distribui��es
# Apenas a distribui��o exponencial negativa est� definida
class Random:

    stream_i = 0

    def __init__(self, seed):
        self.next_normal = 0
        self.has_next_normal = False
        self.seed = seed
        self.stream = Random.stream_i
        rand_generator.randst(seed, self.stream)
        Random.stream_i += 1

    def exponencial(self, media):
        # """Gera um n�mero segundo uma distribui��o exponencial negativa de m�dia m
        return (-media*math.log(rand_generator.rand(self.stream)))

    def normal(self, dist):
        if self.has_next_normal:
            self.has_next_normal = False
            return self.next_normal

        v1 = 1
        v2 = 2
        while(v1**2 + v2**2 > 1):
            #print 'start'
            v1 = 2 * rand_generator.rand(self.stream) - 1
            v2 = 2 * rand_generator.rand(self.stream) - 1
            # print(self.stream)
            # print(v1)
            # print(v2)

        w = math.pow(v1,2) + math.pow(v2,2)

        y1 = v1 * math.sqrt(-2 * math.log(w) / w )
        y2 = v2 * math.sqrt(-2 * math.log(w) / w )

        x1 = dist[0] + y1 * dist[1]
        x2 = dist[0] + y2 * dist[1]

        self.next_normal = x2
        self.has_next_normal = True
        return x1

    def reset_stream_count():
        Random.stream_i = 0

if __name__ == "__main__":
	rand = Random(100)
	for i in range(10):
		print(rand.normal((10,1)))
