# Qiskit and docplex imports
from qiskit_optimization.algorithms import CplexOptimizer
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.translators import from_docplex_mp
from docplex.mp.model import Model
#%%construction the problem using docplex
def create_problem(mu: np.array, sigma: np.array, total: int = 4) -> QuadraticProgram:
    """Solve the quadratic program using docplex."""

    mdl = Model()
    x = [mdl.binary_var("x%s" % i) for i in range(len(sigma))]

    objective = mdl.sum([mu[i] * x[i] for i in range(len(mu))])
    objective =mdl.sum(
        [sigma[i, j] * x[i] * x[j] for i in range(len(mu)) for j in range(len(mu))]
    )
    mdl.minimize(objective)
    cost = mdl.sum(x)
    mdl.add_constraint(cost == total)

    qp = from_docplex_mp(mdl)
    return qp
N = 60
mu = np.random.rand(N,)
sigma = np.random.rand(N,N)
qubo = create_problem(mu, sigma)
print(qubo.prettyprint())
#%%Cplex
t1=timeit.default_timer()
result = CplexOptimizer().solve(qubo)
print(timeit.default_timer()-t1)
#print(result.prettyprint())
