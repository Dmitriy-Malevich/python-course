def print_models(unprinted_design, completed_models):

    while unprinted_design:
        current_design = unprinted_design.pop()
        # Печать модели на 3D принтере.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):

# Вывод всех готовых моделей.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_design = ['iphone case', 'robot pendent', 'dodecahedron']
completed_models = []
print_models(unprinted_design[:], completed_models)
show_completed_models(completed_models)