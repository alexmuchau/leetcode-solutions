from typing import List

def floodFill( image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  color_curr = image[sr][sc]
  if color_curr==color: return image

  n_row, n_col = len(image), len(image[0])
  visited = [[0]*n_col for _ in range(n_row)]
  image[sr][sc], l = color, [(sr, sc)]
  while l:
    ii, jj = l.pop(0)
    print(l)
    # print(ii, jj)
    up, right, down, left = (ii-1,jj), (ii,jj+1), (ii+1,jj), (ii,jj-1)
    directions = []
    if up[0]>=0: directions.append(up)
    if right[1]<n_col: directions.append(right)
    if down[0]<n_row: directions.append(down)
    if left[1]>=0: directions.append(left)
    # print(directions)
    for d in directions:
        if image[d[0]][d[1]]==color_curr and visited[d[0]][d[1]]==0:
            image[d[0]][d[1]] = color
            visited[d[0]][d[1]] = 1
            l.append(d)
  return image


print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))