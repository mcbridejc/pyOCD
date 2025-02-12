# pyOCD debugger
# Copyright (c) 2006-2013 Arm Limited
# Copyright (c) 2021 Chris Reed
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import (FlashRegion, RamRegion, MemoryMap)

FLASH_ALGO = {
    'load_address' : 0x3fff4000,
    'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4770ba40, 0x4770bac0, 0x4770ba40, 0x4770bac0, 0xf2402a03, 0xf0108030, 0xf0000c03, 0xf8118015,
    0xf1bc3b01, 0x44620f02, 0xf811bf98, 0xf800cb01, 0xbf383b01, 0x3b01f811, 0x0204f1a2, 0xf800bf98,
    0xbf38cb01, 0x3b01f800, 0x0303f011, 0x8025f000, 0xf0c03a08, 0xf8518008, 0x3a083b04, 0xcb04f851,
    0x1008e8a0, 0x1d12e7f5, 0xf851bf5c, 0xf8403b04, 0xf3af3b04, 0x07d28000, 0xf811bf24, 0xf8113b01,
    0xbf48cb01, 0x2b01f811, 0xf800bf24, 0xf8003b01, 0xbf48cb01, 0x2b01f800, 0xb5104770, 0xf0c03a20,
    0xe8b1800b, 0x3a205018, 0x5018e8a0, 0x5018e8b1, 0x5018e8a0, 0xaff5f4bf, 0x7c02ea5f, 0xe8b1bf24,
    0xe8a05018, 0xbf445018, 0xc018c918, 0x4010e8bd, 0x7c82ea5f, 0xf851bf24, 0xf8403b04, 0xbf083b04,
    0x07d24770, 0xf831bf28, 0xbf483b02, 0x2b01f811, 0xf820bf28, 0xbf483b02, 0x2b01f800, 0x20004770,
    0x00004770, 0xb5104803, 0xf0004478, 0x2000f8b5, 0x0000bd10, 0x00000390, 0x9800b501, 0x5f00f5b0,
    0x2001bf3c, 0xf410bd08, 0x466a1f80, 0x0102f04f, 0x4804bf1c, 0xbf044478, 0x44784803, 0xf80ef000,
    0xbd082000, 0x00000370, 0x0000035e, 0x69c14770, 0x0f01f011, 0x69c0bf18, 0x00004770, 0x4c44b410,
    0xc110f8df, 0xd27f2906, 0xf001e8df, 0x562a037e, 0x6801704a, 0x1f80f411, 0xf44fbf14, 0xf44f1181,
    0x68425100, 0x684160d1, 0x6801610c, 0x1f80f411, 0xbf146841, 0xc018f8c1, 0xc014f8c1, 0x68422102,
    0x68016091, 0xf4116840, 0xd0041f80, 0xf0116801, 0xd1fb0f02, 0x6801e058, 0x0f01f011, 0xe053d1fb,
    0x68426811, 0x68026114, 0x1f80f412, 0xbf146842, 0xc018f8c2, 0xc014f8c2, 0x60d16842, 0x21016842,
    0x68016091, 0xf4116840, 0xd0041f80, 0xf0116801, 0xd1fb0f02, 0x6801e038, 0x0f01f011, 0xe033d1fb,
    0x68406801, 0x1f80f411, 0xbf146841, 0x0101f041, 0x0102f041, 0xe0276041, 0xf4116801, 0x68411f80,
    0xbf14684a, 0x0201f022, 0x0202f022, 0x6801604a, 0xf4116840, 0xd0041f80, 0xf0116801, 0xd1fb0f02,
    0x6801e012, 0x0f01f011, 0xe00dd1fb, 0x68406801, 0x1f80f411, 0x6801d004, 0x0f02f011, 0xe003d1fb,
    0xf0116801, 0xd1fb0f01, 0x2001bc10, 0x00004770, 0xbb781ae9, 0xb56d9099, 0xf4116801, 0x68411f80,
    0xf44fbf14, 0xf44f1281, 0x60ca5200, 0x49076842, 0x68016111, 0xf4116842, 0x49051f80, 0x6191bf14,
    0x21026151, 0x60816840, 0x00004770, 0xbb781ae9, 0xb56d9099, 0x4a086843, 0x6802611a, 0xf4126843,
    0x4a061f80, 0x619abf14, 0x6842615a, 0x684060d1, 0x60812101, 0x00004770, 0xbb781ae9, 0xb56d9099,
    0x68406801, 0x1f80f411, 0xbf146841, 0x0101f041, 0x0102f041, 0x47706041, 0x68406801, 0x1f80f411,
    0xbf146841, 0x0101f021, 0x0102f021, 0x47706041, 0x1e5b6808, 0xf810d305, 0xf802cb01, 0x1e5bcb01,
    0x6008d2f9, 0x47702001, 0x68406801, 0x1f80f411, 0x6801d004, 0x0f02f011, 0x4770d1fb, 0xf0116801,
    0xd1fb0f01, 0x00004770, 0x49056842, 0x68016111, 0xf4116840, 0x49031f80, 0x6181bf14, 0x47706141,
    0xbb781ae9, 0xb56d9099, 0x4614b510, 0x68084602, 0x5f00f5b0, 0x010af3c0, 0xb131d20b, 0x0c0af3c0,
    0x6100f5cc, 0xd905428b, 0xf5b3e00a, 0xd8076f00, 0xb139e00b, 0x0c0af3c0, 0x6100f5cc, 0xd904428b,
    0xbd102000, 0x6f00f5b3, 0xf8d2d8fa, 0xf8dcc004, 0xf0411004, 0xf8cc0140, 0xf8d21004, 0x4908c004,
    0x1010f8cc, 0x68526811, 0x1f80f411, 0xbf144905, 0x61516191, 0x4621461a, 0xfe1af7ff, 0xbd102001,
    0xbb781ae9, 0xb56d9099, 0xb5104916, 0xf422690a, 0x610a0200, 0x22e0f04f, 0xf8c2211f, 0xf8c21180,
    0x4a111280, 0x6120f04f, 0xf4106011, 0xf04f1f80, 0xf04f0200, 0xd0080103, 0x4478480c, 0xfe9ef7ff,
    0x2200480b, 0x44782104, 0x480ae007, 0xf7ff4478, 0x4808fe95, 0x21042200, 0xf7ff4478, 0x2000fe8f,
    0x0000bd10, 0x4001b000, 0xe000ed04, 0x0000008a, 0x00000072, 0x0000006c, 0x9800b507, 0x5f00f5b0,
    0x460bd310, 0x1f80f410, 0xbf1c4669, 0x44784807, 0x4807bf04, 0xf7ff4478, 0x2801ff77, 0x2000bf02,
    0xbd00b003, 0xb0032001, 0x0000bd00, 0x00000036, 0x00000024, 0x47702000, 0x47702000, 0x00000000,
    0x40017000, 0x00000008, 0x00100000, 0x40017000, 0x00000008, 0x00000000, 0x00000000, 0x00000000,
    0x00000000,
    ],

    'pc_init' : 0x3FFF4409,
    'pc_verify' : 0x3FFF44B9,
    'pc_uninit' : 0x3FFF44B5,
    'pc_eraseAll' : 0x3FFF4125,
    'pc_program_page' : 0x3FFF4479,
    'pc_erase_sector' : 0x3FFF4139,

    'static_base' : 0x3fff4000 + 0x00000020 + 0x000004b4,
    'begin_data' : 0x3fff4000 + 0x00000A00,
    'begin_stack' : 0x3fff4800,
    'page_size' : 0x00000800,
    'min_program_length' : 0x00000800,
    'analyzer_supported' : False,
}


class NCS36510(CoreSightTarget):

    VENDOR = "ONSemiconductor"
    
    MEMORY_MAP = MemoryMap(
        FlashRegion(    start=0x2000,           length=0x50000,      blocksize=0x800, is_boot_memory=True,
            algo=FLASH_ALGO),
        RamRegion(      start=0x3FFF4000,  length=0xC000)
        )

    def __init__(self, session):
        super(NCS36510, self).__init__(session, self.MEMORY_MAP)
