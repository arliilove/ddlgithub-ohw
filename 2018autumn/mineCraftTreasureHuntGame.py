#导入所需模块
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

#连接到Minecraft游戏
mc = minecraft.Minecraft.create()

#设置被检测的钻石方块
diamond_pos = mc.player.getTilePos()
diamond_pos.x = diamond_pos.x + 1
mc.setBlock(diamond_pos.x,diamond_pos.y,diamond_pos.z,block.DIAMOND_BLOCK.id)

#检测钻石方块是否被击打
def checkHit():
    #将被打击的方块事件进行记录，形成一个列表
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:
            mc.postToChat("HIT")
#测试击打检测函数
#while True:
#    time.sleep(1)
#    checkHit()
            
    
