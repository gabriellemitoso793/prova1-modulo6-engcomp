import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
from collections import deque

# Algumas partes do código foram tiradas do repositorio do professor, do grupo e do meu repositório 

class ControleTartaruga(Node):
    # a funções add_command e init foram tirada de uma postagem no medium sobre deque, queue e python
    def __init__(self):
        super().__init__('controle_tartaruga')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 5)
        self.command_queue = deque()

    def add_comando(self, vx, vy, vt, tempo):
        self.command_queue.append((vx, vy, vt, tempo))

    def executar_comando(self):
        while self.command_queue:
            vx, vy, vt, tempo = self.command_queue.popleft()
            twist = Twist()
            twist.linear.x = vx
            twist.linear.y = vy
            twist.angular.z = vt
            self.publisher_.publish(twist)
            self.get_logger().info('Executando comando: ' + str((vx, vy, vt, tempo)))
            rclpy.sleep(tempo / 1000.0)

def main(args=None):
    rclpy.init(args=args)
    controle_tartaruga = ControleTartaruga()
    controle_tartaruga.add_comando(0.0, 1.0, 0.0, 1000) 
    controle_tartaruga.executar_comando()
    rclpy.spin(controle_tartaruga)
    controle_tartaruga.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
