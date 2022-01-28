for i in range(img_np.shape[1]):
    for j in range(img_np.shape[0]):
        cur_result_matrix = np.zeros((img_np.shape[0], img_np.shape[1]))
        if (img_np[j, i] == 0.0):
            cur_outer_zero = True
        for k in range(img_np.shape[1]):
            for l in range(img_np.shape[0]):
                if (img_np[l, k] == 0.0):
                    cur_inner_zero = True

                if (cur_outer_zero or cur_inner_zero):
                    cur_result_matrix[l, k] = 0
                elif (i == k and j == l):
                    cur_result_matrix[l, k] = 1
                else:
                    img_np[l, k] = 100.0  # set goal
                    path = bfs(img_np, (i, j), 0.0, 100.00)
                    if (path == None):
                        print("Unable to find path between nodes ", (i, j), "and", (k, l))
                        break
                    else:
                        cur_result_matrix[l, k] = len(path)
                        # reset
                        img_np[l, k] = 1.0
                cur_inner_zero = False
        adjacency_dict[i, j] = cur_result_matrix
    cur_outer_zero = False
