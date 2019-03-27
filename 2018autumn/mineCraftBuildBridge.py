#导入所需模块
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

#连接到MineCraft游戏
mc = minecraft.Minecraft.create()

#用isSafeFeet函数判断玩家是否安全
def isSafeFeet():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.postToChat("not safe")
    else:
        mc.postToChat("safe")
def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y - 1,pos.z)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x,pos.y-1,pos.z,block.GLASS.id)

while True:
    buildBridge()
