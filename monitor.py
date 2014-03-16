import collections
import functools
import mcpi.minecraft as minecraft
import mcpi.block as block
import sys
from time import sleep



def print_changed_block(new_block_type):
	print "Block changed: " + str(new_block_type)

def trigger_block(target_information, new_block_type):
	print "Target = " + str(target_information.blocklocation)
	print "Block changed: " + str(new_block_type)
	(x,y,z) = target_information.blocklocation
	target_information.worldconnection.setBlock(x, y, z, new_block_type)




def monitor_block(serverinfo, on_change_fn):
	(x,y,z) = serverinfo.blocklocation

	old_block_state = 0
	while True:
		new_block_state = serverinfo.worldconnection.getBlock(x, y, z)
		if new_block_state != old_block_state:
			on_change_fn(new_block_state)
			old_block_state = new_block_state
		sleep(0.1)
	

Point = collections.namedtuple("Point", ["x", "y", "z"])
Server = collections.namedtuple("Server", ["worldconnection", "blocklocation"])


if __name__ == "__main__":
	source_world = minecraft.Minecraft.create("tosh")
	target_world = minecraft.Minecraft.create("w500")	
	source_information = Server(source_world, Point(574, 3, 1406))
	target_information = Server(target_world, Point(-175, 1, -39))

	changefn = functools.partial(trigger_block, target_information)
	monitor_block(source_information, changefn)


