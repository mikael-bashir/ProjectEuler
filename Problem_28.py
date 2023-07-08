# notice a general pattern for the sum of corners in each spiral
# in general, the sum of corners of each spiral, indexed from second spiral 1, is 16i**2 + 4*i + 4
# however, this doesn't work for centre dot, so we can just add 1 and exclude centre from calculations
# in general, an n x n grid (with n odd) will have (n-1)/2 + 1 spirals
# so we have 501 spirals, 500 excluding centre


diag_sum = 0
for i in range(1, 501):
    diag_sum += ((16*(i**2))+(4*i)+4)

print(diag_sum + 1)
