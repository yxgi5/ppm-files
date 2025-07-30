从P2到P5，实际上用后缀来表示的
convert image_out_1.ppm  +compress out.pgm


    PNM_P1      = 1, /* ASCII PBM */
    PNM_P2      = 2, /* ASCII PGM */
    PNM_P3      = 3, /* ASCII PPM */
    PNM_P4      = 4, /* BINARY PBM */
    PNM_P5      = 5, /* BINARY PGM */
    PNM_P6      = 6, /* BINARY PPM */



# convert to P6 (binary)
convert image.ppm result.ppm

# convert to P3 (ASCII)
convert image.ppm -compress none result.ppm
sed -i -e 'N' -e '2b' -e 's/ /\n/g' 480x640a_2.ppm # 空格用换行符替换
sed -i '/^$/d' 480x640a_2.ppm #去空行 



其实python也可以转
tb在仿真输出文件的时候也可以二进制输出
hls在仿真的时候也可以二进制输出

P5去掉头其实就是raw文件





