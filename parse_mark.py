#!/usr/bin/env python

import os
import sys

print("begin")

n = 0
def save(f, time):
    f.write("Mrk {\n");
    event = "    Event: \"%d\"\n" %(n);
    f.write(event);
    f.write("    Desc: \"CAMERA PLUSE\"\n");
    f.write("    GTim: ");
    Gtim = time[1] + time[2] / 1e9;
    Gtim = format(Gtim, '.6f');
    f.write(str(Gtim) + " " + str(time[0]) + "\n");
    f.write("}\n");

infile = open(sys.argv[1], "r");
filename = os.path.basename(sys.argv[1]);
path = filename.replace(".bin", "_mark.txt");
outfile = open(os.getcwd() + "/" + path, "wb");

a = infile.read(1);

while a != "":
    if a == '\xaa':
        a = infile.read(2);
        if a[0] == '\x44' and a[1] == '\x12':
            a = infile.read(28-3); # head
            if (a[1] != '\x35' or  a[2] != '\x01'):
                continue;
            b = infile.read(4); # unused
            c = infile.read(4); # week
            week = ord(c[3]) << 24 | ord(c[2]) << 16 | ord(c[1]) << 8 | ord(c[0]) << 0;
            c = infile.read(4); # sec
            sec = ord(c[3]) << 24 | ord(c[2]) << 16 | ord(c[1]) << 8 | ord(c[0]) << 0;
            c = infile.read(4); # nsec
            nsec = ord(c[3]) << 24 | ord(c[2]) << 16 | ord(c[1]) << 8 | ord(c[0]) << 0;
            save(outfile, [week, sec, nsec]);
            n += 1;

    a = infile.read(1);

infile.close();
outfile.close();

print("end")
