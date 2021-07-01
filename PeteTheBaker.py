def cakes(recipe, available):
    max_amount=999999
    for ingredient, amount in recipe.items():
        found = False
        for wh_ingredient, wh_amount in available.items(): 
            if wh_ingredient == ingredient:
                max_amount = wh_amount//amount if wh_amount//amount<max_amount else max_amount
                found=True
                break
        if not found:
            max_amount=0
            break
    return max_amount
