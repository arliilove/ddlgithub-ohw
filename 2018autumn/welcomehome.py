import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
stayed_time = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))
    if pos.x == -28 and pos.z == -40:
        mc.postToChat("welcome home")
        stayed_time = stayed_time + 1
        print(str(stayed_time))
        if stayed_time >=5:
            mc.player.setTilePos(-28,50,-40)
            stayed_time = 0
    else:
        stayed_time = 0
        
     
