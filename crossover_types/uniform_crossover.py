from random import randint


def uniform_crossover(parent_1, parent_2):
    mask = ['0' for _ in range(len(parent_1))]
    for i in range(len(mask)):
        random_value = randint(1, 10)
        if random_value <= 5:
            mask[i] = '1'
    crossover_mask = ''.join(mask)
    offspring_1 = []
    offspring_2 = []
    for parent_1_dna, parent_2_dna, mask_value in zip(parent_1, parent_2, crossover_mask):
        if mask_value == '1':
            offspring_1.append(parent_1_dna)
            offspring_2.append(parent_2_dna)
        else:
            offspring_1.append(parent_2_dna)
            offspring_2.append(parent_1_dna)
    return [''.join(offspring_1), ''.join(offspring_2)]


parent1 = '11111111111'
parent2 = '00000000000'
offsprings = uniform_crossover(parent1, parent2)
print("\n Single point crossover")
print("Parent 1    : " + parent1)
print("Parent 2    : " + parent2)
print("Offspring 1 : " + offsprings[0])
print("Offspring 2 : " + offsprings[1])
