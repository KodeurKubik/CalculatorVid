import math

char_, short_, int_, long_, void_ = 0, 0, 0, 0, 0
int8_t = char_
uint8_t = char_
int16_t = short_
uint16_t = short_
int32_t = int_
uint32_t = int_
uint64_t = long_
int64_t = long_

float_ = 0.00
size_t = 0
double_ = 0
score_t = int64_t
CHAR_BIT = 8

ptrdiff_t = int_

UINT8, INT16 = char_, short_

RAW_FILE, IVF_FILE, WEBM_FILE = 0, 1, 2
MB_FEATURE_TREE_PROBS, MAX_MB_SEGMENTS = 3, 4
BLOCK_CONTEXTS = 4
MAX_PARTITIONS = 8

BLOCK_TYPES, PREV_COEF_CONTEXTS, COEF_BANDS, ENTROPY_NODES = 4, 3, 8, 11

MV_PROB_CNT = 2 + 8 - 1 + 10

TOKEN_BLOCK_Y1, TOKEN_BLOCK_UV, TOKEN_BLOCK_Y2, TOKEN_BLOCK_TYPES = 0, 1, 2, 3
CURRENT_FRAME, LAST_FRAME, GOLDEN_FRAME, ALTREF_FRAME, NUM_REF_FRAMES = 0, 1, 2, 3, 4

MASK_NONE, MASK_FIRST_BIT = 0, 1

CNT_BEST, CNT_ZEROZERO, CNT_NEAREST, CNT_NEAR, CNT_SPLITMV = 0, 0, 1, 2, 3

ID_EBML = 0x1a45dfa3
ID_EBML_VERSION = 0x4286
ID_EBML_READ_VERSION = 0x42f7
ID_EBML_MAX_ID_LENGTH = 0x42f2
ID_EBML_MAX_SIZE_LENGTH = 0x42f3
ID_DOCTYPE = 0x4282
ID_DOCTYPE_VERSION = 0x4287
ID_DOCTYPE_READ_VERSION = 0x4285

ID_VOID = 0xec
ID_CRC32 = 0xbf

ID_SEGMENT = 0x18538067

ID_SEEK_HEAD = 0x114d9b74
ID_SEEK = 0x4dbb
ID_SEEK_ID = 0x53ab
ID_SEEK_POSITION = 0x53ac

ID_INFO = 0x1549a966
ID_TIMECODE_SCALE = 0x2ad7b1
ID_DURATION = 0x4489

ID_CLUSTER = 0x1f43b675
ID_TIMECODE = 0xe7
ID_BLOCK_GROUP = 0xa0
ID_SIMPLE_BLOCK = 0xa3

ID_BLOCK = 0xa1
ID_BLOCK_DURATION = 0x9b
ID_REFERENCE_BLOCK = 0xfb

ID_TRACKS = 0x1654ae6b
ID_TRACK_ENTRY = 0xae
ID_TRACK_NUMBER = 0xd7
ID_TRACK_UID = 0x73c5
ID_TRACK_TYPE = 0x83
ID_FLAG_ENABLED = 0xb9
ID_FLAG_DEFAULT = 0x88
ID_FLAG_LACING = 0x9c
ID_TRACK_TIMECODE_SCALE = 0x23314f
ID_LANGUAGE = 0x22b59c
ID_CODEC_ID = 0x86
ID_CODEC_PRIVATE = 0x63a2

ID_VIDEO = 0xe0
ID_PIXEL_WIDTH = 0xb0
ID_PIXEL_HEIGHT = 0xba
ID_PIXEL_CROP_BOTTOM = 0x54aa
ID_PIXEL_CROP_TOP = 0x54bb
ID_PIXEL_CROP_LEFT = 0x54cc
ID_PIXEL_CROP_RIGHT = 0x54dd
ID_DISPLAY_WIDTH = 0x54b0
ID_DISPLAY_HEIGHT = 0x54ba

ID_AUDIO = 0xe1
ID_SAMPLING_FREQUENCY = 0xb5
ID_CHANNELS = 0x9f
ID_BIT_DEPTH = 0x6264

ID_CUES = 0x1c53bb6b
ID_CUE_POINT = 0xbb
ID_CUE_TIME = 0xb3
ID_CUE_TRACK_POSITIONS = 0xb7
ID_CUE_TRACK = 0xf7
ID_CUE_CLUSTER_POSITION = 0xf1
ID_CUE_BLOCK_NUMBER = 0x5378

TYPE_UNKNOWN, TYPE_MASTER, TYPE_UINT, TYPE_FLOAT, TYPE_INT, TYPE_STRING, TYPE_BINARY = 0, 1, 2, 3, 4, 5, 6

LIMIT_STRING = (1 << 20)
LIMIT_BINARY = (1 << 24)
LIMIT_BLOCK = (1 << 30)
LIMIT_FRAME = (1 << 28)

DESC_FLAG_NONE = 0
DESC_FLAG_MULTI = (1 << 0)
DESC_FLAG_SUSPEND = (1 << 1)
DESC_FLAG_OFFSET = (1 << 2)

BLOCK_FLAGS_LACING = 6

LACING_NONE = 0
LACING_XIPH = 1
LACING_FIXED = 2
LACING_EBML = 3

TRACK_TYPE_VIDEO = 1
TRACK_TYPE_AUDIO = 2

TRACK_ID_VP8 = "V_VP8"
TRACK_ID_VORBIS = "A_VORBIS"

VERSION_STRING = " v0.9.7"

VPX_CODEC_OK, VPX_CODEC_CORRUPT_FRAME, VPX_CODEC_MEM_ERROR, VPX_CODEC_UNSUP_BITSTREAM = 0, 1, 2, 3

FRAME_HEADER_SZ, KEYFRAME_HEADER_SZ = 3, 7

DC_PRED, V_PRED, H_PRED, TM_PRED, B_PRED, NEARESTMV, NEARMV, ZEROMV, NEWMV, SPLITMV, MB_MODE_COUNT = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
B_DC_PRED, B_TM_PRED, B_VE_PRED, B_HE_PRED, B_LD_PRED, B_RD_PRED, B_VR_PRED, B_VL_PRED, B_HD_PRED, B_HU_PRED, LEFT4X4, ABOVE4X4, ZERO4X4, NEW4X4, B_MODE_COUNT = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

sixtap_filters = [
    [0, 0, 128, 0, 0, 0],
    [0, -6, 123, 12, -1, 0],
    [2, -11, 108, 36, -8, 1],
    [0, -9, 93, 50, -6, 0],
    [3, -16, 77, 77, -16, 3],
    [0, -6, 50, 93, -9, 0],
    [1, -8, 36, 108, -11, 2],
    [0, -1, 12, 123, -6, 0]
]

bilinear_filters = [
    [0, 0, 128, 0, 0, 0],
    [0, 0, 112, 16, 0, 0],
    [0, 0, 96, 32, 0, 0],
    [0, 0, 80, 48, 0, 0],
    [0, 0, 64, 64, 0, 0],
    [0, 0, 48, 80, 0, 0],
    [0, 0, 32, 96, 0, 0],
    [0, 0, 16, 112, 0, 0]
]
    
BORDER_PIXELS = 16

k_coeff_entropy_update_probs = [
        [
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [176, 246, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [223, 241, 252, 255, 255, 255, 255, 255, 255, 255, 255],
                [249, 253, 253, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 244, 252, 255, 255, 255, 255, 255, 255, 255, 255],
                [234, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [253, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 246, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [239, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 248, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [251, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [251, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 254, 253, 255, 254, 255, 255, 255, 255, 255, 255],
                [250, 255, 254, 255, 254, 255, 255, 255, 255, 255, 255],
                [254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ]
        ],
        [
            [
                [217, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [225, 252, 241, 253, 255, 255, 254, 255, 255, 255, 255],
                [234, 250, 241, 250, 253, 255, 253, 254, 255, 255, 255]
            ],
            [
                [255, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [223, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [238, 253, 254, 254, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 248, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [249, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 253, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [247, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [252, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [253, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 254, 253, 255, 255, 255, 255, 255, 255, 255, 255],
                [250, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ]
        ],
        [
            [
                [186, 251, 250, 255, 255, 255, 255, 255, 255, 255, 255],
                [234, 251, 244, 254, 255, 255, 255, 255, 255, 255, 255],
                [251, 251, 243, 253, 254, 255, 254, 255, 255, 255, 255]
            ],
            [
                [255, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [236, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [251, 253, 253, 254, 254, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ]
        ],
        [
            [
                [248, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [250, 254, 252, 254, 255, 255, 255, 255, 255, 255, 255],
                [248, 254, 249, 253, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 253, 253, 255, 255, 255, 255, 255, 255, 255, 255],
                [246, 253, 253, 255, 255, 255, 255, 255, 255, 255, 255],
                [252, 254, 251, 254, 254, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 254, 252, 255, 255, 255, 255, 255, 255, 255, 255],
                [248, 254, 253, 255, 255, 255, 255, 255, 255, 255, 255],
                [253, 255, 254, 254, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 251, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [245, 251, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [253, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 251, 253, 255, 255, 255, 255, 255, 255, 255, 255],
                [252, 253, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 252, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [249, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 253, 255, 255, 255, 255, 255, 255, 255, 255],
                [250, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ],
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
            ]
        ]
]


k_default_y_mode_probs = [112, 86, 140, 37]
k_default_uv_mode_probs = [162, 101, 204]


k_default_coeff_probs = [
        [
            [
                [128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128],
                [128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128],
                [128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128]
            ],
            [
                [253, 136, 254, 255, 228, 219, 128, 128, 128, 128, 128],
                [189, 129, 242, 255, 227, 213, 255, 219, 128, 128, 128],
                [106, 126, 227, 252, 214, 209, 255, 255, 128, 128, 128]
            ],
            [
                [1, 98, 248, 255, 236, 226, 255, 255, 128, 128, 128],
                [181, 133, 238, 254, 221, 234, 255, 154, 128, 128, 128],
                [78, 134, 202, 247, 198, 180, 255, 219, 128, 128, 128]
            ],
            [
                [1, 185, 249, 255, 243, 255, 128, 128, 128, 128, 128],
                [184, 150, 247, 255, 236, 224, 128, 128, 128, 128, 128],
                [77, 110, 216, 255, 236, 230, 128, 128, 128, 128, 128]
            ],
            [
                [1, 101, 251, 255, 241, 255, 128, 128, 128, 128, 128],
                [170, 139, 241, 252, 236, 209, 255, 255, 128, 128, 128],
                [37, 116, 196, 243, 228, 255, 255, 255, 128, 128, 128]
            ],
            [
                [1, 204, 254, 255, 245, 255, 128, 128, 128, 128, 128],
                [207, 160, 250, 255, 238, 128, 128, 128, 128, 128, 128],
                [102, 103, 231, 255, 211, 171, 128, 128, 128, 128, 128]
            ],
            [
                [1, 152, 252, 255, 240, 255, 128, 128, 128, 128, 128],
                [177, 135, 243, 255, 234, 225, 128, 128, 128, 128, 128],
                [80, 129, 211, 255, 194, 224, 128, 128, 128, 128, 128]
            ],
            [
                [1, 1, 255, 128, 128, 128, 128, 128, 128, 128, 128],
                [246, 1, 255, 128, 128, 128, 128, 128, 128, 128, 128],
                [255, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128]
            ]
        ],
        [
            [
                [198, 35, 237, 223, 193, 187, 162, 160, 145, 155, 62],
                [131, 45, 198, 221, 172, 176, 220, 157, 252, 221, 1],
                [68, 47, 146, 208, 149, 167, 221, 162, 255, 223, 128]
            ],
            [
                [1, 149, 241, 255, 221, 224, 255, 255, 128, 128, 128],
                [184, 141, 234, 253, 222, 220, 255, 199, 128, 128, 128],
                [81, 99, 181, 242, 176, 190, 249, 202, 255, 255, 128]
            ],
            [
                [1, 129, 232, 253, 214, 197, 242, 196, 255, 255, 128],
                [99, 121, 210, 250, 201, 198, 255, 202, 128, 128, 128],
                [23, 91, 163, 242, 170, 187, 247, 210, 255, 255, 128]
            ],
            [
                [1, 200, 246, 255, 234, 255, 128, 128, 128, 128, 128],
                [109, 178, 241, 255, 231, 245, 255, 255, 128, 128, 128],
                [44, 130, 201, 253, 205, 192, 255, 255, 128, 128, 128]
            ],
            [
                [1, 132, 239, 251, 219, 209, 255, 165, 128, 128, 128],
                [94, 136, 225, 251, 218, 190, 255, 255, 128, 128, 128],
                [22, 100, 174, 245, 186, 161, 255, 199, 128, 128, 128]
            ],
            [
                [1, 182, 249, 255, 232, 235, 128, 128, 128, 128, 128],
                [124, 143, 241, 255, 227, 234, 128, 128, 128, 128, 128],
                [35, 77, 181, 251, 193, 211, 255, 205, 128, 128, 128]
            ],
            [
                [1, 157, 247, 255, 236, 231, 255, 255, 128, 128, 128],
                [121, 141, 235, 255, 225, 227, 255, 255, 128, 128, 128],
                [45, 99, 188, 251, 195, 217, 255, 224, 128, 128, 128]
            ],
            [
                [1, 1, 251, 255, 213, 255, 128, 128, 128, 128, 128],
                [203, 1, 248, 255, 255, 128, 128, 128, 128, 128, 128],
                [137, 1, 177, 255, 224, 255, 128, 128, 128, 128, 128]
            ]
        ],
        [
            [
                [253, 9, 248, 251, 207, 208, 255, 192, 128, 128, 128],
                [175, 13, 224, 243, 193, 185, 249, 198, 255, 255, 128],
                [73, 17, 171, 221, 161, 179, 236, 167, 255, 234, 128]
            ],
            [
                [1, 95, 247, 253, 212, 183, 255, 255, 128, 128, 128],
                [239, 90, 244, 250, 211, 209, 255, 255, 128, 128, 128],
                [155, 77, 195, 248, 188, 195, 255, 255, 128, 128, 128]
            ],
            [
                [1, 24, 239, 251, 218, 219, 255, 205, 128, 128, 128],
                [201, 51, 219, 255, 196, 186, 128, 128, 128, 128, 128],
                [69, 46, 190, 239, 201, 218, 255, 228, 128, 128, 128]
            ],
            [
                [1, 191, 251, 255, 255, 128, 128, 128, 128, 128, 128],
                [223, 165, 249, 255, 213, 255, 128, 128, 128, 128, 128],
                [141, 124, 248, 255, 255, 128, 128, 128, 128, 128, 128]
            ],
            [
                [1, 16, 248, 255, 255, 128, 128, 128, 128, 128, 128],
                [190, 36, 230, 255, 236, 255, 128, 128, 128, 128, 128],
                [149, 1, 255, 128, 128, 128, 128, 128, 128, 128, 128]
            ],
            [
                [1, 226, 255, 128, 128, 128, 128, 128, 128, 128, 128],
                [247, 192, 255, 128, 128, 128, 128, 128, 128, 128, 128],
                [240, 128, 255, 128, 128, 128, 128, 128, 128, 128, 128]
            ],
            [
                [1, 134, 252, 255, 255, 128, 128, 128, 128, 128, 128],
                [213, 62, 250, 255, 255, 128, 128, 128, 128, 128, 128],
                [55, 93, 255, 128, 128, 128, 128, 128, 128, 128, 128]
            ],
            [
                [128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128],
                [128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128],
                [128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128]
            ]
        ],
        [
            [
                [202, 24, 213, 235, 186, 191, 220, 160, 240, 175, 255],
                [126, 38, 182, 232, 169, 184, 228, 174, 255, 187, 128],
                [61, 46, 138, 219, 151, 178, 240, 170, 255, 216, 128]
            ],
            [
                [1, 112, 230, 250, 199, 191, 247, 159, 255, 255, 128],
                [166, 109, 228, 252, 211, 215, 255, 174, 128, 128, 128],
                [39, 77, 162, 232, 172, 180, 245, 178, 255, 255, 128]
            ],
            [
                [1, 52, 220, 246, 198, 199, 249, 220, 255, 255, 128],
                [124, 74, 191, 243, 183, 193, 250, 221, 255, 255, 128],
                [24, 71, 130, 219, 154, 170, 243, 182, 255, 255, 128]
            ],
            [
                [1, 182, 225, 249, 219, 240, 255, 224, 128, 128, 128],
                [149, 150, 226, 252, 216, 205, 255, 171, 128, 128, 128],
                [28, 108, 170, 242, 183, 194, 254, 223, 255, 255, 128]
            ],
            [
                [1, 81, 230, 252, 204, 203, 255, 192, 128, 128, 128],
                [123, 102, 209, 247, 188, 196, 255, 233, 128, 128, 128],
                [20, 95, 153, 243, 164, 173, 255, 203, 128, 128, 128]
            ],
            [
                [1, 222, 248, 255, 216, 213, 128, 128, 128, 128, 128],
                [168, 175, 246, 252, 235, 205, 255, 255, 128, 128, 128],
                [47, 116, 215, 255, 211, 212, 255, 255, 128, 128, 128]
            ],
            [
                [1, 121, 236, 253, 212, 214, 255, 255, 128, 128, 128],
                [141, 84, 213, 252, 201, 202, 255, 219, 128, 128, 128],
                [42, 80, 160, 240, 162, 185, 255, 205, 128, 128, 128]
            ],
            [
                [1, 1, 255, 128, 128, 128, 128, 128, 128, 128, 128],
                [244, 1, 255, 128, 128, 128, 128, 128, 128, 128, 128],
                [238, 1, 255, 128, 128, 128, 128, 128, 128, 128, 128]
            ]
        ]
]


k_mv_entropy_update_probs = [
    [
        237,
        246,
        253, 253, 254, 254, 254, 254, 254,
        254, 254, 254, 254, 254, 250, 250, 252, 254, 254
    ],
    [
        231,
        243,
        245, 253, 254, 254, 254, 254, 254,
        254, 254, 254, 254, 254, 251, 251, 254, 254, 254
    ]
]


def k_default_mv_probs():
    return [
        [
            162,
            128,
            225, 146, 172, 147, 214, 39, 156,
            128, 129, 132, 75, 145, 178, 206, 239, 254, 254
        ],
        [
            164,
            128,
            204, 170, 119, 235, 140, 230, 228,
            128, 130, 130, 74, 148, 180, 203, 236, 254, 254
        ]
    ]


dc_q_lookup = [
        4, 5, 6, 7, 8, 9, 10, 10,
        11, 12, 13, 14, 15, 16, 17, 17,
        18, 19, 20, 20, 21, 21, 22, 22,
        23, 23, 24, 25, 25, 26, 27, 28,
        29, 30, 31, 32, 33, 34, 35, 36,
        37, 37, 38, 39, 40, 41, 42, 43,
        44, 45, 46, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66,
        67, 68, 69, 70, 71, 72, 73, 74,
        75, 76, 76, 77, 78, 79, 80, 81,
        82, 83, 84, 85, 86, 87, 88, 89,
        91, 93, 95, 96, 98, 100, 101, 102,
        104, 106, 108, 110, 112, 114, 116, 118,
        122, 124, 126, 128, 130, 132, 134, 136,
        138, 140, 143, 145, 148, 151, 154, 157
]

ac_q_lookup = [
        4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27,
        28, 29, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 42, 43,
        44, 45, 46, 47, 48, 49, 50, 51,
        52, 53, 54, 55, 56, 57, 58, 60,
        62, 64, 66, 68, 70, 72, 74, 76,
        78, 80, 82, 84, 86, 88, 90, 92,
        94, 96, 98, 100, 102, 104, 106, 108,
        110, 112, 114, 116, 119, 122, 125, 128,
        131, 134, 137, 140, 143, 146, 149, 152,
        155, 158, 161, 164, 167, 170, 173, 177,
        181, 185, 189, 193, 197, 201, 205, 209,
        213, 217, 221, 225, 229, 234, 239, 245,
        249, 254, 259, 264, 269, 274, 279, 284
]


kf_y_mode_probs = [145, 156, 163, 128]
kf_uv_mode_probs = [142, 114, 183]

kf_b_mode_probs = [
        [
            [231, 120, 48, 89, 115, 113, 120, 152, 112],
            [152, 179, 64, 126, 170, 118, 46, 70, 95],
            [175, 69, 143, 80, 85, 82, 72, 155, 103],
            [56, 58, 10, 171, 218, 189, 17, 13, 152],
            [144, 71, 10, 38, 171, 213, 144, 34, 26],
            [114, 26, 17, 163, 44, 195, 21, 10, 173],
            [121, 24, 80, 195, 26, 62, 44, 64, 85],
            [170, 46, 55, 19, 136, 160, 33, 206, 71],
            [63, 20, 8, 114, 114, 208, 12, 9, 226],
            [81, 40, 11, 96, 182, 84, 29, 16, 36]
        ],
        [
            [134, 183, 89, 137, 98, 101, 106, 165, 148],
            [72, 187, 100, 130, 157, 111, 32, 75, 80],
            [66, 102, 167, 99, 74, 62, 40, 234, 128],
            [41, 53, 9, 178, 241, 141, 26, 8, 107],
            [104, 79, 12, 27, 217, 255, 87, 17, 7],
            [74, 43, 26, 146, 73, 166, 49, 23, 157],
            [65, 38, 105, 160, 51, 52, 31, 115, 128],
            [87, 68, 71, 44, 114, 51, 15, 186, 23],
            [47, 41, 14, 110, 182, 183, 21, 17, 194],
            [66, 45, 25, 102, 197, 189, 23, 18, 22]
        ],
        [
            [88, 88, 147, 150, 42, 46, 45, 196, 205],
            [43, 97, 183, 117, 85, 38, 35, 179, 61],
            [39, 53, 200, 87, 26, 21, 43, 232, 171],
            [56, 34, 51, 104, 114, 102, 29, 93, 77],
            [107, 54, 32, 26, 51, 1, 81, 43, 31],
            [39, 28, 85, 171, 58, 165, 90, 98, 64],
            [34, 22, 116, 206, 23, 34, 43, 166, 73],
            [68, 25, 106, 22, 64, 171, 36, 225, 114],
            [34, 19, 21, 102, 132, 188, 16, 76, 124],
            [62, 18, 78, 95, 85, 57, 50, 48, 51]
        ],
        [
            [193, 101, 35, 159, 215, 111, 89, 46, 111],
            [60, 148, 31, 172, 219, 228, 21, 18, 111],
            [112, 113, 77, 85, 179, 255, 38, 120, 114],
            [40, 42, 1, 196, 245, 209, 10, 25, 109],
            [100, 80, 8, 43, 154, 1, 51, 26, 71],
            [88, 43, 29, 140, 166, 213, 37, 43, 154],
            [61, 63, 30, 155, 67, 45, 68, 1, 209],
            [142, 78, 78, 16, 255, 128, 34, 197, 171],
            [41, 40, 5, 102, 211, 183, 4, 1, 221],
            [51, 50, 17, 168, 209, 192, 23, 25, 82]
        ],
        [
            [125, 98, 42, 88, 104, 85, 117, 175, 82],
            [95, 84, 53, 89, 128, 100, 113, 101, 45],
            [75, 79, 123, 47, 51, 128, 81, 171, 1],
            [57, 17, 5, 71, 102, 57, 53, 41, 49],
            [115, 21, 2, 10, 102, 255, 166, 23, 6],
            [38, 33, 13, 121, 57, 73, 26, 1, 85],
            [41, 10, 67, 138, 77, 110, 90, 47, 114],
            [101, 29, 16, 10, 85, 128, 101, 196, 26],
            [57, 18, 10, 102, 102, 213, 34, 20, 43],
            [117, 20, 15, 36, 163, 128, 68, 1, 26]
        ],
        [
            [138, 31, 36, 171, 27, 166, 38, 44, 229],
            [67, 87, 58, 169, 82, 115, 26, 59, 179],
            [63, 59, 90, 180, 59, 166, 93, 73, 154],
            [40, 40, 21, 116, 143, 209, 34, 39, 175],
            [57, 46, 22, 24, 128, 1, 54, 17, 37],
            [47, 15, 16, 183, 34, 223, 49, 45, 183],
            [46, 17, 33, 183, 6, 98, 15, 32, 183],
            [65, 32, 73, 115, 28, 128, 23, 128, 205],
            [40, 3, 9, 115, 51, 192, 18, 6, 223],
            [87, 37, 9, 115, 59, 77, 64, 21, 47]
        ],
        [
            [104, 55, 44, 218, 9, 54, 53, 130, 226],
            [64, 90, 70, 205, 40, 41, 23, 26, 57],
            [54, 57, 112, 184, 5, 41, 38, 166, 213],
            [30, 34, 26, 133, 152, 116, 10, 32, 134],
            [75, 32, 12, 51, 192, 255, 160, 43, 51],
            [39, 19, 53, 221, 26, 114, 32, 73, 255],
            [31, 9, 65, 234, 2, 15, 1, 118, 73],
            [88, 31, 35, 67, 102, 85, 55, 186, 85],
            [56, 21, 23, 111, 59, 205, 45, 37, 192],
            [55, 38, 70, 124, 73, 102, 1, 34, 98]
        ],
        [
            [102, 61, 71, 37, 34, 53, 31, 243, 192],
            [69, 60, 71, 38, 73, 119, 28, 222, 37],
            [68, 45, 128, 34, 1, 47, 11, 245, 171],
            [62, 17, 19, 70, 146, 85, 55, 62, 70],
            [75, 15, 9, 9, 64, 255, 184, 119, 16],
            [37, 43, 37, 154, 100, 163, 85, 160, 1],
            [63, 9, 92, 136, 28, 64, 32, 201, 85],
            [86, 6, 28, 5, 64, 255, 25, 248, 1],
            [56, 8, 17, 132, 137, 255, 55, 116, 128],
            [58, 15, 20, 82, 135, 57, 26, 121, 40]
        ],
        [
            [164, 50, 31, 137, 154, 133, 25, 35, 218],
            [51, 103, 44, 131, 131, 123, 31, 6, 158],
            [86, 40, 64, 135, 148, 224, 45, 183, 128],
            [22, 26, 17, 131, 240, 154, 14, 1, 209],
            [83, 12, 13, 54, 192, 255, 68, 47, 28],
            [45, 16, 21, 91, 64, 222, 7, 1, 197],
            [56, 21, 39, 155, 60, 138, 23, 102, 213],
            [85, 26, 85, 85, 128, 128, 32, 146, 171],
            [18, 11, 7, 63, 144, 171, 4, 4, 246],
            [35, 27, 10, 146, 174, 171, 12, 26, 128]
        ],
        [
            [190, 80, 35, 99, 180, 80, 126, 54, 45],
            [85, 126, 47, 87, 176, 51, 41, 20, 32],
            [101, 75, 128, 139, 118, 146, 116, 128, 85],
            [56, 41, 15, 176, 236, 85, 37, 9, 62],
            [146, 36, 19, 30, 171, 255, 97, 27, 20],
            [71, 30, 17, 119, 118, 255, 17, 18, 138],
            [101, 38, 60, 138, 55, 70, 43, 26, 142],
            [138, 45, 61, 62, 219, 1, 81, 188, 64],
            [32, 41, 20, 117, 151, 142, 20, 21, 163],
            [112, 19, 12, 61, 195, 128, 48, 4, 24]
        ]
]

kf_y_mode_tree = [
    -B_PRED, 2,
    4, 6,
    -DC_PRED, -V_PRED,
    -H_PRED, -TM_PRED
]

y_mode_tree = [
    -DC_PRED, 2,
    4, 6,
    -V_PRED, -H_PRED,
    -TM_PRED, -B_PRED
]

uv_mode_tree = [
    -DC_PRED, 2,
    -V_PRED, 4,
    -H_PRED, -TM_PRED
]

b_mode_tree = [
    -B_DC_PRED, 2,
    -B_TM_PRED, 4,
    -B_VE_PRED, 6,
    8, 12,
    -B_HE_PRED, 10,
    -B_RD_PRED, -B_VR_PRED,
    -B_LD_PRED, 14,
    -B_VL_PRED, 16,
    -B_HD_PRED, -B_HU_PRED
]
    
small_mv_tree = [
    2, 8,
    4, 6,
    -0, -1,
    -2, -3,
    10, 12,
    -4, -5,
    -6, -7
]

mv_ref_tree = [
    -ZEROMV, 2,
    -NEARESTMV, 4,
    -NEARMV, 6,
    -NEWMV, -SPLITMV
]

submv_ref_tree = [
    -LEFT4X4, 2,
    -ABOVE4X4, 4,
    -ZERO4X4, -NEW4X4
]

split_mv_tree = [
    -3, 2,
    -2, 4,
    -0, -1
]

default_b_mode_probs = [120, 90, 79, 133, 87, 85, 80, 111, 151]

mv_counts_to_probs = [
    [7, 1, 1, 143],
    [14, 18, 14, 107],
    [135, 64, 57, 68],
    [60, 56, 128, 65],
    [159, 134, 128, 34],
    [234, 188, 128, 28]
]

split_mv_probs = [110, 111, 150]

submv_ref_probs2 = [
    [147, 136, 18],
    [106, 145, 1],
    [179, 121, 1],
    [223, 1, 34],
    [208, 1, 1]
]

mv_partitions = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 3, 3],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
]


class mv_clamp_rect:
    def __init__(self):
        self.to_left = int_
        self.to_right = int_
        self.to_top = int_
        self.to_bottom = int_


VPX_IMG_FMT_I420 = 258
VPX_IMG_FMT_VPXI420 = 260

VPX_PLANE_PACKED = 0
VPX_PLANE_Y = 0
VPX_PLANE_U = 1
VPX_PLANE_V = 2
VPX_PLANE_ALPHA = 3
PLANE_PACKED = VPX_PLANE_PACKED
PLANE_Y = VPX_PLANE_Y
PLANE_U = VPX_PLANE_U
PLANE_V = VPX_PLANE_V
PLANE_ALPHA = VPX_PLANE_ALPHA

VPX_IMAGE_ABI_VERSION = 1

VPX_IMG_FMT_PLANAR = 0x100
VPX_IMG_FMT_UV_FLIP = 0x200
VPX_IMG_FMT_HAS_ALPHA = 0x400


VPX_IMG_FMT_NONE = 0
VPX_IMG_FMT_RGB24 = 1
VPX_IMG_FMT_RGB32 = 2
VPX_IMG_FMT_RGB565 = 3
VPX_IMG_FMT_RGB555 = 4
VPX_IMG_FMT_UYVY = 5
VPX_IMG_FMT_YUY2 = 6
VPX_IMG_FMT_YVYU = 7
VPX_IMG_FMT_BGR24 = 8
VPX_IMG_FMT_RGB32_LE = 9
VPX_IMG_FMT_ARGB = 10
VPX_IMG_FMT_ARGB_LE = 11
VPX_IMG_FMT_RGB565_LE = 12
VPX_IMG_FMT_RGB555_LE = 13
VPX_IMG_FMT_YV12 = VPX_IMG_FMT_PLANAR | VPX_IMG_FMT_UV_FLIP | 1
VPX_IMG_FMT_I420 = VPX_IMG_FMT_PLANAR | 2
VPX_IMG_FMT_VPXYV12 = VPX_IMG_FMT_PLANAR | VPX_IMG_FMT_UV_FLIP | 3
VPX_IMG_FMT_VPXI420 = VPX_IMG_FMT_PLANAR | 4

IMG_FMT_PLANAR = VPX_IMG_FMT_PLANAR
IMG_FMT_UV_FLIP = VPX_IMG_FMT_UV_FLIP
IMG_FMT_HAS_ALPHA = VPX_IMG_FMT_HAS_ALPHA

IMG_FMT_NONE = VPX_IMG_FMT_NONE
IMG_FMT_RGB24 = VPX_IMG_FMT_RGB24
IMG_FMT_RGB32 = VPX_IMG_FMT_RGB32
IMG_FMT_RGB565 = VPX_IMG_FMT_RGB565
IMG_FMT_RGB555 = VPX_IMG_FMT_RGB555
IMG_FMT_UYVY = VPX_IMG_FMT_UYVY
IMG_FMT_YUY2 = VPX_IMG_FMT_YUY2
IMG_FMT_YVYU = VPX_IMG_FMT_YVYU
IMG_FMT_BGR24 = VPX_IMG_FMT_BGR24
IMG_FMT_RGB32_LE = VPX_IMG_FMT_RGB32_LE
IMG_FMT_ARGB = VPX_IMG_FMT_ARGB
IMG_FMT_ARGB_LE = VPX_IMG_FMT_ARGB_LE
IMG_FMT_RGB565_LE = VPX_IMG_FMT_RGB565_LE
IMG_FMT_RGB555_LE = VPX_IMG_FMT_RGB555_LE
IMG_FMT_YV12 = VPX_IMG_FMT_YV12
IMG_FMT_I420 = VPX_IMG_FMT_I420
IMG_FMT_VPXYV12 = VPX_IMG_FMT_VPXYV12
IMG_FMT_VPXI420 = VPX_IMG_FMT_VPXI420


def clamp_q(q):
    if q < 0:
        return 0
    elif q > 127:
        return 127

    return q

def dc_q(q):
    return dc_q_lookup[clamp_q(q)]

def ac_q(q):
    return ac_q_lookup[clamp_q(q)]

def vpx_internal_error(err, code, more):
    print('Got error ' + err + ' with code ' + code + '\n' + more)

def BITS_MASK(n):
    return ((1 << (n)) - 1)

def BITS_GET(val, bit, len):
    return (((val) >> (bit)) & BITS_MASK(len))

def setjmp(jmp):
    return 0

def Arr(len, val):
    return [val] * len

def Arr_new(len, val):
    return [val()] * len

def ArrM(AOfLen, val):
    a = len(AOfLen) - 1
    
    while a >= 0:
        val = Arr(AOfLen[a], val)
        a -= 1
    return val

def ASSERT(bCondition):
    if not bCondition:
        raise AssertionError('assert :P')

def CHECK_FOR_UPDATE(lval, rval, update_flag):
    old = lval
    lval = rval
    update_flag[0] |= (old != lval)
    return lval

class ebml_element_desc:
    def __init__(self):
        self.name = char_
        self.id = uint64_t
        self.type = 0
        self.offset = size_t
        self.flags = int_
        self.children = None
        self.size = size_t
        self.data_offset = size_t

class list_node:
    def __init__(self):
        self.previous = 0
        self.node = ebml_element_desc()
        self.data = char_

class ebml_list_node:
    def __init__(self):
        self.next = None
        self.id = uint64_t
        self.data = void_

class vpx_image_t:
    def __init__(self):
        self.fmt = 0
        
        self.w = int_
        self.h = int_
        
        self.d_w = int_
        self.d_h = int_
        
        self.x_chroma_shift = int_
        self.y_chroma_shift = int_
        
        self.planes = [None] * 4
        self.planes_off = [None] * 4
        self.stride = [None] * 4
        
        self.bps = int_
        
        self.user_priv = void_
        
        self.img_data = char_
        self.img_data_off = 0
        self.img_data_owner = int_
        self.self_allocd = int_

class nestegg_io:
    def __init__(self):
        self.read = int_
        self.seek = int_
        self.tell = int64_t
        self.userdata = void_
        
class pool_ctx:
    def __init__(self):
        self.dummy = char_

class ebml_binary:
    def __init__(self):
        self.data = char_
        self.length = size_t

class ebml_type:
    def __init__(self):
        self.v = {
            "u": uint64_t,
            "f": double_,
            "i": int64_t,
            "s": char_,
            "b": ebml_binary()
        }
        self.type = 0
        self.read = int_
    
class ebml:
    def __init__(self):
        self.ebml_version = ebml_type()
        self.ebml_read_version = ebml_type()
        self.ebml_max_id_length = ebml_type()
        self.ebml_max_size_length = ebml_type()
        self.doctype = ebml_type()
        self.doctype_version = ebml_type()
        self.doctype_read_version = ebml_type()

class ebml_list:
    def __init__(self):
        self.head = None
        self.tail = None

class info:
    def __init__(self):
        self.timecode_scale = ebml_type()
        self.duration = ebml_type()

class tracks:
    def __init__(self):
        self.track_entry = ebml_list()

class cues:
    def __init__(self):
        self.cue_point = ebml_list()
    
class segment:
    def __init__(self):
        self.seek_head = ebml_list()
        self.info = info()
        self.cluster = ebml_list()
        self.tracks = tracks()
        self.cues = cues()
    
class nestegg:
    def __init__(self):
        self.io = nestegg_io()
        self.log_ = 0
        self.alloc_pool = pool_ctx()
        self.last_id = uint64_t
        self.last_size = uint64_t
        self.ancestor = None
        self.ebml = ebml()
        self.segment = segment()
        self.segment_offset = int64_t
        self.track_count = int_

class input_ctx:
    def __init__(self):
        self.kind = 0
        self.infile = 0
        self.nestegg_ctx = nestegg()
        self.pkt = [None]
        self.chunk = int_
        self.chunks = [int_]
        self.video_track = int_

class vp8_frame_hdr:
    def __init__(self):
        self.is_keyframe = int_
        self.is_experimental = int_
        self.version = int_
        self.is_shown = int_
        self.part0_sz = int_
        
        self.kf = {
            "w": int_,
            "h": int_,
            "scale_w": int_,
            "scale_h": int_
        }
        
        self.frame_size_updated = int_

class vp8_segment_hdr:
    def __init__(self):
        self.enabled = int_
        self.update_data = int_
        self.abs_ = int_
        self.tree_probs = [MB_FEATURE_TREE_PROBS]
        self.lf_level = [MAX_MB_SEGMENTS]
        self.quant_idx = [MAX_MB_SEGMENTS]

class vp8_loopfilter_hdr:
    def __init__(self):
        self.use_simple = int_
        self.level = int_
        self.sharpness = int_
        self.delta_enabled = int_
        self.ref_delta = [BLOCK_CONTEXTS]
        self.mode_delta = [BLOCK_CONTEXTS]

class vp8_token_hdr:
    def __init__(self):
        self.partitions = int_
        self.partition_sz = [MAX_PARTITIONS]

class vp8_quant_hdr:
    def __init__(self):
        self.q_index = int_
        self.delta_update = int_
        self.y1_dc_delta_q = int_
        self.y2_dc_delta_q = int_
        self.y2_ac_delta_q = int_
        self.uv_dc_delta_q = int_
        self.uv_ac_delta_q = int_

class vp8_reference_hdr:
    def __init__(self):
        self.refresh_last = int_
        self.refresh_gf = int_
        self.refresh_arf = int_
        self.copy_gf = int_
        self.copy_arf = int_
        self.sign_bias = [4]
        self.refresh_entropy = int_
        
def coeff_probs_table_t():
    return ArrM([
        BLOCK_TYPES, COEF_BANDS,
        PREV_COEF_CONTEXTS, ENTROPY_NODES
    ], char_)

def mv_component_probs_t():
    return [MV_PROB_CNT]

class vp8_entropy_hdr:
    def __init__(self):
        self.coeff_probs = coeff_probs_table_t()
        self.coeff_probs_ = Arr(1056, 0)
        self.mv_probs = Arr_new(2, mv_component_probs_t)
        self.coeff_skip_enabled = int_
        self.coeff_skip_prob = char_
        self.y_mode_probs = [0, 0, 0, 0]
        self.uv_mode_probs = [0, 0, 0]
        self.prob_inter = char_
        self.prob_last = char_
        self.prob_gf = char_

class mv:
    def __init__(self):
        self.d = {
            "x": int16_t,
            "y": int16_t
        }

class mb_base_info:
    def __init__(self):
        self.y_mode = char_
        self.uv_mode = char_
        self.segment_id = char_
        self.ref_frame = char_
        self.skip_coeff = char_
        self.need_mc_border = char_
        self.partitioning = None
        self.mv = mv()
        self.eob_mask = int_

class mb_info:
    def __init__(self):
        self.base = mb_base_info()
        self.splitt = {
            "mvs": Arr_new(16, mv),
            "modes": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }

def token_entropy_ctx_t():
    return [4 + 2 + 2 + 1]

def filter_t():
    return [None] * 6

class bool_decoder:
    def __init__(self):
        self.input = char_
        self.input_off = 0
        self.input_len = size_t
        self.range = int_
        self.value = int_
        self.bit_count = int_

class token_decoder:
    def __init__(self):
        self.bool = bool_decoder()
        self.left_token_entropy_ctx = token_entropy_ctx_t()
        self.coeffs = short_

class dequant_factors:
    def __init__(self):
        self.quant_idx = int_
        self.factor = ArrM([TOKEN_BLOCK_TYPES, 2], short_)

class ref_cnt_img:
    def __init__(self):
        self.img = vpx_image_t()
        self.ref_cnt = int_

class vp8_decoder_ctx:
    def __init__(self):
        self.error = []
        self.frame_cnt = int_
        
        self.frame_hdr = vp8_frame_hdr()
        self.segment_hdr = vp8_segment_hdr()
        self.loopfilter_hdr = vp8_loopfilter_hdr()
        self.token_hdr = vp8_token_hdr()
        self.quant_hdr = vp8_quant_hdr()
        self.reference_hdr = vp8_reference_hdr()
        self.entropy_hdr = vp8_entropy_hdr()

        self.saved_entropy = vp8_entropy_hdr()
        self.saved_entropy_valid = int_

        self.mb_rows = int_
        self.mb_cols = int_
        self.mb_info_storage = None
        self.mb_info_storage_off = 0
        self.mb_info_storage_object = mb_info

        self.mb_info_rows_storage = None
        self.mb_info_rows_storage_off = 0
        self.mb_info_rows_storage_object = mb_info
        self.mb_info_rows = None
        self.mb_info_rows_off = 0

        self.above_token_entropy_ctx = None
        self.above_token_entropy_ctx_object = token_entropy_ctx_t
        self.tokens = Arr_new(MAX_PARTITIONS, token_decoder)
        self.dequant_factors = Arr_new(MAX_MB_SEGMENTS, dequant_factors)

        self.frame_strg = Arr_new(NUM_REF_FRAMES, ref_cnt_img)
        self.ref_frames = Arr_new(NUM_REF_FRAMES, ref_cnt_img)
        self.ref_frame_offsets = [0, 0, 0, 0]
        self.ref_frame_offsets_ = [0, 0, 0, 0]

        self.subpixel_filters = filter_t()

class frame:
    def __init__(self):
        self.data = char_
        self.length = size_t
        self.next = None

class nestegg_packet:
    def __init__(self):
        self.track = uint64_t
        self.timecode = uint64_t
        self.frame = frame()

def nestegg_free_packet(pkt):
    frame = None
    
    while pkt.frame:
        frame = pkt.frame
        pkt.frame = frame.next
        frame.data = ''
        frame = ''
    
    pkt = ''

def ne_io_read(io, buffer, length):
    r = io.read(buffer, length, io.userdata)
    return r

def ne_bare_read_vint(io, value, length, maskflag):
    r = int_
    b = { "val": char_ }
    maxlen = 8
    count = 1
    mask = 1 << 7
    
    r = ne_io_read(io, b, 1)
    if r != 1:
        return r
    
    while count < maxlen:
        if (b.val[0] & mask) != 0:
            break
        mask >>= 1
        count += 1
    
    if length:
        length.val = count
        
    value.val = b.val[0]
        
    if maskflag == MASK_FIRST_BIT:
        value.val = b.val[0] & ~mask
    
    while count > 0:
        count -= 1
        r = ne_io_read(io, b, 1)
        if r != 1:
            return r
        value.val <<= 8
        value.val |= b.val[0]

    return 1
    
def ne_read_id(io, value, length):
    return ne_bare_read_vint(io, value, length, MASK_NONE)

def ne_read_vint(io, value, length):
    return ne_bare_read_vint(io, value, length, MASK_FIRST_BIT)

def ne_is_suspend_element(id):
    if id == ID_SIMPLE_BLOCK or id == ID_BLOCK:
        return 1
    return 0

def ne_read_element(ctx, id, size):
    r = int_
    
    r = ne_peek_element(ctx, id, size)
    if r != 1:
        return r
    
    ctx.last_id = 0
    ctx.last_size = 0
    
    return 1

def ne_peek_element(ctx, id, size):
    r = int_
    
    if ctx.late_id and ctx.last_size:
        if id:
            id[0] = ctx.last_id
        if size:
            size[0] = ctx.last_size
        return 1

    ctx.last_id = { "val": ctx.last_id }
    r = ne_read_id(ctx.io, ctx.last_id, None)
    ctx.last_id = ctx.last_id.val
    if r != 1:
        return r
    
    ctx.last_size = { "val": ctx.last_size }
    r = ne_read_vint(ctx.io, ctx.last_size, None)
    ctx.last_size = ctx.last_size.val
    if r != 1:
        return r
    
    if id:
        id[0] = ctx.last_id
    if size:
        size[0] = ctx.last_size
        
    return 1

def ne_read_uint(io, val, length):
    b = { "val": char_ }
    r = int_
    
    if length == 0 or length > 8:
        return -1
    r = ne_io_read(io, b, 1)
    if r != 1:
        return r
    val[0] = b.val[0]
    while length > 0:
        length -= 1
        r = ne_io_read(io, b, 1)
        if r != 1:
            return r
        val[0] <<= 8
        val[0] |= b.val[0]

    return 1

def ne_read_float(io, val, length):
    value = {
        "u": [uint64_t],
        "f": [float_],
        "d": [double_]
    }
    r = int_
    
    if length != 4 and length != 8:
        return -1
    r = ne_read_uint(io, value.u, length)
    if r != 1:
        return r
    if length == 4:
        val[0] = value.f = value.u
    else:
        val[0] = value.d = value.u
    return 1

def ne_read_string(ctx, val, length):
    str = { "val": char_ }
    r = int_
    
    if length == 0 or length > LIMIT_STRING:
        return -1
    
    r = ne_io_read(ctx.io, str, length)
    if r != 1:
        return r
    str2 = ''
    for i in range(length):
        str2 += chr(str.val[i])
    str.val = str2
    val[0] = str.val
    return 1

def ne_read_binary(ctx, val, length):
    if length == 0 or length > LIMIT_BINARY:
        return -1
    val.data = { "val": 0 }
    val.length = length
    return ne_io_read(ctx.io, val.data, length)
    

def ne_read_xiph_lace_value(io, value, value_off, consumed):
    r = int_
    lace = [uint64_t]
    
    r = ne_read_uint(io, lace, 1)
    if r != 1:
        return r
    consumed[0] += 1
    
    value[value_off] = lace[0]
    while lace[0] == 255:
        r = ne_read_uint(io, lace, 1)
        if r != 1:
            return r
        consumed[0] += 1
        value[value_off] += lace[0]
        
    return 1

def ne_read_xiph_lacing(io, block, read, n, sizes):
    r = int_
    i = 0
    sum = 0
    
    while n > 0:
        n -= 1
        r = ne_read_xiph_lace_value(io, sizes, i, read)
        if r != 1:
            return r
        sum += sizes[i]
        i += 1
        
    if read[0] + sum > block:
        return -1
    
    sizes[i] = block - read[0] - sum
    return 1

def ne_read_svint(io, value, length):
    r = int_
    uvalue = [uint64_t]
    ulength = [uint64_t]
    svint_subtr = [
        0x3f, 0x1fff,
        0xfffff, 0x7ffffff,
        0x3ffffffff, 0x1ffffffffff,
        0xffffffffffff, 0x7fffffffffffff
    ]
    
    r = ne_bare_read_vint(io, uvalue, ulength, MASK_FIRST_BIT)
    if r != 1:
        return r
    value[0] = uvalue - svint_subtr[ulength - 1]
    if length:
        length[0] = ulength
    return r

def ne_read_ebml_lacing(io, block, read, n, sizes):
    r = int_
    lace = [uint64_t]
    sum = uint64_t
    length = [uint64_t]
    slace = [int64_t]
    i = 0
    
    r = ne_read_vint(io, lace, length)
    if r != 1:
        return r
    read[0] += length[0]
    
    sizes[i] = lace[0]
    sum = sizes[i]
    
    i += 1
    n -= 1
    
    while n > 0:
        n -= 1
        
        r = ne_read_svint(io, slace, length)
        if r != 1:
            return r
        read[0] += length[0]
        sizes[i] = sizes[i - 1] + slace[0]
        sum += sizes[i]
        i += 1
    
    if read[0] + sum > block:
        return -1
    
    sizes[i] = block - read[0] - sum
    return 1

def ne_find_track_entry(ctx, track):
    tracks = 0
    
    node = ctx.segment.tracks.track_entry.head
    while node:
        ASSERT(node.id == ID_TRACK_ENTRY)
        if track == tracks:
            return node.data
        tracks += 1
        node = node.next
    
    return None

def ne_get_uint(type, value):
    if not type.read:
        return -1
    
    ASSERT(type.type == TYPE_UINT)
    
    value[0] = type.v.u
    
    return 0

def ne_get_timecode_scale(ctx):
    scale = [uint64_t]
    
    if ne_get_uint(ctx.segment.info.timecode_scale, scale) != 0:
        scale[0] = 1000000
        
    return scale[0]

frame_sizes_256 = Arr(256, 0)
def ne_read_block(ctx, block_id, block_size, data):
    r = int_
    timecode, abs_timecode = [int64_t], int64_t
    pkt = None
    cluster = None
    f, last = None, None
    entry = None
    track_scale = double_
    track = { "val": uint64_t }
    length = { "val": uint64_t }
    frame_sizes = frame_sizes_256
    cluster_tc, flags, frames = [uint64_t], [uint64_t], [uint64_t]
    tc_scale, total = uint64_t, uint64_t
    i, lacing = int_, int_
    consumed = [0]
    
    data[0] = None
    
    if block_size > LIMIT_BLOCK:
        return -1
    
    r = ne_read_vint(ctx.io, track, length)
    if r != 1:
        return r
    
    if track.val == 0 or track.val > ctx.track_count:
        return -1
    
    consumed[0] += length.val
    
    r = ne_read_int(ctx.io, timecode, 2)
    if (r != 1):
        return r
    
    consumed[0] += 2
    
    r = ne_read_uint(ctx.io, flags, 1)
    if r != 1:
        return r
    
    consumed[0] += 1
    
    frames[0] = 0
    
    lacing = (flags[0] & BLOCK_FLAGS_LACING) >> 1

    if lacing == LACING_NONE:
        frames[0] = 1
    elif lacing in [LACING_XIPH, LACING_FIXED, LACING_EBML]:
        r = ne_read_uint(ctx.io, frames, 1)
        if r != 1:
            return r
        consumed[0] += 1
        frames[0] += 1
        
    if frames[0] > 256:
        return -1
    
    if lacing == LACING_NONE:
        frame_sizes[0] = block_size - consumed[0]
    elif lacing == LACING_XIPH:
        if frames == 1:
            return -1
        r = ne_read_xiph_lacing(ctx.io, block_size, consumed, frames, frame_sizes)
        if r != 1:
            return r
    elif lacing == LACING_FIXED:
        if (block_size - consumed[0]) % frames[0]:
            return -1
        for i in range(frames[0]):
            frame_sizes[i] = int((block_size - consumed[0]) / frames[0])
    elif lacing == LACING_EBML:
        if frames[0] == 1:
            return -1
        r = ne_read_ebml_lacing(ctx.io, block_size, consumed, frames, frame_sizes)
        if r != 1:
            return r
        
    total = consumed[0]
    for i in range(frames[0]):
        total += frame_sizes[i]
    if total > block_size:
        return -1
    
    entry = ne_find_track_entry(ctx, track.val - 1)
    if not entry:
        return -1
    
    track_scale = 1.0
    
    tc_scale = ne_get_timecode_scale(ctx)
    
    ASSERT(ctx.segment.cluster.tail.id == ID_CLUSTER)
    cluster = ctx.segment.cluster.tail.data
    if ne_get_uint(cluster.timecode, cluster_tc) != 0:
        return -1
    
    abs_timecode = timecode[0] + cluster_tc[0]
    if abs_timecode < 0:
        return -1
    
    pkt = nestegg_packet()
    pkt.track = track.val - 1
    pkt.timecode = abs_timecode * tc_scale * track_scale
    
    last = None
    for i in range(frames[0]):
        if frame_sizes[i] > LIMIT_FRAME:
            nestegg_free_packet(pkt)
            return -1
        
        f = frame()
        f.data = []
        f.length = frame_sizes[i]
        f.data = { "val": f.data }
        r = ne_io_read(ctx.io, f.data, frame_sizes[i])
        f.data = f.data.val
        if r != 1:
            f.data = None
            f = None
            nestegg_free_packet(pkt)
            return -1
        
        if not last:
            pkt.frame = f
        else:
            last.next = f
        last = f
        
    data[0] = pkt
    
    return 1

def ne_find_element(id, elements):
    element_pos = 0
    while elements[element_pos].id:
        if elements[element_pos].id == id:
            return elements[element_pos]
        element_pos += 1
    
    return None

def ne_io_tell(io):
    return io.tell(io.userdata)

def ne_ctx_push(ctx, ancestor, data):
    item_ = list_node()
    
    item_.previous = ctx.ancestor
    item_.node = ancestor
    item_.data = data
    ctx.ancestor = item_

def ne_read_master(ctx, desc):
    list, oldtail = None, None
    node = ebml_list_node()
    
    ASSERT(desc.type == TYPE_MASTER and desc.flags & DESC_FLAG_MULTI)
    
    if ctx.ancestor.data[desc.offset]:
        list = ctx.ancestor.data[desc.offset]
    
    node.id = desc.id
    node.data = globals()[desc.offset]()
    
    oldtail = list.tail
    if oldtail:
        oldtail.next = node
    list.tail = node
    if not list.head:
        list.head = node
    
    ne_ctx_push(ctx, desc.children, node.data)
    
def ne_read_single_master(ctx, desc):
    ASSERT(desc.type == TYPE_MASTER and not (desc.flags & DESC_FLAG_MULTI))
    
    ne_ctx_push(ctx, desc.children, ctx.ancestor.data[desc.offset])

def ne_read_simple(ctx, desc, length):
    storage = None
    r = int_
    
    if ctx.ancestor.data[desc.offset]:
        storage = ctx.ancestor.data[desc.offset]
    
    if storage.read:
        return 0
    
    storage.type = desc.type
    
    r = -1
    
    if desc.type == TYPE_UINT:
        storage.v.u = [storage.v.u]
        r = ne_read_uint(ctx.io, storage.v.u, length)
        storage.v.u = storage.v.u[0]
    elif desc.type == TYPE_FLOAT:
        storage.v.f = [storage.v.f]
        r = ne_read_float(ctx.io, storage.v.f, length)
        storage.v.f = storage.v.f[0]
    elif desc.type == TYPE_INT:
        storage.v.i = [storage.v.i]
        r = ne_read_int(ctx.io, storage.v.i, length)
        storage.v.i = storage.v.i[0]
    elif desc.type == TYPE_STRING:
        storage.v.s = [storage.v.s]
        r = ne_read_string(ctx.io, storage.v.s, length)
        storage.v.s = storage.v.s[0]
    elif desc.type == TYPE_BINARY:
        r = ne_read_binary(ctx, storage.v.b, length)
    elif desc.type == TYPE_MASTER or desc.type == TYPE_UNKNOWN:
        ASSERT(0)
    
    if r == 1:
        storage.read = 1
    
    return r

def ne_is_ancestor_element(id, ancestor):
    while ancestor:
        element_pos = 0
        while ancestor.node[element_pos].id:
            if ancestor.node[element_pos].id == id:
                return 1
            element_pos += 1
        ancestor = ancestor.previous

    return 0

def ne_ctx_pop(ctx):
    item_ = ctx.ancestor
    ctx.ancestor = item_.previous
    item_ = ''
    
buffer_8192 = Arr(8192, 0)
def ne_io_read_skip(io, length):
    get_ = size_t
    buf = { "val": buffer_8192 }
    r = 1
    
    while length > 0:
        get_ = length if length < buf.val.length else buf.val.length
        r = ne_io_read(io, buf, get_)
        if r != 1:
            break
        length -= get_
    
    return r

def ne_parse(ctx, top_level):
    r = int_
    data_offset = int64_t
    id, size = [uint64_t], [uint64_t]
    element = None
    
    if not ctx.ancestor:
        return -1
    
    while 1:
        r = ne_peek_element(ctx, id, size)
        if r != 1:
            break
        
        element = ne_find_element(id[0], ctx.ancestor.node)
        if element:
            if element.flags & DESC_FLAG_SUSPEND:
                ASSERT(element.type == TYPE_BINARY)
                r = 1
                break
            
            r = ne_read_element(ctx, id, size)
            if r != 1:
                break
            
            if element.flags & DESC_FLAG_OFFSET:
                data_offset = ctx.ancestor.data[element.data_offset] = { "v": None }
                data_offset.v = ne_io_tell(ctx.io)
                if data_offset < 0:
                    r = -1
                    break
            
            if element.type == TYPE_MASTER:
                if element.flags & DESC_FLAG_MULTI:
                    ne_read_master(ctx, element)
                else:
                    ne_read_single_master(ctx, element)
                continue
            else:
                r = ne_read_simple(ctx, element, size[0])
                if r < 0:
                    break
                
        elif ne_is_ancestor_element(id, ctx.ancestor.previous):
            if top_level and ctx.ancestor.node == top_level:
                r = 1
                break
            ne_ctx_pop(ctx)
        else:
            r = ne_read_element(ctx, id, size)
            if r != 1:
                break
            
            r = ne_io_read_skip(ctx.io, size[0])
            if r != 1:
                break
    
    if r != 1:
        while ctx.ancestor:
            ne_ctx_pop(ctx)
    
    return r
            
    
def nestegg_read_packet(ctx, pkt):
    r = int_
    id, size = [uint64_t], [uint64_t]
    
    pkt[0] = None
    
    while 1:
        r = ne_peek_element(ctx, id, size)
        if r != 1:
            return r

        if ne_is_suspend_element(id):
            r = ne_read_element(ctx, id, size)
            if r != 1:
                return r
            
            r = ne_read_block(ctx, id, size[0], pkt)
            return r

        r = ne_parse(ctx, None)
        if (r != 1):
            return r
    
    return 1

def ne_read_int(io, val, length):
    r = int_
    uval, base = [uint64_t], uint64_t
    
    r = ne_read_uint(io, uval, length)
    if r != 1:
        return r
    
    if length < 8:
        base = 1
        base <<= length * 8 - 1
        if uval >= base:
            base = 1
            base <<= length * 8
        else:
            base = 0
        val[0] = uval - base
    else:
        val[0] = uval
    
    return 1

def nestegg_packet_track(pkt, track):
    track[0] = pkt[0].track
    return 0

def nestegg_packet_count(pkt, count):
    f = pkt[0].frame
    
    count[0] = 0
    
    while f:
        count[0] += 1
        f = f.next
    
    return 0

def buffer8k():
    return Arr(8800, 0)

def fread(ptr, size, count, stream):
    ptr.val = buffer8k()
    
    if stream.data.length < count + stream.data_off:
        stream.data_off += count
        return 0
    for i in range(count):
        stream.data_off += 1
        ptr.val[i] = stream.data[stream.data_off]
    ptr.val.length = count
    return i

def nestegg_packet_data(pkt, item_, data, length):
    f = pkt[0].frame
    count = 0
    
    data[0] = None
    length[0] = 0
    
    while f:
        if count == item_:
            data[0] = f.data
            length[0] = f.length
            return 0
        count += 1
        f = f.next
    
    return -1

def read_frame(input, buf, buf_off, buf_sz, buf_alloc_sz):
    new_buf_sz = size_t
    infile = input.infile
    kind = input.kind
    if kind == WEBM_FILE:
        if input.chunk >= input.chunks:
            track = [int_]
            
            while True:
                # End of this packet, get another.
                if input.pkt:
                    nestegg_free_packet(input.pkt)
                
                if nestegg_read_packet(input.nestegg_ctx, input.pkt) <= 0 or nestegg_packet_track(input.pkt, track):
                    return 1
                
                if track == input.video_track:
                    break
            
            if nestegg_packet_count(input.pkt, input.chunks):
                return 1
            input.chunk = 0
        
        if nestegg_packet_data(input.pkt, input.chunk, buf, buf_sz):
            return 1
        
        input.chunk += 1
        
        return 0
    
    buf_sz[0] = new_buf_sz
    
    if buf_sz:
        if fread(buf, 1, buf_sz[0], infile) != buf_sz[0]:
            print('Failed to read full frame')
            return 1
        return 0
    return 1

def vp8_parse_frame_header(data, sz, hdr):
    raw = long_
    
    if sz < 10:
        return VPX_CODEC_CORRUPT_FRAME
    
    raw = data[0] | (data[1] << 8) | (data[2] << 16)
    hdr.is_keyframe = not BITS_GET(raw, 0, 1)
    hdr.version = BITS_GET(raw, 1, 2)
    hdr.is_experimental = BITS_GET(raw, 3, 1)
    hdr.is_shown = BITS_GET(raw, 4, 1)
    hdr.part0_sz = BITS_GET(raw, 5, 19)
    
    if sz <= hdr.part0_sz + (10 if hdr.is_keyframe else 3):
        return VPX_CODEC_CORRUPT_FRAME

    hdr.frame_size_updated = 0
    
    if hdr.is_keyframe:
        update = [0]
        
        if data[3] != 0x9d or data[4] != 0x01 or data[5] != 0x2a:
            return VPX_CODEC_UNSUP_BITSTREAM
        
        raw = data[6] | (data[7] << 8) | (data[8] << 16) | (data[9] << 24)
        hdr.kf.w = CHECK_FOR_UPDATE(hdr.kf.w, BITS_GET(raw, 0, 14), update)
        hdr.kf.scale_w = CHECK_FOR_UPDATE(hdr.kf.scale_w, BITS_GET(raw, 14, 2), update)
        hdr.kf.h = CHECK_FOR_UPDATE(hdr.kf.h, BITS_GET(raw, 16, 14), update)
        hdr.kf.scale_h = CHECK_FOR_UPDATE(hdr.kf.scale_h, BITS_GET(raw, 30, 2), update)

        hdr.frame_size_updated = update[0]

        if not hdr.kf.w or not hdr.kf.h:
            return VPX_CODEC_UNSUP_BITSTREAM

def init_bool_decoder(d, start_partition, start_partition_off, sz):
    if sz >= 2:
        d.value = (start_partition[start_partition_off] << 8) | start_partition[start_partition_off + 1]
        d.input = start_partition
        d.input_off = start_partition_off + 2
        d.input_len = sz - 2
    else:
        d.value = 0
        d.input = None
        d.input_len = 0
    
    d.range = 255
    d.bit_count = 0
    
def bool_get(d, probability):
    splitt = 1 + (((d.range - 1) * probability) >> 8)
    SPLIT = splitt << 8
    retval = int_
    
    if d.value >= SPLIT:
        retval = 1
        d.range -= splitt
        d.value -= SPLIT
    else:
        retval = 0
        d.range = splitt
    
    while d.range < 128:
        d.value <<= 1
        d.range <<= 1
        
        d.bit_count += 1
        if d.bit_count == 8:
            d.bit_count = 0
            
            if (d.input_len):
                d.input_off += 1
                d.value |= d.input[d.input_off]
                d.input_len -= 1
    
    return retval

def bool_get_bit(br):
    return bool_get(br, 128)
    
def bool_get_uint(br, bits):
    z, bit = 0, int_
    
    bit = bits - 1
    while bit >= 0:
        z |= bool_get_bit(br) << bit
        bit -= 1
    
    return z

def memset(ptr, ptr_off, value, num):
    for i in range(num):
        ptr[ptr_off + i] = value

def bool_get_int(br):
    return bool_get(br, 128)

def bool_maybe_get_int(br, bits):
    return bool_get_int(br, bits) if bool_get_bit(br) else 0

def decode_segmentation_header(ctx, bool, hdr):
    if ctx.frame_hdr.is_keyframe:
        memset(hdr, 0, 1)
    
    hdr.enabled = bool_get_bit(bool)
    
    if hdr.enabled:
        i = int_
        
        hdr.update_map = bool_get_bit(bool)
        hdr.update_data = bool_get_bit(bool)

        if hdr.update_data:
            hdr.abs_ = bool_get_bit(bool)
            
            for i in range(MAX_MB_SEGMENTS):
                hdr.quant_idx[i] = bool_maybe_get_int(bool, 7)
            
            for i in range(MAX_MB_SEGMENTS):
                hdr.lf_level[i] = bool_maybe_get_int(bool, 6)
        
        if hdr.update_map:
            for i in range(MB_FEATURE_TREE_PROBS):
                hdr.tree_probs[i] = bool_get_uint(bool, 8) if bool_get_bit(bool) else 255
    
    else:
        hdr.update_map = 0
        hdr.update_data = 0
        
def decode_loopfilter_header(ctx, bool, hdr):
    if ctx.frame_hdr.is_keyframe:
        memset(hdr, 0, 1)
    
    hdr.use_simple = bool_get_bit(bool)
    hdr.level = bool_get_uint(bool, 6)
    hdr.sharpness = bool_get_uint(bool, 3)
    hdr.delta_enabled = bool_get_bit(bool)

    if hdr.delta_enabled and bool_get_bit(bool):
        for i in range(BLOCK_CONTEXTS):
            hdr.ref_delta[i] = bool_maybe_get_int(bool, 6)

        for i in range(BLOCK_CONTEXTS):
            hdr.mode_delta[i] = bool_maybe_get_int(bool, 6)

def decode_and_init_token_partitions(ctx, bool, data, data_off, sz, hdr):
    i = int_
    
    hdr.partitions = 1 << bool_get_uint(bool, 2)
    
    if sz < 3 * (hdr.partitions - 1):
        vpx_internal_error(ctx.error, VPX_CODEC_CORRUPT_FRAME, "Truncated packet found parsing partition" +
            " lengths.")
    
    sz -= 3 * (hdr.partitions - 1)
    
    for i in range(hdr.partitions):
        if i < hdr.partitions - 1:
            hdr.partition_sz[i] = (data[data_off + 2] << 16) | (data[data_off + 1] << 8) | data[data_off]
            data_off += 3
        else:
            hdr.partition_sz[i] = sz
        
        if sz < hdr.partition_sz[i]:
            vpx_internal_error(ctx.error, VPX_CODEC_CORRUPT_FRAME, "Truncated partition " + str(i))
        
        sz -= hdr.partition_sz[i]
    
    for i in range(ctx.token_hdr.partitions):
        init_bool_decoder(ctx.tokens[i].bool, data, data_off, ctx.token_hdr.partition_sz[i])
        data_off += ctx.token_hdr.partition_sz[i]

def decode_quantizer_header(ctx, bool, hdr):
    update = int_
    last_q = hdr.q_index
    
    hdr.q_index = bool_get_uint(bool, 7)
    update = (last_q != hdr.q_index) + 0
    hdr.y1_dc_delta_q = bool_maybe_get_int(bool, 4)
    update |= hdr.y1_dc_delta_q
    hdr.y2_dc_delta_q = bool_maybe_get_int(bool, 4)
    update |= hdr.y2_dc_delta_q
    hdr.y2_ac_delta_q = bool_maybe_get_int(bool, 4)
    update |= hdr.y2_ac_delta_q
    hdr.uv_dc_delta_q = bool_maybe_get_int(bool, 4)
    update |= hdr.uv_dc_delta_q
    hdr.uv_ac_delta_q = bool_maybe_get_int(bool, 4)
    update |= hdr.uv_ac_delta_q
    
    hdr.delta_update = update

def decode_reference_header(ctx, bool, hdr):
    key = ctx.frame_hdr.is_keyframe
    
    hdr.refresh_gf = 1 if key else bool_get_bit(bool)
    hdr.refresh_arf = 1 if key else bool_get_bit(bool)
    hdr.copy_gf = 0 if key else (bool_get_uint(bool, 2) if not hdr.refresh_gf else 0)
    hdr.copy_arf = 0 if key else (bool_get_uint(bool, 2) if not hdr.refresh_arf else 0)
    hdr.sign_bias[GOLDEN_FRAME] = 0 if key else bool_get_bit(bool)
    hdr.sign_bias[ALTREF_FRAME] = 0 if key else bool_get_bit(bool)
    hdr.refresh_entropy = bool_get_bit(bool)
    hdr.refresh_last = 1 if key else bool_get_bit(bool)

def memcpy(dst, dst_off, src, src_off, num):
    for i in range(num):
        dst[dst_off + i] = src[src_off + i]
    return dst

def ARRAY_COPY(a, b):
    ASSERT(len(a) == len(b))
    memcpy(a, 0, b, 0, len(a))

def decode_entropy_header(ctx, bool, hdr):
    ii = 0
    
    for i in range(BLOCK_TYPES):
        for j in range (COEF_BANDS):
            for k in range(PREV_COEF_CONTEXTS):
                for l in range(ENTROPY_NODES):
                    if bool_get(bool, k_coeff_entropy_update_probs[i][j][k][l]):
                        hdr.coeff_probs_[ii] = hdr.coeff_probs[i][j][k][l] = bool_get_uint(bool, 8)
                    ii += 1
    
    hdr.coeff_skip_enabled = bool_get_bit(bool)
    
    if hdr.coeff_skip_enabled:
        hdr.coeff_skip_prob = bool_get_uint(bool, 8)
    
    if not ctx.frame_hdr.is_keyframe:
        hdr.prob_inter = bool_get_uint(bool, 8)
        hdr.prob_last = bool_get_uint(bool, 8)
        hdr.prob_gf = bool_get_uint(bool, 8)
        
        if bool_get_bit(bool):
            for i in range(4):
                hdr.y_mode_probs[i] = bool_get_uint(bool, 8)
        
        if bool_get_bit(bool):
            for i in range(3):
                hdr.uv_mode_probs[i] = bool_get_uint(bool, 8)
        
        for i in range(2):
            for j in range(MV_PROB_CNT):
                if bool_get(bool, k_mv_entropy_update_probs[i][j]):
                    x = bool_get_uint(bool, 7)
                    hdr.mv_probs[i][j] = x << 1 if x else 1

def vp8_dixie_modemv_init(ctx):
    mbi_w, mbi_h, i = int_, int_, int_
    mbi = mb_info()
    mbi_off = 0
    
    mbi_w = ctx.mb_cols + 1
    mbi_h = ctx.mb_rows + 1
    
    if ctx.frame_hdr.frame_size_updated:
        ctx.mb_info_storage = None
        ctx.mb_info_rows_storage = None
    
    if not ctx.mb_info_storage:
        ctx.mb_info_storage = Arr_new(mbi_w * mbi_h, ctx.mb_info_storage_object)
        
        ctx.mb_info_storage_off = 0
    
    if not ctx.mb_info_rows_storage:
        ctx.mb_info_rows_storage = Arr_new(mbi_h, ctx.mb_info_rows_storage_object)
        
        ctx.mb_info_rows_storage_off = [mbi_h]
    
    mbi = ctx.mb_info_storage
    mbi_off = ctx.mb_info_storage_off + 1
    
    for i in range(mbi_h):
        ctx.mb_info_rows_storage[i] = mbi
        ctx.mb_info_rows_storage_off[i] = mbi_off
        mbi_off += mbi_w
    
    ctx.mb_info_rows = ctx.mb_info_rows_storage
    ctx.mb_info_rows_off = ctx.mb_info_rows_storage_off

def vp8_dixie_tokens_init(ctx):
    partitions = ctx.token_hdr.partitions
    
    if ctx.frame_hdr.frame_size_updated:
        i = int_
        coeff_row_sz = ctx.mb_cols * 25 * 16
        
        for i in range(partitions):
            ctx.tokens[i].coeffs = [coeff_row_sz]

            if not ctx.tokens[i].coeffs:
                vpx_internal_error(ctx.error, VPX_CODEC_MEM_ERROR, None)
        
        ctx.above_token_entropy_ctx = Arr_new(ctx.mb_cols, ctx.above_token_entropy_ctx_object)

        if not ctx.above_token_entropy_ctx:
            vpx_internal_error(ctx.error, VPX_CODEC_MEM_ERROR, None)

def vpx_img_free(img):
    if img:
        if img.img_data and img.img_data_owner:
            img.img_data = ''

        if img.self_allocd:
            img = ''

def malloc(size, value):
    output = [value] * size
    return output

def vpx_img_set_rect(img, x, y, w, h):
    data = char_
    data_off = 0
    
    if x + w <= img.w and y + h <= img.h:
        img.d_w = img["d_w"] = w
        img.d_h = img["d_h"] = h
        
        if not (img.fmt & VPX_IMG_FMT_PLANAR):
            img.planes[VPX_PLANE_PACKED] = img.img_data; img.img_data_of + int(x * img.bps / 8 + y * img.stride[VPX_PLANE_PACKED])
        else:
            data = img.img_data
            data_off = img.img_data_off
            
            if img.fmt & VPX_IMG_FMT_HAS_ALPHA:
                img.planes[VPX_PLANE_ALPHA] = data
                img.planes_off[VPX_PLANE_ALPHA] = data_off + x + y * img.stride[VPX_PLANE_ALPHA]
                data_off += img.h * img.stride[VPX_PLANE_ALPHA]
            
            img.planes[VPX_PLANE_Y] = data
            img.planes_off[VPX_PLANE_Y] = data_off + x + y * img.stride[VPX_PLANE_Y]
            data_off += img.h * img.stride[VPX_PLANE_Y]
            
            if not (img.fmt & VPX_IMG_FMT_UV_FLIP):
                img.planes[VPX_PLANE_U] = data
                img.planes_off[VPX_PLANE_U] = data_off + (x >> img.x_chroma_shift) + (y >> img.y_chroma_shift) * img.stride[VPX_PLANE_U]
                data_off += (img.h >> img.y_chroma_shift) * img.stride[VPX_PLANE_U]
                img.planes[VPX_PLANE_V] = data
                img.planes_off[VPX_PLANE_V] = data_off + (x >> img.x_chroma_shift) + (y >> img.y_chroma_shift) * img.stride[VPX_PLANE_V]
            else:
                img.planes[VPX_PLANE_V] = data
                img.planes_off[VPX_PLANE_V] = data_off + (x >> img.x_chroma_shift) + (y >> img.y_chroma_shift) * img.stride[VPX_PLANE_V]
                data_off += (img.h >> img.y_chroma_shift) * img.stride[VPX_PLANE_V]
                img.planes[VPX_PLANE_U] = data
                img.planes_off[VPX_PLANE_U] = data_off + (x >> img.x_chroma_shift) + (y >> img.y_chroma_shift) * img.stride[VPX_PLANE_U]
            
        return 0
    return -1

def img_alloc_helper(img, fmt, d_w, d_h, stride_align, img_data):
    h, w, s, xcs, ycs, bps, align = int_, int_, int_, int_, int_, int_, int_
    
    if not stride_align:
        stride_align = 1
    
    if stride_align & (stride_align - 1):
        print('goto fail')
    
    if fmt in (VPX_IMG_FMT_RGB32, VPX_IMG_FMT_RGB32_LE, VPX_IMG_FMT_ARGB, VPX_IMG_FMT_ARGB_LE):
        bps = 32
    elif fmt in (VPX_IMG_FMT_RGB24, VPX_IMG_FMT_BGR24):
        bps = 24
    elif fmt in (VPX_IMG_FMT_RGB565, VPX_IMG_FMT_RGB565_LE, VPX_IMG_FMT_RGB555, VPX_IMG_FMT_RGB555_LE, VPX_IMG_FMT_UYVY, VPX_IMG_FMT_YUY2, VPX_IMG_FMT_YVYU):
        bps = 16
    elif fmt in (VPX_IMG_FMT_I420, VPX_IMG_FMT_YV12, VPX_IMG_FMT_VPXI420, VPX_IMG_FMT_VPXYV12):
        bps = 12
    else:
        bps = 16
    
    if fmt in (VPX_IMG_FMT_I420, VPX_IMG_FMT_YV12, VPX_IMG_FMT_VPXI420, VPX_IMG_FMT_VPXYV12):
        xcs = 1
    else:
        xcs = 0

    if fmt in (VPX_IMG_FMT_I420, VPX_IMG_FMT_YV12, VPX_IMG_FMT_VPXI420, VPX_IMG_FMT_VPXYV12):
        ycs = 1
    else:
        ycs = 0

    align = (1 << xcs) - 1
    w = (d_w + align) & ~align
    align = (1 << ycs) - 1
    h = (d_h + align) & ~align
    s = w if (fmt & VPX_IMG_FMT_PLANAR) else bps * w / 8
    s = (s + stride_align - 1) & ~(stride_align - 1)

    if not img:
        img = vpx_image_t()
        
        if not img:
            print('goto fail')
        
        img.self_allocd = 1
    else:
        pass
    
    img.img_data = img_data
    
    if not img_data:
        img.img_data = malloc(h * w * bps / 8 if (fmt & VPX_IMG_FMT_PLANAR) else h * s, 0)
        img.img_data_owner = 1

    if not img.img_data:
        print('goto fail')
    
    img.fmt = img["fmt"] = fmt
    img.w = img["w"] = w
    img.h = img["h"] = h
    img.x_chroma_shift = img["x_chroma_shift"] = xcs
    img.y_chroma_shift = img["y_chroma_shift"] = ycs
    img.bps = img["bps"] = bps

    img.stride[VPX_PLANE_Y] = img.stride[VPX_PLANE_ALPHA] = s
    img.stride[VPX_PLANE_U] = img.stride[VPX_PLANE_V] = s >> xcs

    if not vpx_img_set_rect(img, 0, 0, d_w, d_h):
        return img

    vpx_img_free(img)
    return None


def vpx_img_alloc(img, fmt, d_w, d_h, stride_align):
    return img_alloc_helper(img, fmt, d_w, d_h, stride_align, None)

def vp8_dixie_release_ref_frame(rcimg):
    if rcimg:
        ASSERT(rcimg.ref_cnt)
        rcimg.ref_cnt -= 1

def vp8_dixie_find_free_ref_frame(frames):
    for i in range(NUM_REF_FRAMES):
        if frames[i].ref_cnt == 0:
            frames[i].ref_cnt = 1
            return frames[i]

    ASSERT(0)
    return None

def vp8_dixie_predict_init(ctx):
    i = int_
    this_frame_base = char_
    this_frame_base_off = 0
    
    if ctx.frame_hdr.frame_size_updated:
        for i in range(NUM_REF_FRAMES):
            w = ctx.mb_cols * 16 + BORDER_PIXELS * 2
            h = ctx.mb_rows * 16 + BORDER_PIXELS * 2
        
            vpx_img_free(ctx.frame_strg[i].img)
            ctx.frame_strg[i].ref_cnt = 0
            ctx.ref_frames[i] = None

            if not vpx_img_alloc(ctx.frame_strg[i].img, IMG_FMT_I420, w, h, 16):
                vpx_internal_error(ctx.error, VPX_CODEC_MEM_ERROR, "Failed to allocate " + str(w) + "x" + str(h) + " framebuffer")

            vpx_img_set_rect(ctx.frame_strg[i].img, BORDER_PIXELS, BORDER_PIXELS, ctx.frame_hdr.kf.w, ctx.frame_hdr.kf.h)
        
        if ctx.frame_hdr.version:
            ctx.subpixel_filters = bilinear_filters
        else:
            ctx.subpixel_filters = sixtap_filters
    
    if ctx.ref_frames[CURRENT_FRAME]:
        vp8_dixie_release_ref_frame(ctx.ref_frames[CURRENT_FRAME])
    
    ctx.ref_frames[CURRENT_FRAME] = vp8_dixie_find_free_ref_frame(ctx.frame_strg)
    this_frame_base = ctx.ref_frames[CURRENT_FRAME].img.img_data

    for i in range(NUM_REF_FRAMES):
        ref = ctx.ref_frames[i]

        ctx.ref_frame_offsets[i] = ref.img.img_data_off - this_frame_base_off if ref else 0
        ctx.ref_frame_offsets_[i] = ref.img.img_data if ref else this_frame_base

def dequant_init(factors, seg, quant_hdr):
    i, q = int_, int_
    dqf = factors
    dqf_off = 0
    
    for i in range(MAX_MB_SEGMENTS if seg.enabled else 1):
        q = quant_hdr.q_index
        
        if seg.enabled:
            q = q + seg.quant_idx[i] if not seg.abs_ else seg.quant_idx[i]
        
        if dqf[dqf_off].quant_idx != q or quant_hdr.delta_update:
            dqf[dqf_off].factor[TOKEN_BLOCK_Y1][0] = dc_q(q + quant_hdr.y1_dc_delta_q)
            dqf[dqf_off].factor[TOKEN_BLOCK_Y1][1] = ac_q(q)
            dqf[dqf_off].factor[TOKEN_BLOCK_UV][0] = dc_q(q + quant_hdr.uv_dc_delta_q)
            dqf[dqf_off].factor[TOKEN_BLOCK_UV][1] = ac_q(q + quant_hdr.uv_ac_delta_q)
            dqf[dqf_off].factor[TOKEN_BLOCK_Y2][0] = dc_q(q + quant_hdr.y2_dc_delta_q) * 2
            dqf[dqf_off].factor[TOKEN_BLOCK_Y2][1] = int(ac_q(q + quant_hdr.y2_ac_delta_q) * 155 / 100)

            if dqf[dqf_off].factor[TOKEN_BLOCK_Y2][1] < 8:
                dqf[dqf_off].factor[TOKEN_BLOCK_Y2][1] = 8

            if dqf[dqf_off].factor[TOKEN_BLOCK_UV][0] > 132:
                dqf[dqf_off].factor[TOKEN_BLOCK_UV][0] = 132

            dqf[dqf_off].quant_idx = q
            
        dqf_off += 1

def read_segment_id(bool, seg):
    return (2 + bool_get(bool, seg.tree_probs[2])) if bool_get(bool, seg.tree_probs[0]) else bool_get(bool, seg.tree_probs[1])

def bool_read_tree(bool_value, t, p, p_off=None):
    i = 0
    
    if p_off is not None:
        while True:
            i = t[i + bool_get(bool_value, p[p_off + (i >> 1)])]
            if i <= 0:
                break
    else:
        while True:
            i = t[i + bool_get(bool_value, p[i >> 1])]
            if i <= 0:
                break

    return -i

def above_block_mode(this_, above, b):
    if b < 4:
        if above.base.y_mode == DC_PRED:
            return B_DC_PRED
        elif above.base.y_mode == V_PRED:
            return B_VE_PRED
        elif above.base.y_mode == H_PRED:
            return B_HE_PRED
        elif above.base.y_mode == TM_PRED:
            return B_TM_PRED
        elif above.base.y_mode == B_PRED:
            return above.splitt.mvs[b + 12].d.x
        else:
            ASSERT(0)

    return this_.splitt.mvs[b - 4].d.x

def left_block_mode(this_, left, b):
    if not (b & 3):
        if left.base.y_mode == DC_PRED:
            return B_DC_PRED
        elif left.base.y_mode == V_PRED:
            return B_VE_PRED
        elif left.base.y_mode == H_PRED:
            return B_HE_PRED
        elif left.base.y_mode == TM_PRED:
            return B_TM_PRED
        elif left.base.y_mode == B_PRED:
            return left.splitt.mvs[b + 3].d.x
        else:
            ASSERT(0)

    return this_.splitt.mvs[b - 1].d.x

def mv_bias(mb, sign_bias, ref_frame, mv):
    if sign_bias[mb.base.ref_frame] ^ sign_bias[ref_frame]:
        mv.d.x *= -1
        mv.d.y *= -1

this_mv_1 = mv()
this_mv_2 = mv()

def decode_kf_mb_mode(this_, this_off, left, left_off, above, above_off, bool):
    y_mode, uv_mode = int_, int_

    y_mode = bool_read_tree(bool, kf_y_mode_tree, kf_y_mode_probs)

    if y_mode == B_PRED:
        for i in range(16):
            a = above_block_mode(this_[this_off], above[above_off], i)
            l = left_block_mode(this_[this_off], left[left_off], i)
            b = 0

            b = bool_read_tree(bool, b_mode_tree, kf_b_mode_probs[a][l])
            this_[this_off].splitt.modes[i] = this_[this_off].splitt.mvs[i].d.x = b; this_[this_off].splitt.mvs[i].d.y = 0

    uv_mode = bool_read_tree(bool, uv_mode_tree, kf_uv_mode_probs)

    this_[this_off].base.y_mode = y_mode
    this_[this_off].base.uv_mode = uv_mode
    this_[this_off].base.mv.d.x = this_[this_off].base.mv.d.y = 0
    this_[this_off].base.ref_frame = 0

def find_near_mvs(this_, left, left_off, above, above_off, sign_bias, near_mvs, cnt):
    aboveleft = above
    aboveleft_off = above_off - 1
    mv_ = near_mvs
    mv_off = 0
    cntx = cnt
    cntx_off = 0

    mv_[0].d.x = mv_[1].d.x = mv_[2].d.x = 0
    mv_[0].d.y = mv_[1].d.y = mv_[2].d.y = 0
    cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0

    above_ = above[above_off]
    left_ = left[left_off]
    aboveleft_ = aboveleft[aboveleft_off]
    
    if above_.base.ref_frame != CURRENT_FRAME:
        if above_.base.mv.d.x or above_.base.mv.d.y:
            mv_off += 1
            mv_[mv_off].d.x = above_.base.mv.d.x
            mv_[mv_off].d.y = above_.base.mv.d.y
            mv_bias(above_, sign_bias, this_.base.ref_frame, mv_[mv_off])
            cntx_off += 1

        cntx[cntx_off] += 2


    if left_.base.ref_frame != CURRENT_FRAME:
        if left_.base.mv.d.x or left_.base.mv.d.y:
            this_mv = this_mv_1

            this_mv.d.x = left_.base.mv.d.x
            this_mv.d.y = left_.base.mv.d.y
            mv_bias(left_, sign_bias, this_.base.ref_frame, this_mv)

            if this_mv.d.x != mv_[mv_off].d.x or this_mv.d.y != mv_[mv_off].d.y:
                mv_off += 1
                mv_[mv_off].d.x = this_mv.d.x
                mv_[mv_off].d.y = this_mv.d.y
                cntx_off += 1

            cntx[cntx_off] += 2
        else:
            cnt[CNT_ZEROZERO] += 2
    
    
    if aboveleft_.base.ref_frame != CURRENT_FRAME:
        if aboveleft_.base.mv.d.x or aboveleft_.base.mv.d.y:
            this_mv = this_mv_2

            this_mv.d.x = aboveleft_.base.mv.d.x
            this_mv.d.y = aboveleft_.base.mv.d.y
            mv_bias(aboveleft_, sign_bias, this_.base.ref_frame, this_mv)

            if this_mv.d.x != mv_[mv_off].d.x or this_mv.d.y != mv_[mv_off].d.y:
                mv_off += 1
                mv_[mv_off].d.x = this_mv.d.x
                mv_[mv_off].d.y = this_mv.d.y
                cntx_off += 1

            cntx[cntx_off] += 1
        else:
            cnt[CNT_ZEROZERO] += 1
    
    if cnt[CNT_SPLITMV]:
        if mv_[mv_off].d.x == near_mvs[CNT_NEAREST].d.x and mv_[mv_off].d.y == near_mvs[CNT_NEAREST].d.y:
            cnt[CNT_NEAREST] += 1
    
    cnt[CNT_SPLITMV] = ((above_.base.y_mode == SPLITMV) + (left_.base.y_mode == SPLITMV)) * 2 + (aboveleft_.base.y_mode == SPLITMV)
    
    if cnt[CNT_NEAR] > cnt[CNT_NEAREST]:
        tmp, tmp2 = int_, int_
        tmp = cnt[CNT_NEAREST]
        cnt[CNT_NEAREST] = cnt[CNT_NEAR]
        cnt[CNT_NEAR] = tmp
        tmp = near_mvs[CNT_NEAREST].d.x
        tmp2 = near_mvs[CNT_NEAREST].d.y
        near_mvs[CNT_NEAREST].d.x = near_mvs[CNT_NEAR].d.x
        near_mvs[CNT_NEAREST].d.y = near_mvs[CNT_NEAR].d.y
        near_mvs[CNT_NEAR].d.x = tmp
        near_mvs[CNT_NEAR].d.y = tmp2

    if cnt[CNT_NEAREST] >= cnt[CNT_BEST]:
        near_mvs[CNT_BEST].d.x = near_mvs[CNT_NEAREST].d.x
        near_mvs[CNT_BEST].d.y = near_mvs[CNT_NEAREST].d.y

near_mvs_4 = Arr_new(4, mv)
mv_cnts_4 = [0, 0, 0, 0]
probs_4 = [0, 0, 0, 0]
chroma_mv_4 = Arr_new(4, mv)
clamped_best_mv_1 = mv()

def clamp_mv(raw, bounds):
    newmv = mv()

    newmv.d.x = bounds.to_left if (raw.d.x < bounds.to_left) else raw.d.x
    newmv.d.x = bounds.to_right if (raw.d.x > bounds.to_right) else newmv.d.x
    newmv.d.y = bounds.to_top if (raw.d.y < bounds.to_top) else raw.d.y
    newmv.d.y = bounds.to_bottom if (raw.d.y > bounds.to_bottom) else newmv.d.y
    return newmv

def read_mv_component(bool, mvc):
    IS_SHORT = 0
    SIGN = 1
    SHORT = 2
    BITS = SHORT + 8 - 1
    LONG_WIDTH = 10
    x = 0

    if bool_get(bool, mvc[IS_SHORT]):
        for i in range(3):
            x += bool_get(bool, mvc[BITS + i]) << i

        for i in range(LONG_WIDTH - 1, 3, -1):
            x += bool_get(bool, mvc[BITS + i]) << i

        if not (x & 0xFFF0) or bool_get(bool, mvc[BITS + 3]):
            x += 8
            
    else:
        x = bool_read_tree(bool, small_mv_tree, mvc, + SHORT)

    if x and bool_get(bool, mvc[SIGN]):
        x = -x

    return (x << 1)

def read_mv(bool, mv, mvc):
    mv.d.y = read_mv_component(bool, mvc[0])
    mv.d.x = read_mv_component(bool, mvc[1])

def left_block_mv(this_, left_, b):
    if not (b & 3):
        if left_.base.y_mode == SPLITMV:
            return left_.splitt.mvs[b + 3]

        return left_.base.mv

    return this_.splitt.mvs[b - 1]

def above_block_mv(this_, above_, b):
    if b < 4:
        if above_.base.y_mode == SPLITMV:
            return above_.splitt.mvs[b + 12]

        return above_.base.mv

    return this_.splitt.mvs[b - 4]

def submv_ref(bool, l, a):
    SUBMVREF_NORMAL = 0
    SUBMVREF_LEFT_ZED = 1
    SUBMVREF_ABOVE_ZED = 2
    SUBMVREF_LEFT_ABOVE_SAME = 3
    SUBMVREF_LEFT_ABOVE_ZED = 4
    
    lez = not (l.d.x or l.d.y) + 0
    aez = not (a.d.x or a.d.y) + 0
    lea = (l.d.x == a.d.x and l.d.y == a.d.y) + 0
    ctx = SUBMVREF_NORMAL

    if (lea and lez):
        ctx = SUBMVREF_LEFT_ABOVE_ZED
    elif (lea):
        ctx = SUBMVREF_LEFT_ABOVE_SAME
    elif (aez):
        ctx = SUBMVREF_ABOVE_ZED
    elif (lez):
        ctx = SUBMVREF_LEFT_ZED

    return bool_read_tree(bool, submv_ref_tree, submv_ref_probs2[ctx])


def decode_split_mv(this_, left_, above_, hdr, best_mv, bool):
    partition = int_
    j, k, mask, partition_id = int_, int_, int_, int_

    partition_id = bool_read_tree(bool, split_mv_tree, split_mv_probs)
    partition = mv_partitions[partition_id]
    this_.base.partitioning = partition_id
    
    j, mask = 0, 0
    
    while mask < 65535:
        mv_ = mv()
        left_mv, above_mv, subblock_mode = None, None, None
        
        k = 0
        while j != partition[k]:
            k += 1
        
        left_mv = left_block_mv(this_, left_, k)
        above_mv = above_block_mv(this_, above_, k)
        subblock_mode = submv_ref(bool, left_mv, above_mv)
        
        if subblock_mode == LEFT4X4:
            mv_ = left_mv
        elif subblock_mode == ABOVE4X4:
            mv_ = above_mv
        elif subblock_mode == ZERO4X4:
            mv_.d.x = mv_.d.y = 0
        elif subblock_mode == NEW4X4:
            read_mv(bool, mv_, hdr.mv_probs)
            mv_.d.x += best_mv.d.x
            mv_.d.y += best_mv.d.y
        else:
            ASSERT(0)

        while k < 16:
            if j == partition[k]:
                this_.splitt.mvs[k].d.x = mv_.d.x
                this_.splitt.mvs[k].d.y = mv_.d.y
                mask |= 1 << k
            
            k += 1
        
        j += 1

def need_mc_border(mv, l, t, b_w, w, h):
    b, r = int_, int_

    l += (mv.d.x >> 3)
    t += (mv.d.y >> 3)

    r = w - (l + b_w)
    b = h - (t + b_w)

    return (l >> 1 < 2 or r >> 1 < 3 or t >> 1 < 2 or b >> 1 < 3)

def decode_mvs(ctx, this_, this_off, left, left_off, above, above_off, bounds, bool):
    hdr = ctx.entropy_hdr
    near_mvs = near_mvs_4
    clamped_best_mv = clamped_best_mv_1
    mv_cnts = mv_cnts_4
    probs = probs_4
    BEST, NEAREST, NEAR = 0, 1, 2
    x, y, w, h, b = int_, int_, int_, int_, int_
    
    this_[this_off].base.ref_frame = (2 + bool_get(bool, hdr.prob_gf)) if bool_get(bool, hdr.prob_last) else 1

    find_near_mvs(this_[this_off], this_, this_off - 1, above, above_off, ctx.reference_hdr.sign_bias, near_mvs, mv_cnts)
    probs[0] = mv_counts_to_probs[mv_cnts[0]][0]
    probs[1] = mv_counts_to_probs[mv_cnts[1]][1]
    probs[2] = mv_counts_to_probs[mv_cnts[2]][2]
    probs[3] = mv_counts_to_probs[mv_cnts[3]][3]
    
    this_ = this_[this_off]

    this_.base.y_mode = bool_read_tree(bool, mv_ref_tree, probs)
    this_.base.uv_mode = this_.base.y_mode

    this_.base.need_mc_border = 0
    x = (-bounds.to_left - 128) >> 3
    y = (-bounds.to_top - 128) >> 3
    w = ctx.mb_cols * 16
    h = ctx.mb_rows * 16
    
    if this_.base.y_mode == NEARESTMV:
        this_.base.mv = clamp_mv(near_mvs[NEAREST], bounds)
        
    elif this_.base.y_mode == NEARMV:
        this_.base.mv = clamp_mv(near_mvs[NEAR], bounds)
        
    elif this_.base.y_mode == ZEROMV:
        this_.base.mv.d.x = this_.base.mv.d.y = 0
        
    elif this_.base.y_mode == NEWMV:
        clamped_best_mv = clamp_mv(near_mvs[BEST], bounds)
        read_mv(bool, this_.base.mv, hdr.mv_probs)
        this_.base.mv.d.x += clamped_best_mv.d.x
        this_.base.mv.d.y += clamped_best_mv.d.y
        
    elif this_.base.y_mode == SPLITMV:
        chroma_mv = chroma_mv_4

        clamped_best_mv = clamp_mv(near_mvs[BEST], bounds)
        decode_split_mv(this_, left[left_off], above[above_off], hdr, clamped_best_mv, bool)
        this_.base.mv.d.x = this_.splitt.mvs[15].d.x
        this_.base.mv.d.y = this_.splitt.mvs[15].d.y

        for b in range(16):
            chroma_mv[(b >> 1 & 1) + (b >> 2 & 2)].d.x += this_.splitt.mvs[b].d.x
            chroma_mv[(b >> 1 & 1) + (b >> 2 & 2)].d.y += this_.splitt.mvs[b].d.y

            if need_mc_border(this_.splitt.mvs[b], x + (b & 3) * 4, y + (b & ~3), 4, w, h):
                this_.base.need_mc_border = 1
                break

        for b in range(4):
            chroma_mv[b].d.x += 4
            chroma_mv[b].d.y += 4
            chroma_mv[b].d.x >>= 2
            chroma_mv[b].d.y >>= 2

            if need_mc_border(chroma_mv[b], x + (b & 1) * 8, y + (b >> 1) * 8, 16, w, h):
                this_.base.need_mc_border = 1
                break

        return
    
    else:
        ASSERT(0)
    
    if need_mc_border(this_.base.mv, x, y, 16, w, h):
        this_.base.need_mc_border = 1

def decode_intra_mb_mode(this_, hdr, bool):
    y_mode, uv_mode = int_, int_

    y_mode = bool_read_tree(bool, y_mode_tree, hdr.y_mode_probs)

    if y_mode == B_PRED:
        i = int_

        for i in range(16):
            b = bool_read_tree(bool, b_mode_tree, default_b_mode_probs)
            this_.splitt.modes[i] = this_.splitt.mvs[i].d.x = b; this_.splitt.mvs[i].d.y = 0

    uv_mode = bool_read_tree(bool, uv_mode_tree, hdr.uv_mode_probs)

    this_.base.y_mode = y_mode
    this_.base.uv_mode = uv_mode
    this_.base.mv.d.x = this_.base.mv.d.y = 0
    this_.base.ref_frame = CURRENT_FRAME

bounds_ = mv_clamp_rect()
def vp8_dixie_modemv_process_row(ctx, bool, row, start_col, num_cols):
    above, above_off, this_, this_off = None, 0, None, 0
    col = int_
    bounds = bounds_
    
    this_ = ctx.mb_info_rows[1 + row]
    this_off = ctx.mb_info_rows_off[1 + row] + start_col
    above = ctx.mb_info_rows[1 + row - 1]
    above_off = ctx.mb_info_rows_off[1 + row - 1] + start_col
    
    bounds.to_left = -((start_col + 1) << 7)
    bounds.to_right = (ctx.mb_cols - start_col) << 7
    bounds.to_top = -((row + 1) << 7)
    bounds.to_bottom = (ctx.mb_rows - row) << 7
    
    for col in range(start_col, start_col + num_cols):
        if ctx.segment_hdr.update_map:
            this_[this_off].base.segment_id = read_segment_id(bool, ctx.segment_hdr)
        
        if ctx.entropy_hdr.coeff_skip_enabled:
            this_[this_off].base.skip_coeff = bool_get(bool, ctx.entropy_hdr.coeff_skip_prob)

        if ctx.frame_hdr.is_keyframe:
            if not ctx.segment_hdr.update_map:
                this_[this_off].base.segment_id = 0

            decode_kf_mb_mode(this_, this_off, this_, this_off - 1, above, above_off, bool)

        else:
            if bool_get(bool, ctx.entropy_hdr.prob_inter):
                decode_mvs(ctx, this_, this_off, this_, this_off - 1, above, above_off, bounds, bool)
            else:
                decode_intra_mb_mode(this_[this_off], ctx.entropy_hdr, bool)

            bounds.to_left -= 16 << 3
            bounds.to_right -= 16 << 3
        
        this_off += 1
        above_off += 1

def vp8_dixie_tokens_process_row(ctx, partition, row, start_col, num_cols):
    pass


bool_1 = bool_decoder()
def decode_frame(ctx, data, data_off, sz):
    res = None
    bool = bool_1
    i, row, partition = int_, int_, int_
    
    ctx.saved_entropy_valid = 0
    
    res = vp8_parse_frame_header(data, sz, ctx.frame_hdr)
    if res:
        vpx_internal_error(ctx.error, res, "Failed to parse frame header")
    
    if ctx.frame_hdr.is_experimental:
        vpx_internal_error(ctx.error, VPX_CODEC_UNSUP_BITSTREAM, "Experimental bitstreams not supported.")
    
    data_off += FRAME_HEADER_SZ
    sz -= FRAME_HEADER_SZ
    
    if ctx.frame_hdr.is_keyframe:
        data_off += KEYFRAME_HEADER_SZ
        sz -= KEYFRAME_HEADER_SZ
        ctx.mb_cols = math.ceil((ctx.frame_hdr.kf.w + 15) / 16)
        ctx.mb_rows = math.ceil((ctx.frame_hdr.kf.h + 15) / 16)
    
    init_bool_decoder(bool, data, data_off, ctx.frame_hdr.part0_sz)
    
    if ctx.frame_hdr.is_keyframe:
        if bool_get_uint(bool, 2):
            vpx_internal_error(ctx.error, VPX_CODEC_UNSUP_BITSTREAM, "Reserved bits not supported")
    
    decode_segmentation_header(ctx, bool, ctx.segment_hdr)
    decode_loopfilter_header(ctx, bool, ctx.loopfilter_hdr)
    decode_and_init_token_partitions(ctx,
        bool, data, data_off + ctx.frame_hdr.part0_sz,
        sz - ctx.frame_hdr.part0_sz, ctx.token_hdr
    )
    decode_quantizer_header(ctx, bool, ctx.quant_hdr)
    decode_reference_header(ctx, bool, ctx.reference_hdr)
    
    if ctx.frame_hdr.is_keyframe:
        i, j, k, l, ii = int_, int_, int_, int_, 0
        
        for i in range(BLOCK_TYPES):
            for j in range(COEF_BANDS):
                for k in range(PREV_COEF_CONTEXTS):
                    for l in range(ENTROPY_NODES):
                        ctx.entropy_hdr.coeff_probs_[ii] = ctx.entropy_hdr.coeff_probs[i][j][k][l] = k_default_coeff_probs[i][j][k][l]
                        ii += 1
        
        ctx.entropy_hdr.mv_probs = k_default_mv_probs()
        ARRAY_COPY(ctx.entropy_hdr.y_mode_probs, k_default_y_mode_probs)
        ARRAY_COPY(ctx.entropy_hdr.uv_mode_probs, k_default_uv_mode_probs)
    
    if not ctx.reference_hdr.refresh_entropy:
        TO = ctx.saved_entropy
        FROM = ctx.entropy_hdr
        ii = 0
        
        for i in range(BLOCK_TYPES):
            for j in range(COEF_BANDS):
                for k in range(PREV_COEF_CONTEXTS):
                    for l in range(ENTROPY_NODES):
                        TO.coeff_probs_[ii] = TO.coeff_probs[i][j][k][l] = FROM.coeff_probs[i][j][k][l]
                        ii += 1
        
        TO.coeff_skip_enabled = FROM.coeff_skip_enabled
        TO.coeff_skip_prob = FROM.coeff_skip_prob
        for i in range(2):
            for j in range(19):
                TO.mv_probs[i][j] = FROM.mv_probs[i][j]
        TO.prob_gf = FROM.prob_gf
        TO.prob_inter = FROM.prob_inter
        TO.prob_last = FROM.prob_last
        for i in range(3):
            TO.uv_mode_probs[i] = FROM.uv_mode_probs[i]
        for i in range(4):
            TO.y_mode_probs[i] = FROM.y_mode_probs[i]
        
        ctx.saved_entropy_valid = 1
    
    decode_entropy_header(ctx, bool, ctx.entropy_hdr)
    
    vp8_dixie_modemv_init(ctx)
    vp8_dixie_tokens_init(ctx)
    vp8_dixie_predict_init(ctx)
    dequant_init(ctx.dequant_factors, ctx.segment_hdr, ctx.quant_hdr)
    
    partition = 0
    for row in range(ctx.mb_rows):
        vp8_dixie_modemv_process_row(ctx, bool, row, 0, ctx.mb_cols)
        vp8_dixie_tokens_process_row(ctx, partition, row, 0, ctx.mb_cols)
        vp8_dixie_predict_process_row(ctx, row, 0, ctx.mb_cols)

        if ctx.loopfilter_hdr.level and row:
            vp8_dixie_loopfilter_process_row(ctx, row - 1, 0, ctx.mb_cols)

        partition += 1
        if partition == ctx.token_hdr.partitions:
            partition = 0
    
    if (ctx.loop_filter_hdr.level):
        vp8_dixie_loopfilter_process_row(ctx, row - 1, 0, ctx.mb_cols)
    
    ctx.frame_cnt += 1
    
    if not ctx.reference_hdr.refresh_entropy:
        TO, FROM, ii = ctx.entropy_hdr, ctx.saved_entropy, 0
        for i in range(BLOCK_TYPES):
            for j in range(COEF_BANDS):
                for k in range(PREV_COEF_CONTEXTS):
                    for l in range(ENTROPY_NODES):
                        TO.coeff_probs_[ii] = TO.coeff_probs[i][j][k][l] = FROM.coeff_probs[i][j][k][l] = FROM.coeff_probs_[ii]
                        i += 1
        
        TO.coeff_skip_enabled = FROM.coeff_skip_enabled
        TO.coeff_skip_prob = FROM.coeff_skip_prob
        for i in range(2):
            for j in range(19):
                TO.mv_probs[i][j] = FROM.mv_probs[i][j]
        TO.prob_gf = FROM.prob_gf
        TO.prob_inter = FROM.prob_inter
        TO.prob_last = FROM.prob_last
        for i in range(3):
            TO.uv_mode_probs[i] = FROM.uv_mode_probs[i]
        for i in range(4):
            TO.y_mode_probs[i] = FROM.y_mode_probs[i]

        ctx.saved_entropy_valid = 0
    
    # Handle reference frame updates
    if ctx.reference_hdr.copy_arf == 1:
        vp8_dixie_release_ref_frame(ctx.ref_frames[ALTREF_FRAME])
        ctx.ref_frames[ALTREF_FRAME] = vp8_dixie_ref_frame(ctx.ref_frames[LAST_FRAME])
    elif ctx.reference_hdr.copy_arf == 2:
        vp8_dixie_release_ref_frame(ctx.ref_frames[ALTREF_FRAME])
        ctx.ref_frames[ALTREF_FRAME] = vp8_dixie_ref_frame(ctx.ref_frames[GOLDEN_FRAME])

    if ctx.reference_hdr.copy_gf == 1:
        vp8_dixie_release_ref_frame(ctx.ref_frames[GOLDEN_FRAME])
        ctx.ref_frames[GOLDEN_FRAME] = vp8_dixie_ref_frame(ctx.ref_frames[LAST_FRAME])
    elif ctx.reference_hdr.copy_gf == 2:
        vp8_dixie_release_ref_frame(ctx.ref_frames[GOLDEN_FRAME])
        ctx.ref_frames[GOLDEN_FRAME] = vp8_dixie_ref_frame(ctx.ref_frames[ALTREF_FRAME])

    if ctx.reference_hdr.refresh_gf:
        vp8_dixie_release_ref_frame(ctx.ref_frames[GOLDEN_FRAME])
        ctx.ref_frames[GOLDEN_FRAME] = vp8_dixie_ref_frame(ctx.ref_frames[CURRENT_FRAME])

    if ctx.reference_hdr.refresh_arf:
        vp8_dixie_release_ref_frame(ctx.ref_frames[ALTREF_FRAME])
        ctx.ref_frames[ALTREF_FRAME] = vp8_dixie_ref_frame(ctx.ref_frames[CURRENT_FRAME])

    if ctx.reference_hdr.refresh_last:
        vp8_dixie_release_ref_frame(ctx.ref_frames[LAST_FRAME])
        ctx.ref_frames[LAST_FRAME] = vp8_dixie_ref_frame(ctx.ref_frames[CURRENT_FRAME])


def vp8_dixie_decode_frame(ctx, data, sz):
    ctx_ = ctx
    
    ctx.error.error_code = VPX_CODEC_OK
    ctx.error.has_detail = 0
    
    if setjmp(ctx.error.jmp):
        decode_frame(ctx, data, 0, sz)
    
    return ctx_.error.error_code


def main(AJAX_response):
    buf, buf_off = [None], [None]
    buf_sz, buf_alloc_sz = [0], [0]
    infile = { "data": AJAX_response, "data_off": 0 }
    
    fourcc = [int_]
    width = [int_]
    height = [int_]
    fps_den = [int_]
    fps_num = [int_]
    
    input = input_ctx()
    
    input.infile = infile
    
    input.kind = WEBM_FILE
    
    decoder2 = vp8_decoder_ctx()
    
    def readframe(ii):
        isframe = not read_frame(input, buf, buf_off, buf_sz, buf_alloc_sz)
        if isframe:
            # sleep?
            buf = buf[0]
            
            vp8_dixie_decode_frame(decoder2, buf, buf_sz)
            buf = [buf]
            img_avail = decoder2.frame_hdr.is_shown
            img = decoder2.ref_frames[0].img
            
            print('TIMECODE ' + input.pkt[0].timecode + ' (' + str(input.pkt[0].timecode // 1000000000) + ' sec)')
            if img_avail:
                # show fps
                if img:
                    vpximg2canvas(img)
                ii += 1
                print('FRAME ' + ii)
            readframe(ii)

    readframe(0)

def fileInput(file):
    print('Got file input: ' + file)
    with open(file, 'rb') as file:
        binary_data = file.read()

    result = list(binary_data)
    
    main(result)


fileInput('./video.webm')
