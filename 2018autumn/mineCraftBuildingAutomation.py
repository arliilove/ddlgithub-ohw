import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()


def buildHouse(x,y,z,L,W,H,M):
    for i in range(L):
        for j in range(H):
            mc.setBlock(x+i,y+j,z,M)
    for k in range(1,W):
        for j in range(H):
            mc.setBlock(x,y+j,z+k,M)
    for i in range(L):
        for j in range(H):
            mc.setBlock(x+i,y+j,z+W-1,M)
    for k in range(1,W):
        for j in range(H):
            mc.setBlock(x+L-1,y+j,z+k,M) 
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    print("x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    mc.postToChat("x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    
