import mcpi.minecraft as minecraft
import sys
import time


servername = "localhost"
if len(sys.argv) > 1:
	servername = sys.argv[1]
print "Opening world '%s'" % servername
world = minecraft.Minecraft.create(servername)
print "Connected to world"

x, y, z = world.player.getPos()
world.postToChat("X = %d" % x)
world.postToChat("Y = %d" % y)
world.postToChat("Z = %d" % z)
