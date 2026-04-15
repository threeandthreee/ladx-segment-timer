# General RAM layout
wram = 0xC000
wramSize = 0x2000
wramLow = 0xC100
wramLowSize = 0x100
# WRAM actually starts at 0xC000, but we mostly care about 0xD800 and up
wramHigh = 0xD800
wramHighSize = 0x800
hram = 0xFF80
hramSize = 0x80
snapshotSize = 0x4000

# General game state
gameStateAddress = 0xDB95
validGameStates = {0x0B, 0x0C}
gameStateResetThreshold = 0x06
seed = 0xFAF00
seedSize = 0x10

# GFX
gfxStart = 0xB0000
gfxHashSize = 0x040

# Entrance/location data
room = 0xFFF6
mapId = 0xFFF7
indoorFlag = 0xDBA5
spawnMap = 0xDB60
spawnRoom = 0xDB61
spawnX = 0xDB62
spawnY = 0xDB63
entranceRoomOffset = 0xD800
transitionState = 0xC124
transitionTargetX = 0xC12C
transitionTargetY = 0xC12D
transitionScrollX = 0xFF96
transitionScrollY = 0xFF97
linkMotionState = 0xC11C
transitionSequence = 0xC16B 
screenCoord = 0xFFFA

rupeesHigh = 0xDB5D
rupeesLow = 0xDB5E
addRupeesHigh = 0xDB8F
addRupeesLow = 0xDB90
removeRupeesHigh = 0xDB91
removeRupeesLow = 0xDB92
