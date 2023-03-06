import math

from constants.constans import kpd, recommendation_gear_ratio
from true_round.true_round import round


def engine(force, velocity, diameter, open_transmission, closed_transmission, coupling, bearing, count_bearing):
    power = force * velocity
    n_sum = open_transmission * closed_transmission * pow(bearing, count_bearing) * coupling
    power_engine = power / n_sum
    recommendation = recommendation_gear_ratio['belt'] * recommendation_gear_ratio['cylindrical']
    w_val = (2 * velocity) / diameter
    n_engine = (30*w_val*recommendation)/math.pi
    return power_engine, n_sum, n_engine


def main():
    print("Привет это программа кинематического рассчёта (ленточного транспортёра)")
    F = 4  # Тяговое усилие
    V = 0.6  # Скорость ленты
    D = 0.3  # Диаметр барабана
    open_transmission = kpd['belt']  # Открытая передача
    closed_transmission = kpd['cylindrical']  # Закрытая передача
    coupling = kpd['coupling']  # муфта
    bearing = kpd['bearings']  # пары подшипников
    count_bearing = 3  # Колличество пар подшипников
    power_engine, n_sum, n_engine = engine(F, V, D, open_transmission, closed_transmission, coupling, bearing, count_bearing)


if __name__ == "__main__":
    main()
