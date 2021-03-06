Experiment(description='Re-analysis of GEFCOM data for purposes of thesis',
           data_dir='../data/gefcom_temp',
           max_depth=10, 
           random_order=True,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=9,
           sd=2, 
           jitter_sd=0.1,
           max_jobs=400, 
           verbose=False,
           make_predictions=False,
           skip_complete=True,
           results_dir='../results/2014-11-11-gefcom-revisited-hint/',
           iters=250,
           base_kernels='SE,Per,Const,Noise',
           random_seed=9001,
           period_heuristic=3,
           max_period_heuristic=3,
           period_heuristic_type='min',
           subset=True,
           subset_size=250,
           full_iters=10,
           bundle_size=5,
           additive_form=True,
           mean='ff.MeanZero()',      # Starting mean
           kernel='ff.SumKernel(operands=[ff.NoiseKernel(sf=2.08809790524), ff.SqExpKernel(dimension=0, lengthscale=3.69609349113, sf=4.14119813054), ff.PeriodicKernel(dimension=0, lengthscale=1.50649327194, period=0.00768179907041, sf=2.57935847545), ff.ProductKernel(operands=[ff.SqExpKernel(dimension=0, lengthscale=1.56492614779, sf=0.616294504434), ff.PeriodicKernel(dimension=0, lengthscale=1.27065410184, period=-5.90050698288, sf=1.0683061003)]), ff.SqExpKernel(dimension=0, lengthscale=-6.27430126974, sf=1.4870890117), ff.SqExpKernel(dimension=0, lengthscale=-8.37650628924, sf=0.709324950518)])' , # Starting kernel
           lik='ff.LikGauss(sf=-np.Inf)', # Starting likelihood
           score='bic',
           stopping_criteria=['no_improvement'],
           improvement_tolerance=0.1,
           search_operators=[('A', ('+', 'A', 'B'), {'A': 'kernel', 'B': 'base'}),
                             ('A', ('*', 'A', 'B'), {'A': 'kernel', 'B': 'base-not-const'}),
                             ('A', ('*-const', 'A', 'B'), {'A': 'kernel', 'B': 'base-not-const'}),
                             ('A', 'B', {'A': 'kernel', 'B': 'base'}),
                             ('A', ('None',), {'A': 'kernel'})])
