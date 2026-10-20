import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class GoalRemapper(Node):
    def __init__(self):
        super().__init__('goal_remapper')
        # Lắng nghe topic từ RViz2
        self.sub = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.goal_callback,
            10)
        
        # Phát lại vào topic của CARLA waypoint publisher
        self.pub = self.create_publisher(
            PoseStamped,
            '/carla/ego_vehicle/goal',
            10)
            
        self.get_logger().info("Goal Remapper Started: Forwarding /goal_pose -> /carla/ego_vehicle/goal")

    def goal_callback(self, msg):
        self.get_logger().info(f"Received goal from RViz: X={msg.pose.position.x:.2f}, Y={msg.pose.position.y:.2f}")
        # Chuyển tiếp nguyên bản tin nhắn tọa độ
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoalRemapper()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()