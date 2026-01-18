Meter
Permission

class Garage {
	public:
		enum ParkingType { REGULAR, HANDICAPPED, COMPACT };
		enum VehicleType { TRUCK, CAR, MOTORCYCLE, BUS };
		bool is_full();
		bool is_empty();
		Space find_nearest_vacant();
		void park_vehicle();
		void release_vehice(Vehicle veh);
	private:
		int capacity;
		vector<Space> vacant;
		vector<Space> occupied;
};

class Space {
	bool is_vacant;
	Vehicle vehicle;
	ParkingType type;
	int distance;
};

class Vehicle {
	VehicleType type;
	string license;
	string state;
	string color;
};

