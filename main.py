from interface.app import App
from interface.control_frame import ControlFrame
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

    if __name__ == '__main__':
        app = App()
        ControlFrame(app)
        app.mainloop()
