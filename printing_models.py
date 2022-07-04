def print_models(unprinted_designs, comleted_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        comleted_models.append(current_design)

def show_comleted_models(comleted_models):
    print("\nThe following models have been printed:")
    for comleted_model in comleted_models:
        print(comleted_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahetron']
comleted_models = []

print_models(unprinted_designs, comleted_models)
show_comleted_models(comleted_models)
