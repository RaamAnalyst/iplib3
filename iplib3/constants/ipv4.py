"""IPv4 constants"""

# IPv4 constants
IPV4_SEGMENT_BIT_COUNT     = 8
IPV4_MIN_SEGMENT_COUNT     = 4 # IPv4 shortening is not valid
IPV4_MAX_SEGMENT_COUNT     = 4
IPV4_MIN_SEGMENT_VALUE     = 0x0 # (0)
IPV4_MAX_SEGMENT_VALUE     = 0xFF # (255)
IPV4_MIN_VALUE             = 0 # 0x0*0x100**0
IPV4_MAX_VALUE             = 4294967295 # 0xFF*0x100**3 + 0xFF*0x100**2 + 0xFF*0x100**1 + 0xFF*0x100**0
                           # 0xFF_FF_FF_FF (8)
