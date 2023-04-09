from dimod import ConstrainedQuadraticModel, Binary
from dwave.system import LeapHybridCQMSampler
import timeit
import numpy as np
#%%
start = timeit.default_timer()
#Construct a problem: Of and Constraints:
def create_problem(mu,sigma):

    x = [Binary("x%s" % i) for i in range(len(sigma))]

    objective = sum([mu[i] * x[i] for i in range(len(mu))])
    objective =sum(
        [sigma[i, j] * x[i] * x[j] for i in range(len(mu)) for j in range(len(mu))]
    
    )
    return objective
N = 60
mu = np.random.rand(N,)
sigma = np.random.rand(N,N)
qubo_1 = create_problem(mu, sigma)
print(qubo_1)
#%%constructing the CQM model 
start = timeit.default_timer()
cqm = ConstrainedQuadraticModel()
cqm.set_objective((qubo_1))
cqm.add_constraint(sum([Binary("x%s" % i) for i in range(len(sigma))])== 4, "constraint1")
print(cqm)

#%%HybridSolver
sampler = LeapHybridCQMSampler() 
sampleset = sampler.sample_cqm(cqm)
print(sampleset) 
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  
if len(feasible_sampleset):      
   best = feasible_sampleset.first
print(best)
#%%Time calculation
stop = timeit.default_timer()
general=stop - start
print('Time: ', general) 
