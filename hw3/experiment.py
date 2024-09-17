def hw3():
      guess = lambda N, d : random.choices(d.rows, k = N)
      d = DATA().adds(csv(the.train))
      x    = len(d.cols.x)

      scoring_policies = [('exploit', lambda B, R,: B-R),
                            ('explore', lambda B, R:  (exp(B) + exp(R))/ (1E-30 + abs(exp(B) - exp(R))))]

      repeats = 20
      rnd = lambda z : z

      b4 = [d.chebyshev(row) for row in d.rows]
      somes = [stats.SOME(b4,f"asIs,{len(d.rows)}")]

      for the.Last in [20,30,40,50]:
        res = []
        tag = f"Random,{the.Last}"
        res = [guess(the.Last,d) for _ in range(20)]
        res = [sorted([d.chebyshev(row) for row in lst])[0] for lst in res]
        #print(res)
        somes +=   [stats.SOME(res,    tag)]

      for what,how in scoring_policies:
        for the.Last in [0, 20, 30, 40]:
          for the.branch in [False, True]:
            start = time()
            result = []
            runs = 0
            for _ in range(repeats):
              tmp=d.shuffle().activeLearning(score=how)
              runs += len(tmp)
              result += [rnd(d.chebyshev(tmp[0]))]

            pre=f"{what}/b={the.branch}" if the.Last >0 else "rrp"
            tag = f"{pre},{int(runs/repeats)}"
            #print(tag, f": {(time() - start) /repeats:.2f} secs")
            somes +=   [stats.SOME(result,    tag)]
            
      stats.report(somes, 0.01)
