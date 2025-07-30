'''
import numpy as np

# 定义 8 种颜色的 RGB 值
colors = [
    (255, 255, 255),  # 白色
    (255, 255, 0),    # 黄色
    (0, 255, 255),    # 青色
    (0, 255, 0),      # 绿色
    (255, 0, 255),    # 品红
    (255, 0, 0),      # 红色
    (0, 0, 255),      # 蓝色
    (0, 0, 0)         # 黑色
]

# 图像宽高
width = 640
height = 480

# 每个彩条的宽度
stripe_width = width // len(colors)

# 创建图像矩阵
image = np.zeros((height, width), dtype=np.uint16)

# 填充彩条
for i, (r, g, b) in enumerate(colors):
    start_x = i * stripe_width
    end_x = (i + 1) * stripe_width if i < len(colors) - 1 else width

    # 模拟 RGGB 的 Bayer 格式
    for y in range(height):
        for x in range(start_x, end_x):
            if (y % 2 == 0) and (x % 2 == 0):  # R
                image[y, x] = r << 4  # RAW12 数据左移 4 位
            elif (y % 2 == 0) and (x % 2 == 1):  # G (even row)
                image[y, x] = g << 4
            elif (y % 2 == 1) and (x % 2 == 0):  # G (odd row)
                image[y, x] = g << 4
            elif (y % 2 == 1) and (x % 2 == 1):  # B
                image[y, x] = b << 4

# 保存为 P2 格式的 PPM 文件
def save_as_p2_ppm(filename, image, width, height):
    with open(filename, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write("4095\n")  # RAW12 最大值
        for row in image:
            f.write(" ".join(map(str, row)) + "\n")

# 保存图像
output_filename = "color_bars_raw12.ppm"
save_as_p2_ppm(output_filename, image, width, height)

print(f"P2 格式的 PPM 文件已保存为 {output_filename}")
'''



'''
def generate_bayer_color_bars_ppm(width, height, bayer_pattern, filename):
    colors = {
        "R": 4095,  # 最大值 (12-bit RAW)
        "G": 2048,  # 中间值
        "B": 1024,  # 较低值
    }

    # 定义每种 Bayer 格式的排列方式
    bayer_patterns = {
        "RGGB": [["R", "G"], ["G", "B"]],
        "GRBG": [["G", "R"], ["B", "G"]],
        "BGGR": [["B", "G"], ["G", "R"]],
        "GBRG": [["G", "B"], ["R", "G"]],
    }

    if bayer_pattern not in bayer_patterns:
        raise ValueError(f"Unsupported Bayer pattern: {bayer_pattern}")

    bayer_grid = bayer_patterns[bayer_pattern]

    # 生成彩条（8个颜色）
    color_bars = [
        (colors["R"], colors["R"], colors["R"]),  # 白色
        (colors["R"], colors["G"], 0),             # 黄色
        (0, colors["G"], colors["B"]),             # 青色
        (0, colors["G"], 0),                        # 绿色
        (colors["R"], 0, colors["B"]),             # 品红
        (colors["R"], 0, 0),                        # 红色
        (0, 0, colors["B"]),                        # 蓝色
        (0, 0, 0),                                   # 黑色
    ]

    # 初始化图像
    image = []
    for y in range(height):
        row = []
        for x in range(width):
            bar_index = (x * 8) // width  # 当前像素所在的彩条
            color = color_bars[bar_index]

            # 计算 Bayer 像素值
            bayer_x, bayer_y = x % 2, y % 2
            channel = bayer_grid[bayer_y][bayer_x]

            if channel == "R":
                value = color[0]
            elif channel == "G":
                value = color[1]
            elif channel == "B":
                value = color[2]

            row.append(value)
        image.append(row)

    # 写入 P2 格式的 PPM 文件
    with open(filename, "w") as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write("4095\n")
        for row in image:
            for pixel in row:
                f.write(f"{pixel}\n")

if __name__ == "__main__":
    # 图像宽度和高度
    width = 640
    height = 480

    # 用户选择 Bayer 格式
    bayer_pattern = "RGGB"  # 可更改为 "GRBG", "BGGR", "GBRG"

    # 输出文件名
    output_filename = "color_bars_bayer.ppm"

    # 生成图像
    generate_bayer_color_bars_ppm(width, height, bayer_pattern, output_filename)

    print(f"Bayer color bars PPM generated: {output_filename}")

'''



def generate_bayer_ppm(width, height, bayer_pattern, bit_depth, filename):
    assert bayer_pattern in ["RGGB", "GRBG", "BGGR", "GBRG"], "Invalid Bayer pattern"
    assert bit_depth in [8, 10, 12, 16], "Bit depth must be one of 8, 10, 12, or 16"

    max_value = (1 << bit_depth) - 1  # Calculate max value based on bit depth

    # Define the 8 color stripes in RGB (normalized to 0-1 range)
    colors = [
        (1.0, 1.0, 1.0),  # White
        (1.0, 1.0, 0.0),  # Yellow
        (0.0, 1.0, 1.0),  # Cyan
        (0.0, 1.0, 0.0),  # Green
        (1.0, 0.0, 1.0),  # Magenta
        (1.0, 0.0, 0.0),  # Red
        (0.0, 0.0, 1.0),  # Blue
        (0.0, 0.0, 0.0),  # Black
    ]

    stripe_width = width // len(colors)  # Width of each color stripe

    # Create the Bayer RAW image
    raw_image = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            # Determine the stripe index based on the column position
            stripe_index = j // stripe_width
            r, g, b = colors[stripe_index]

            # Map RGB values to the Bayer pattern
            if bayer_pattern == "RGGB":
                if i % 2 == 0 and j % 2 == 0:
                    raw_image[i][j] = int(r * max_value)
                elif i % 2 == 0 and j % 2 == 1:
                    raw_image[i][j] = int(g * max_value)
                elif i % 2 == 1 and j % 2 == 0:
                    raw_image[i][j] = int(g * max_value)
                else:
                    raw_image[i][j] = int(b * max_value)

            elif bayer_pattern == "GRBG":
                if i % 2 == 0 and j % 2 == 0:
                    raw_image[i][j] = int(g * max_value)
                elif i % 2 == 0 and j % 2 == 1:
                    raw_image[i][j] = int(r * max_value)
                elif i % 2 == 1 and j % 2 == 0:
                    raw_image[i][j] = int(b * max_value)
                else:
                    raw_image[i][j] = int(g * max_value)

            elif bayer_pattern == "BGGR":
                if i % 2 == 0 and j % 2 == 0:
                    raw_image[i][j] = int(b * max_value)
                elif i % 2 == 0 and j % 2 == 1:
                    raw_image[i][j] = int(g * max_value)
                elif i % 2 == 1 and j % 2 == 0:
                    raw_image[i][j] = int(g * max_value)
                else:
                    raw_image[i][j] = int(r * max_value)

            elif bayer_pattern == "GBRG":
                if i % 2 == 0 and j % 2 == 0:
                    raw_image[i][j] = int(g * max_value)
                elif i % 2 == 0 and j % 2 == 1:
                    raw_image[i][j] = int(b * max_value)
                elif i % 2 == 1 and j % 2 == 0:
                    raw_image[i][j] = int(r * max_value)
                else:
                    raw_image[i][j] = int(g * max_value)

    # Write the P2 PPM file
    with open(filename, "w") as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_value}\n")

        # Write pixel values, one per line
        for row in raw_image:
            for value in row:
                f.write(f"{value}\n")

# Example usage
width = 640
height = 480
bayer_pattern = "RGGB"  # Choose from "RGGB", "GRBG", "BGGR", "GBRG"
bit_depth = 12  # Choose from 8, 10, 12, 16
filename = "color_bars_bayer.ppm"

generate_bayer_ppm(width, height, bayer_pattern, bit_depth, filename)
print(f"Bayer PPM file generated: {filename}")

