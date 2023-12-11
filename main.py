from experiment import experiment
import algorithms as alg


if __name__ == '__main__':
    algorithms = [
        alg.Algorithm('Венгерский мин', alg.hungarian_min),
        alg.Algorithm('Венгерский макс', alg.hungarian_max),
        alg.Algorithm('Жадный', alg.greedy_max),
        alg.Algorithm('Бережливый', alg.greedy_min),
        alg.Algorithm('Жадно-бережливый', alg.greedy_thrifty),
        alg.Algorithm('Бережливо-жадный', alg.thrifty_greedy)
    ]

    experiment(20, 50, 0.1, 0.11, 0.95, 1, algorithms)
