# import random
# # from modules.test import my_module

# # print(my_module.pi)

# # random_int = random.randint(1,10)
# # print(random_int)

# random_float = random.random() * 5


# print(random_float)


states_of_america = ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Federated States of Micronesia','Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

print(states_of_america[0])

states_of_america.append("Lukeland")

states_of_america.extend(["test1","test2"])

print(states_of_america.pop(1))
print(states_of_america.pop(len(states_of_america)-1))
print(states_of_america)