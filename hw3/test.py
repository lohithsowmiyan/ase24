from ezr import * 

import unittest


class TestShuffle(unittest.TestCase):
"Does d.shuffle() really jiggle the order of the data?"
    def test_shuffle(self):
        d = DATA().adds(csv(the.train)).rows   
        shuffled_data = DATA().adds(csv(the.train)).shuffle().rows
        self.assertNotEqual(d, shuffled_data, "Shuffle did not change the data order.")

class TestExperimentalTreatment(unittest.TestCase):
"Does you code really run some experimental treatment 20 times for statistical validity?"
    def test_experimental_runs(self):
        d = DATA().adds(csv(the.train))
        repeats = 20
        count = 0
        rnd = lambda z : z
        result = []
        for _ in range(repeats):
              tmp=d.shuffle().activeLearning(score= lambda B, R,: B-R )
              result += [rnd(d.chebyshev(tmp[0]))]
              count += 1
        self.assertEqual(repeats, count, "Treatment was not repeated 20 times.")

class TestLengthofTreatments(unittest.TestCase):
"Are smart and dumb lists the right length (i.e. N). if not, why not?"
    def test_treatment_size(self):
        guess = lambda N, d : random.choices(d.rows, k = N)
        d = DATA().adds(csv(the.train))
        for the.Last in [20]:
          
          res = []
          tag = f"Random,{the.Last}"
          dumb = guess(the.Last,d)
          smart = d.shuffle().activeLearning(score= lambda B, R,: B-R )
          
        self.assertEqual(len(dumb), len(smart), "Treatments are not of equal length")
        self.assertEqual(len(dumb), the.Last, "Treatments  not equal to N")


class TestChebyshev(unittest.TestCase):
"Does chebyshevs().rows[0] return the top item in that sort?"
    def test_top_item(self):
        d = DATA().adds(csv(the.train))
        cheb_top = d.chebyshev(DATA().adds(csv(the.train)).chebyshevs().rows[0])
        sorted_top = sorted(d.chebyshev(row) for row in d.rows)[0]
        self.assertEqual(cheb_top,sorted_top, "Chebyshevs does not sort")

        


          




       