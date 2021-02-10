class LinearCongruenceEquation:
	def __init__(self, a, b, m):
		self.a = a
		self.b = b
		self.m = m
		self.d = gcd(a,m)
		
	def intermediate_steps(self):
		intermediate_a = floor(self.a/self.d)#volver entero
		intermediate_b = floor(self.b/self.d)#volver entero
		intermediate_m = floor(self.m/self.d)#volver entero
		intermediate_inverse_a = intermediate_a.inverse_mod(intermediate_m)
		result = intermediate_inverse_a * intermediate_b % intermediate_m
		result_vector = [intermediate_a, intermediate_b, intermediate_m, intermediate_inverse_a, result]
		return result_vector	
	
	def solution_vector(self):
		steps_vector = self.intermediate_steps()
		solution_vector_info = [steps_vector[4] + j* steps_vector[2] for j in range(self.d)] #[4]result [2]intermediate_m
		return solution_vector_info
	
	def show_solution(self):
		results_list_incongruence = self.solution_vector()
		results_list_incongruence_str = list(map(str, results_list_incongruence))
		last_results_list_incongruence_str = results_list_incongruence_str.pop()
		text = ', '.join(results_list_incongruence_str) + ' y ' + last_results_list_incongruence_str
		return text