class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, capacity_weight):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self._capacity_weight = capacity_weight


    def get_capacity(self):
        return self._capacity_weight

    def set_capacity(self, capacity_weight):
        if capacity_weight > 0:
            self._capacity_weight = capacity_weight
        else:
            print("Неправильна вага!")

    def describe(self):
        return f"Транспортний засіб ID: {self.vehicle_id}, Тип: {self.vehicle_type}, Вантажопідйомність: {self._capacity_weight} кг."

    def update_status(self, status):
        print(f"Транспортний засіб {self.vehicle_id} має статус: {status}")

    @staticmethod
    def calculate_fuel(distance_km, fuel_efficiency_l_per_km):
        return distance_km * fuel_efficiency_l_per_km


class Truck(Vehicle):
    def __init__(self, vehicle_id, capacity_weight, num_of_axles):
        super().__init__(vehicle_id, "Вантажівка", capacity_weight)
        self.num_of_axles = num_of_axles

    def describe(self):
        return f"Вантажівка ID: {self.vehicle_id}, Вантажопідйомність: {self._capacity_weight} кг, Кількість осей: {self.num_of_axles}"


class ServiceProvider:
    def __init__(self, provider_name):
        self.provider_name = provider_name

    def provide_service(self):
        return f"Сервіс надано постачальником: {self.provider_name}"


class TruckWithService(Truck, ServiceProvider):
    def __init__(self, vehicle_id, capacity_weight, num_of_axles, provider_name):
        Truck.__init__(self, vehicle_id, capacity_weight, num_of_axles)
        ServiceProvider.__init__(self, provider_name)

    def describe(self):
        return f"Вантажівка ID: {self.vehicle_id}, Вантажопідйомність: {self._capacity_weight} кг, Кількість осей: {self.num_of_axles}, Постачальник сервісу: {self.provider_name}"


vehicle = Vehicle("V001", "Легковий автомобіль", 1000)
print(vehicle.describe())
vehicle.update_status("Вільний")

truck = Truck("T001", 5000, 6)
print(truck.describe())
truck.update_status("У дорозі")

truck_with_service = TruckWithService("T002", 8000, 8, "Сервіс Техно")
print(truck_with_service.describe())
print(truck_with_service.provide_service())


fuel_needed = Truck.calculate_fuel(200, 0.15)
print(f"Необхідна кількість палива: {fuel_needed} л")
