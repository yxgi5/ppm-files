#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fd = open('rgb888.ppm', "w")


width_out=640
height_out=480
fd.write("P3\n")
fd.write("%0d %0d\n" % (width_out, height_out))
fd.write("%0d\n" % (2**8-1))
for y in range(height_out):
    for x in range(width_out):
        if(x<width_out/8):
            fd.write("%0d\n%0d\n%0d\n" % (0xff, 0xff, 0xff))
        elif((x>=width_out/8) and x< ((width_out/8)*2)):
            fd.write("%0d\n%0d\n%0d\n" % (0xff, 0xff, 0x00))
        elif((x>=(width_out/8)*2) and x< ((width_out/8)*3)):
            fd.write("%0d\n%0d\n%0d\n" % (0x00, 0xff, 0xff))
        elif((x>=(width_out/8)*3) and x< ((width_out/8)*4)):
            fd.write("%0d\n%0d\n%0d\n" % (0x00, 0xff, 0x00))
        elif((x>=(width_out/8)*4) and x< ((width_out/8)*5)):
            fd.write("%0d\n%0d\n%0d\n" % (0xff, 0x00, 0xff))
        elif((x>=(width_out/8)*5) and x< ((width_out/8)*6)):
            fd.write("%0d\n%0d\n%0d\n" % (0xff, 0x00, 0x00))
        elif((x>=(width_out/8)*6) and x< ((width_out/8)*7)):
            fd.write("%0d\n%0d\n%0d\n" % (0x00, 0x00, 0xff))
        elif((x>=(width_out/8)*7) and (x<width_out)):
            fd.write("%0d\n%0d\n%0d\n" % (0x00, 0x00, 0x00))
fd.close()