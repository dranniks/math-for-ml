import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt

def proj(vec1: npt.NDArray[np.float64], vec2: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:

    if vec1.shape != vec2.shape:
        raise ValueError("Vectors must have same shape")
    if np.linalg.norm(vec2) == 0:
        raise ValueError("Second vector can't be zero")

    vec_proj = (np.dot(vec1, vec2) / np.dot(vec2, vec2)) * vec2
    
    return vec_proj


v1 = np.array([-5, 5])
v2 = np.array([4, 8])
print(proj(v1, v2))

def draw2DProj(vec1: npt.NDArray[np.float64], vec2: npt.NDArray[np.float64], vec_proj: npt.NDArray[np.float64]):
    if vec1.size != 2 or vec2.size != 2 or vec_proj.size != 2:
        raise ValueError("Only 2D vectors can be visualized")
    # задаем область графика
    plt.figure(figsize=(6, 6))
    # отображаем вектора
    plt.quiver(0, 0, vec1[0], vec1[1], angles='xy', scale_units='xy', scale=1, label="vector1")
    plt.quiver(0, 0, vec2[0], vec2[1], angles='xy', scale_units='xy', scale=1, label="vector2")
    plt.quiver(0, 0, vec_proj[0], vec_proj[1], angles='xy', scale_units='xy', scale=1, label="projection")
    # отображаем пунктирную линию с вектора на проекцию
    plt.plot([vec1[0], vec_proj[0]], [vec1[1], vec_proj[1]], linestyle='--')
    # отображаем точки
    plt.scatter(vec1[0], vec1[1])
    plt.scatter(vec2[0], vec2[1])
    plt.scatter(vec_proj[0], vec_proj[1])
    # подписываем объекты на графике
    plt.text(vec1[0], vec1[1], "vec1")
    plt.text(vec2[0], vec2[1], "vec2")
    plt.text(vec_proj[0], vec_proj[1], "vec_proj")
    # отображаем оси координат
    plt.axhline(0)
    plt.axvline(0)
    # включаем сетку
    plt.grid()
    # одинаковый масштаб осей, чтобы график не растянулся
    plt.axis("equal")
    # границы графика
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    # отображение легенды
    plt.legend()
    # показываем график
    plt.show()

draw2DProj(v1, v2, proj(v1, v2))