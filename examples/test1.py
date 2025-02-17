from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# SOUTH, EAST, NORTH, WEST

# Intersection in
sim.create_segment(0, (lane_space/2, length+intersection_size/2), (lane_space/2, intersection_size/2))
sim.create_segment(1, (length+intersection_size/2, -lane_space/2), (intersection_size/2, -lane_space/2))
sim.create_segment(2, (-lane_space/2, -length-intersection_size/2), (-lane_space/2, -intersection_size/2))
sim.create_segment(3, (-length-intersection_size/2, lane_space/2), (-intersection_size/2, lane_space/2))
# Intersection out
sim.create_segment(4, (-lane_space/2, intersection_size/2), (-lane_space/2, length+intersection_size/2))
sim.create_segment(5, (intersection_size/2, lane_space/2), (length+intersection_size/2, lane_space/2))
sim.create_segment(6, (lane_space/2, -intersection_size/2), (lane_space/2, -length-intersection_size/2))
sim.create_segment(7, (-intersection_size/2, -lane_space/2), (-length-intersection_size/2, -lane_space/2))
# Straight
sim.create_segment(8,(lane_space/2, intersection_size/2), (lane_space/2, -intersection_size/2))
sim.create_segment(9, (intersection_size/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_segment(10, (-lane_space/2, -intersection_size/2), (-lane_space/2, intersection_size/2))
sim.create_segment(11, (-intersection_size/2, lane_space/2), (intersection_size/2, lane_space/2))
# Right turn
sim.create_quadratic_bezier_curve(12, (lane_space/2, intersection_size/2), (lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
sim.create_quadratic_bezier_curve(13, (intersection_size/2, -lane_space/2), (lane_space/2, -lane_space/2), (lane_space/2, -intersection_size/2))
sim.create_quadratic_bezier_curve(14, (-lane_space/2, -intersection_size/2), (-lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_quadratic_bezier_curve(15, (-intersection_size/2, lane_space/2), (-lane_space/2, lane_space/2), (-lane_space/2, intersection_size/2))
# Left turn
sim.create_quadratic_bezier_curve(16, (lane_space/2, intersection_size/2), (lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_quadratic_bezier_curve(17, (intersection_size/2, -lane_space/2), (-lane_space/2, -lane_space/2), (-lane_space/2, intersection_size/2))
sim.create_quadratic_bezier_curve(18, (-lane_space/2, -intersection_size/2), (-lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
sim.create_quadratic_bezier_curve(19, (-intersection_size/2, lane_space/2), (lane_space/2, lane_space/2), (lane_space/2, -intersection_size/2))

vg = VehicleGenerator({
    'vehicles': [
        (1, {'path': [0, 8, 6], 'v': 16.6}),
        (1, {'path': [0, 12, 5], 'v': 16.6})
        ]
    })
sim.add_vehicle_generator(vg)



# v = Vehicle({'path': [0], 'x': 20, 'v':16.6})
# sim.add_vehicle(v)

# v = Vehicle({'path': [0]})
# sim.add_vehicle(v)

win = Window(sim)
win.run()
win.show()
