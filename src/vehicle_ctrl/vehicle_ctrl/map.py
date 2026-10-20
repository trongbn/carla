import carla
import time
import sys

def main():
    try:
        # Kết nối với CARLA server ở cổng mặc định 2000
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        print("Connecting to CARLA server...")
        
        world = client.get_world()
        current_map = world.get_map()
        
        # Kiểm tra xem Town01 đã được tải chưa
        if 'Town01' not in current_map.name:
            print("Town01 is not loaded. Loading Town01...")
            world = client.load_world('Town01')
            time.sleep(2) # Đợi bản đồ load xong
        else:
            print("Town01 is already loaded in the simulator.")

        # Lấy dữ liệu topology (mạng lưới đường) của bản đồ hiện tại
        map_data = world.get_map()
        print(f"Map topology loaded successfully! Name: {map_data.name}")
        
    except RuntimeError as e:
        print(f"Failed to connect to CARLA: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()