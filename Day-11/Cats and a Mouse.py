def catAndMouse(x, y, z):

    distance_CatA = abs(x - z)
    distance_CatB = abs(y - z)

    if distance_CatA == distance_CatB:
        return "Mouse C"

    elif distance_CatA < distance_CatB:
        return "Cat A"

    else:
        return "Cat B"
