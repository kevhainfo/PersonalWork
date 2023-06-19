from problem import xs,ys
import matplotlib.pyplot as plt


def plotTSP(path):
    """
    path: List of lists with the different orders in which the nodes are visited
    points: coordinates for the different nodes
    num_iters: number of paths that are in the path list

    """

    # Unpack the primary TSP path and transform it into a list of ordered
    # coordinates

    x = []
    y = []
    for i in path:
        x.append(xs[i])
        y.append(ys[i])

    plt.plot(x, y, 'co')

    # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
    a_scale = float(max(x)) / float(100)/100

    # Draw the older paths, if provided


    xi = [];
    yi = [];
    for j in path:
        xi.append(points[j][0])
        yi.append(points[j][1])
    for i in range(0, len(x) - 1):
            plt.arrow(xi[i], yi[i], (xi[i + 1] - xi[i]), (yi[i + 1] - yi[i]),head_width=a_scale, color='r', length_includes_head=True, ls='dashed', width=0.001 / float(1))

    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width=a_scale,
              color='g', length_includes_head=True)
    for i in range(0, len(x) - 1):
        plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]), head_width=a_scale,
                  color='g', length_includes_head=True)

    # Set axis too slitghtly larger than the set of x and y
    plt.xlim(0, max(x) * 1.1)
    plt.ylim(0, max(y) * 1.1)
    plt.show()


if __name__ == '__main__':
    # Run an example

    # Create a randomn list of coordinates, pack them into a list
    x_cor = xs
    y_cor = ys
    points = []
    for i in range(0, len(x_cor)):
        points.append((x_cor[i], y_cor[i]))

   #h3 =[0, 33, 16, 30, 26, 18, 99, 14, 28, 23, 115, 94, 78, 37, 91, 72, 98, 73, 74, 51, 8, 56, 55, 64, 11, 86, 80, 76, 102, 81, 100, 122, 110, 118, 83, 35, 31, 112, 93, 88, 109, 97, 24, 47, 67, 62, 42, 103, 126, 106, 69, 96, 6, 25, 87, 85, 68, 63, 123, 128, 60, 108, 75, 10, 4, 44, 15, 127, 104, 61, 111, 116, 114, 27, 65, 84, 124, 89, 77, 120, 58, 29, 82, 2, 113, 125, 7, 107, 17, 20, 32, 21, 36, 39, 46, 22, 95, 12, 66, 9, 13, 121, 54, 101, 5, 90, 71, 48, 57, 105, 52, 119, 59, 50, 41, 43, 92, 19, 45, 79, 117, 3, 34, 53, 1, 49, 129, 70, 38, 40]
    path1=[0,4,2,3,1]
    plotTSP(path1)
