import matplotlib.pyplot as plt
import numpy as np

def recherche_direction_vent(angle_deg):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(angle_deg / (360.0 / len(directions))) % len(directions)
    return directions[index]

def dessiner_direction_vent(angle_deg, centre=(0, 0)):
    # Conversion degrés en radians
    angle_rad = np.deg2rad(angle_deg)

    # Calcul des coordonnées du point extrémité
    longueur_ligne = 1.0
    end_point = (centre[0] + longueur_ligne * np.cos(angle_rad), centre[1] + longueur_ligne * np.sin(angle_rad))

    # Tracer le quadrant
    plt.figure(figsize=(6, 6))
    plt.plot([centre[0], end_point[0]], [centre[1], end_point[1]], 'r', linewidth=2)  # Ligne de direction
    plt.scatter(centre[0], centre[1], color='b', marker='o', label='Centre')  # Centre du quadrant
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Direction du vent: {recherche_direction_vent(angle_deg)}")
    plt.xlabel("Est")
    plt.ylabel("Nord")
    plt.grid(True)

    # Ajouter la rose des vents
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    for i, direction in enumerate(directions):
        angle_rad = np.deg2rad(i * 45)
        x = centre[0] + 1.3 * np.cos(angle_rad)
        y = centre[1] + 1.3 * np.sin(angle_rad)
        plt.text(x, y, direction, ha='center', va='center')

    plt.legend()
    plt.show()

# Test de la fonction avec un angle de 45 degrés et un centre par défaut
dessiner_direction_vent(45)