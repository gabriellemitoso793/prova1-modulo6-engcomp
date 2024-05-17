import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Comandos para a tartaruga.')
    parser.add_argument('--vx', type=float, default=0.0, help='Velocidade em x')
    parser.add_argument('--vy', type=float, default=0.0, help='Velocidade em y')
    parser.add_argument('--vt', type=float, default=0.0, help='Velocidade angular')
    parser.add_argument('-t', type=int, required=True, help='Tempo em ms')
    return parser.parse_args()

def main():
    args = parse_args()
    print(f'Movimentação enviada: vx={args.vx}, vy={args.vy}, vt={args.vt}, tempo={args.tempo}')

if __name__ == '__main__':
    main()